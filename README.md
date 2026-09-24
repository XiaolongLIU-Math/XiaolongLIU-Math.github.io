# Xiaolong Liu · 数学学术主页

这份文件夹可以直接作为 GitHub Pages 仓库使用。包括六个页面、原照片、两篇论文及可展开摘要、TeX 数学公式、完整本地字体，以及自动发布配置。不需要付费服务、数据库、API 密钥或安装前端工具。

## 第一次发布

1. 登录 GitHub，创建一个 **Public（公开）** 仓库，推荐名称：`你的GitHub用户名.github.io`。这样主页地址就是 `https://你的GitHub用户名.github.io/`。
2. 把解压后的**文件夹内全部内容**上传到仓库的根目录，使用 `main` 分支。根目录应直接看到 `index.html`、`assets`、`notes`、`friends`、`links`、`experts`、`tools`、`scripts` 和 `.github`，不要再套一层文件夹。不要仅上传 ZIP。
3. **必须包含 `.github/workflows/pages.yml`。** 如果浏览器提示隐藏文件无法上传，在仓库选择 **Add file → Create new file**，文件名填 `.github/workflows/pages.yml`，复制本文件夹中对应文件的内容并提交。已经配置过的网站无需重复操作。
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
| 学者主页 | `experts/index.html` |
| 数学工具 | `tools/index.html` |
| 照片 | `assets/xiaolong-liu.jpg` |
| 配色、字号、留白 | `assets/style.css` |
| TeX 宏 | `assets/mathjax-config.js` |

网页内容都是普通 HTML。只改文字时不用调整发布配置。修改后提交到 `main` 即可自动发布。`_site` 是发布过程中生成的目录，不要手动修改或上传。

Basic Information 按你提供的原文保留为 fourth-year graduate (& second-year Ph.D.)，分为三组条目。两篇论文分别链接到 arXiv:2609.17720 和 arXiv:2507.21582，PDF 链接直接打开 arXiv 的 PDF 页面。

## 已有网站：上传更新文件

本仓库是 `XiaolongLIU-Math/XiaolongLIU-Math.github.io`，主页是 <https://xiaolongliu-math.github.io/>。

1. 解压更新包，打开解压后的文件夹。
2. 打开 [仓库根目录的上传页面](https://github.com/XiaolongLIU-Math/XiaolongLIU-Math.github.io/upload/main)。
3. 将更新包内的文件和子文件夹一起拖入上传区，保留原有目录结构；不要上传 ZIP 或外面那层包装文件夹。
4. 选择直接提交到 `main`，点击 **Commit changes**。同路径文件会被替换，新路径文件会新增；其他文件不会因此删除。
5. 到仓库顶部的 **Actions** 等待 **Publish academic homepage** 显示绿色完成标记，再刷新主页。

不用先删除旧文件，也不用重新设置 Pages 或 Search Console。Google 所有权验证文件应一直保留。

## 新增论文模板

打开 `index.html`，搜索中文注释 `Research：每篇论文`。把下面完整区块放在第一篇论文的 `<article class="paper">` 前面，即可把新论文排在最上面。不要放进其他论文的 `article` 内。

将 `PAPER_TITLE`、`YEAR`、`PAGE_COUNT`、`ARXIV_ID`、`ABSTRACT_TEXT` 和 `VERSION_DATE` 换成实际内容。`ARXIV_ID` 共出现三次，都要修改；例如 `2609.17720`。标题、摘要都支持 TeX 公式。多段摘要可以增加更多 `<p>...</p>`。

```html
<!-- 新论文 -->
<article class="paper">
  <div class="paper-meta">
    <span>Preprint</span>
    <span>YEAR</span>
  </div>

  <h3>PAPER_TITLE</h3>
  <p class="byline">
    Xiaolong Liu <span class="byline-separator">·</span> PAGE_COUNT pages
  </p>

  <div class="paper-actions">
    <a href="https://arxiv.org/abs/ARXIV_ID">
      arXiv:ARXIV_ID <span aria-hidden="true">↗</span>
    </a>
    <a href="https://arxiv.org/pdf/ARXIV_ID">
      PDF <span aria-hidden="true">↗</span>
    </a>
  </div>

  <details class="abstract">
    <summary>
      <span class="abstract-closed">Abstract</span>
      <span class="abstract-open">Hide abstract</span>
      <span class="toggle-symbol" aria-hidden="true"></span>
    </summary>
    <div class="abstract-content">
      <p>ABSTRACT_TEXT</p>
    </div>
  </details>

  <!-- 例如：17 September 2026 · v1 -->
  <p class="version">VERSION_DATE · v1</p>
</article>
```

作者有合作者时，直接修改 `byline` 中的作者列表。已投稿或发表时，可以修改 `Preprint`，并按已有论文的格式增加状态或期刊信息。

文件末尾的 `搜索引擎信息` 中另有现有论文的 `ScholarlyArticle` 信息。修改现有论文的标题、日期、摘要时，请同步对应的 `name`、`datePublished` / `dateModified`、`abstract`；它们不控制网页显示。新增论文只添加上面的 HTML 就能正常显示，无需为了发布而手动增加这一可选数据。HTML 正文中的 TeX 使用单个反斜杠；JSON 字符串中的反斜杠需要写成 `\\`。

## 新增 Talk 模板

打开 `index.html`，搜索中文注释 `Talks：按年份`。找到相应年份的 `<ol class="talk-list">`，把下面整个 `<li>...</li>` 区块放在该列表内，按日期从新到旧排序。

每场报告统一分成三组：日期和标题；书本图标加会议／研讨班名称；定位图标加学校／研究所、城市、国家。长文字会自动换行，无需手动添加 `<br>`。没有专门活动名称时，将 `EVENT_NAME` 写成 `Invited talk`。

```html
<!-- 新报告：填写日期 -->
<li>
  <!-- 第一行：datetime 用 YYYY-MM-DD，显示日期用 10 Apr 这样的格式 -->
  <time datetime="YYYY-MM-DD">DAY MON</time>
  <div>
    <h4>TALK_TITLE</h4>

    <!-- 第二行：会议／研讨班名称 -->
    <p class="talk-event">
      <svg class="talk-icon" aria-hidden="true"><use href="#icon-book"></use></svg>
      <span>EVENT_NAME</span>
    </p>

    <!-- 第三行：学校／研究所 · 城市, 国家 -->
    <p class="talk-location">
      <svg class="talk-icon" aria-hidden="true"><use href="#icon-location"></use></svg>
      <span>INSTITUTION · CITY, COUNTRY</span>
    </p>
  </div>
</li>
```

需要会议链接时，把 `<span>EVENT_NAME</span>` 换成下面这一段；学校／研究所名称也可以用同样方法加链接：

```html
<span>
  <a href="https://example.org/meeting">EVENT_NAME</a>
</span>
```

新增年份时，在现有年份上方、Talks 的 `<div class="section-body">` 内加入以下区块，再把 Talk 模板放到 `ol` 里面。将 `YEAR` 换成实际年份：

```html
<h3 class="year-heading">YEAR</h3>
<ol class="talk-list">
  <!-- 把该年份的报告 li 区块放在这里 -->
</ol>
```

只增删论文或报告时，通常只需上传修改后的 `index.html`。`<!-- ... -->` 是编辑提示，不会显示在网页上。普通文字中的 `&` 请写成 `&amp;`，小于号请写成 `&lt;`。

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
