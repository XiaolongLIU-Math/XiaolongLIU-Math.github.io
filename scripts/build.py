#!/usr/bin/env python3
"""Build a dependency-free GitHub Pages site with the actual deployment URL."""
import argparse
import html
import json
import os
from pathlib import Path
import shutil
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET
import re

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--base-url', default=os.environ.get('SITE_URL', ''))
parser.add_argument('--output', default='_site')
args = parser.parse_args()
base_url = args.base_url.strip().rstrip('/')
url = urlsplit(base_url)
if url.scheme not in ('https', 'http') or not url.netloc or url.username or url.query or url.fragment:
    parser.error('Provide the public site URL with --base-url or SITE_URL (no query or fragment).')
output = (ROOT / args.output).resolve()
if output == ROOT or output in ROOT.parents or (output.exists() and not (output / '.math-site-output').exists()):
    parser.error('Output must be a new directory, or one previously created by this build script.')
output.mkdir(parents=True, exist_ok=True)
(output / '.math-site-output').write_text('Generated site output\n')
# Clear only output previously created by this script, to avoid stale pages.
for entry in output.iterdir():
    if entry.name == '.math-site-output':
        continue
    if entry.is_dir():
        shutil.rmtree(entry)
    else:
        entry.unlink()

# Static pages/assets, and optional Google verification files or custom domain.
for item in ROOT.iterdir():
    if item.resolve() == output or item.name.startswith('.'):
        continue
    if item.is_dir() and (item.name == 'assets' or (item / 'index.html').exists()):
        shutil.copytree(item, output / item.name)
    elif item.is_file() and (item.suffix in {'.html', '.xml', '.txt', '.ico', '.svg', '.png'} or item.name == 'CNAME'):
        shutil.copy2(item, output / item.name)
(output / '.nojekyll').write_text('')


def absolute_ids(value):
    if isinstance(value, dict):
        result = {key: absolute_ids(v) for key, v in value.items()}
        if result.get('@type') in ('Person', 'ProfilePage'):
            result['url'] = base_url + '/'
        return result
    if isinstance(value, list):
        return [absolute_ids(v) for v in value]
    if isinstance(value, str) and value.startswith('#'):
        return base_url + '/' + value
    return value


page_urls = []
for page in sorted(output.rglob('*.html')):
    content = page.read_text(encoding='utf-8')
    if '</head>' not in content:
        continue  # Preserve verification files exactly.
    path = page.relative_to(output).as_posix()
    route = path[:-10] if path.endswith('index.html') else path
    page_url = base_url + '/' + route
    content = re.sub(r'<link rel="canonical"[^>]*>\s*', '', content)
    content = re.sub(r'<meta property="og:url"[^>]*>\s*', '', content)
    metadata = ('<link rel="canonical" href="' + html.escape(page_url, quote=True) + '">\n'
                '<meta property="og:url" content="' + html.escape(page_url, quote=True) + '">\n')
    content = content.replace('</head>', metadata + '</head>')
    def update_json(match):
        data = absolute_ids(json.loads(match.group(1)))
        return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False).replace('</', '<\\/') + '</script>'
    content = re.sub(r'<script type="application/ld\+json">(.*?)</script>', update_json, content, flags=re.S)
    page.write_text(content, encoding='utf-8')
    if path != '404.html':
        page_urls.append(page_url)

ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
sitemap = ET.Element(ns + 'urlset')
for page_url in page_urls:
    entry = ET.SubElement(sitemap, ns + 'url')
    ET.SubElement(entry, ns + 'loc').text = page_url
ET.ElementTree(sitemap).write(output / 'sitemap.xml', encoding='utf-8', xml_declaration=True)
(output / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + base_url + '/sitemap.xml\n')
print(f'Ready: {len(page_urls)} pages, canonical URLs and sitemap for {base_url}/')
