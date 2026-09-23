# Xiaolong Liu · 数学学术主页

这份文件夹可以直接作为 GitHub Pages 仓库使用。包括四个页面、原照片、两篇论文及可展开摘要、TeX 数学公式、完整本地字体，以及自动发布配置。不需要付费服务、数据库、API 密钥或安装前端工具。

## 第一次发布

1. 登录 GitHub，创建一个 **Public（公开）** 仓库，推荐名称：`你的GitHub用户名.github.io`。这样主页地址就是 `https://你的GitHub用户名.github.io/`。
2. 把解压后的**文件夹内全部内容**上传到仓库的根目录，使用 `main` 分支。根目录应直接看到 `index.html`、`assets`、`notes`、`friends`、`links`、`scripts` 和 `.github`，不要再套一层文件夹。不要仅上传 ZIP。
3. **必须包含 `.github/workflows/pages.yml`。** `.github` 是隐藏文件夹：macOS Finder 中按 `Command + Shift + .` 可以显示它，再一并上传。这里的 `.nojekyll` 和 `.gitignore` 也建议保留。
4. 在仓库打开 **Settings → Pages → Build and deployment → Source**，选择 **GitHub Actions**。网站已经附带发布配置，无需再创建模板。
5. 打开 **Actions → Publish academic homepage → Run workflow → Run workflow**。以后每次向 `main` 提交修改，都会自动更新网站。
6. 等待该次运行显示绿色完成标记。在 **Settings → Pages** 或该次运行的 `github-pages` 部署中打开正式网址。

如果第一次上传后 Actions 因 Pages 尚未启用而失败，完成第 4 步后，在 Actions 重新运行即可。

也可以使用其他仓库名称。发布配置会自动适配 `https://用户名.github.io/仓库名/`，包含子页面、图片、字体、公式、canonical 和站点地图。使用在 GitHub Pages 设置中配置的独立域名时，也会自动使用该域名。

## 日常修改

| 想修改的内容 | 对应文件 |
| --- | --- |
| 基本信息、研究、论文、报告 | `index.html` |
| 讲义 | `notes/index.html` |
| 朋友链接 | `friends/index.html` |
| 资料链接 | `links/index.html` |
| 照片 | `assets/xiaolong-liu.jpg` |
| 配色、字号、留白 | `assets/style.css` |
| TeX 宏 | `assets/mathjax-config.js` |

网页内容都是普通 HTML。只改文字时不用调整发布配置。修改后提交到 `main` 即可自动发布。`_site` 是发布过程中生成的目录，不要手动修改或上传。

Basic Information 按你提供的原文保留为 fourth-year graduate (& second-year Ph.D.)，分为三组条目。两篇论文分别链接到 arXiv:2609.17720 和 arXiv:2507.21582，PDF 链接直接打开 arXiv 的 PDF 页面。

## 数学公式和摘要

标题、正文和摘要都支持行内与独立公式，例如：

```tex
行内：$\mathbb{C}^4$ 或 \(\mathbb{C}^4\)
独立公式：\[ \sum_{n \geq 0} a_n q^n \]
```

MathJax 使用本地文件，支持常用数学命令及 AMS 数学环境。支持的是数学公式语法，不是整份 LaTeX 文档的编译。`\CC`、`\ZZ`、`\RR` 的宏定义位于 `assets/mathjax-config.js`。

每篇论文的摘要使用 `<details class="abstract">`，按钮使用 `<summary>`。新增论文时复制已有的 `<article class="paper">`，再修改论文信息、链接和摘要。摘要文本始终包含在 HTML 里，点击展开无需额外联网。

## Google 收录

网站已包含中英文姓名、标题、描述、人物与论文结构化数据。发布时会根据正式网址自动生成 canonical、Open Graph URL、`sitemap.xml` 和 `robots.txt`。没有保留旧的临时托管地址。

发布成功后：

1. 使用自己的 Google 账号打开 [Google Search Console](https://search.google.com/search-console/)。
2. 添加「网址前缀」资源，填写 GitHub Pages 的**正式完整网址**。
3. 选择 HTML 文件验证，将 Google 提供的验证文件原样上传到仓库根目录。网站发布后返回 Search Console 完成验证。也可使用首页 `<head>` 内的 meta 标签验证。无需把账号密码交给任何人。
4. 在「站点地图」中提交 `sitemap.xml`。
5. 在「网址检查」中检查首页，并请求编入索引。
6. 在原 Google Sites 主页和可以编辑的机构个人资料中添加新主页链接，帮助搜索引擎发现新地址。

GitHub Pages 的访问环境、Google 抓取与排名由相应服务决定；这些设置提供正常收录所需的技术基础，不能保证收录时间或姓名搜索排名。普通仓库网站的 `robots.txt` 位于仓库子路径；Google 只把域名根目录的 robots.txt 作为抓取规则，因此这类网站应直接在 Search Console 提交站点地图。

## 本地查看（可选）

在这份文件夹中运行：

```sh
python3 -m http.server 8000
```

然后打开 `http://localhost:8000/`。图片、公式、字体与页面导航都在本地，无需 Google Fonts 或其他外部 CDN。

如需手动生成正式发布文件：

```sh
python3 scripts/build.py --base-url https://你的GitHub用户名.github.io
```

生成结果在 `_site/`。正常 GitHub Actions 发布不需要手动执行这一步；配置会自动提供正确网址。

## 字体与资源

- 标题与正文：EB Garamond。
- 导航与辅助信息：Source Sans 3。
- 年份、日期、章节编号及 L 标志：Courier Prime。
- 浏览器图标使用 Courier Prime 的 L 字形轮廓，不依赖设备上安装的字体。
- 配色：墨蓝、酒红与暖灰。Research 介绍段落使用酒红色 M 首字下沉。
- 字体许可证与来源：`assets/fonts/` 中的 OFL 文件和 `PROVENANCE.txt`。
- 数学组件许可证：`assets/MATHJAX-LICENSE`。

照片和文字仍属于各自权利人；字体与数学组件遵循附带的开源许可。

## 官方参考

- [GitHub Pages 发布源设置](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub Pages 自定义工作流](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [Google 搜索技术要求](https://developers.google.com/search/docs/essentials/technical)
- [Google 站点地图说明](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [请求 Google 抓取](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)
