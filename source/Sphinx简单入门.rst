###############
Sphinx 简单入门
###############

Sphinx 是一个用于生成 Python 文档的工具, 但是也可以用来制作电子书. 本文记录使用该工具的一些经验.

首先使用 Sphinx 的自动配置工具
==============================

.. highlight:: none

在准备好的工作目录下, 运行 ``sphinx-quickstart`` 将会弹出一堆文本, 并让你在其中选择要使用的配置, 一般情况下, 只需要手动修改两项, 其他保持默认即可. 让我们来看看 Sphinx 询问了我们哪些问题吧.

::

    Welcome to the Sphinx 1.8.1 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Selected root path: .

选择当前工作目录为项目根目录.

::

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: y

是否将源文件(使用 .rst 或 .md 标记语言写的文档)和生成文件(html 或 epub, pdf 等)分开放置在不同的目录

::

    Inside the root directory, two more directories will be created; "_templates"
    for custom HTML templates and "_static" for custom stylesheets and other static
    files. You can enter another prefix (such as ".") to replace the underscore.
    > Name prefix for templates and static dir [_]:

对于模板或静态目录(文件不被解析渲染), 设它们的前缀为 `_`.

::

    The project name will occur in several places in the built documentation.
    > Project name: Learn-Sphinx
    > Author name(s): Zombie110year
    > Project release []:

分别是 项目名, 作者名, Project release 是指项目发布版本, 根据实际项目来填.

::

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    http://sphinx-doc.org/config.html#confval-language.
    > Project language [en]: zh_CN

选择项目语言, 默认是英语, 用 zh_CN 表示简体中文, 可以在上面那个链接看支持的语言以及其表示代码. 这个选项会影响搜索功能, 英文情况下, 会以英语存储搜索索引, 这样就无法使用中文搜索. 搜索功能是用 JavaScript + 字典实现的.

::

    The file name suffix for source files. Commonly, this is either ".txt"
    or ".rst".  Only files with this suffix are considered documents.
    > Source file suffix [.rst]:

文档文件后缀, 只有拥有这些后缀的文件才会被解析, 在当前使用的版本(v1.8.2)中只能接受 .rst 与 .txt 后缀(但都是以 reStructuredText 的语法进行解析). 要解析 Markdown, 需要安装额外的插件 recommonmark, 这个稍后再讲.

::

    One document is special in that it is considered the top node of the
    "contents tree", that is, it is the root of the hierarchical structure
    of the documents. Normally, this is "index", but if your "index"
    document is a custom template, you can also set this to another filename.
    > Name of your master document (without suffix) [index]:

这个是主文件, 对于 html, 就是指 index.html 等能够被浏览器直接默认显示的. 建议保持默认.

接下来就是插件配置. 这里的都是默认插件, 其中 imgmath 和 mathjax 不能同时选.

::

    Indicate which of the following Sphinx extensions should be enabled:
    > autodoc: automatically insert docstrings from modules (y/n) [n]: y
    > doctest: automatically test code snippets in doctest blocks (y/n) [n]: n
    > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
    > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
    > coverage: checks for documentation coverage (y/n) [n]: n
    > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: n
    > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
    > ifconfig: conditional inclusion of content based on config values (y/n) [n]: y
    > viewcode: include links to the source code of documented Python objects (y/n) [n]: y
    > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y

然后询问是否创建 Makefile 或者 Windows 的批处理脚本, 这是为了方便使用 ``make xxx`` 来构建文档.

::

    A Makefile and a Windows command file can be generated for you so that you
    only have to run e.g. `make html' instead of invoking sphinx-build
    directly.
    > Create Makefile? (y/n) [y]: y
    > Create Windows command file? (y/n) [y]: y

就算在 quickstart 中有选项不满意, 也可以在接下来的 `conf.py` 中修改.

如何规划目录结构
================

在运行了如上的 sphinx-quickstart 程序后, 目录下出现了以下文件/目录:

::

    ├─build
    └─source
        ├─_static
        ├─_templates
        |  conf.py
        |  index.rst
      Makefile

在根目录下设置了 ``Makefile`` 便于使用 make 工具自动构建, 而配置文件和索引则放在了 source 目录下.
如果需要修改文件规划, 那么, 可以在 Makefile 中修改 ``BUILDDIR`` 和 ``SOURCEDIR`` 两项目.

插件介绍
========

官方插件
--------

- autodoc: 自动从模块中抽取 docstring 插入文档
- doctest: 自动测试 doctest
- intersphinx: 链接多个 Sphinx 文档. 需要启用它才能使用 :mod:`os` 这样的语法链接到官方文档
- todo: 写下 todo 在文件头部时, 将不会渲染该文件
- coverage: 检查封面
- imgmath: 将数学公式渲染为 png 或 svg 图像
- mathjax: 使用 Mathjax 渲染数学公式
- ifconfig: 通过配置的条件判断决定文档包含
- viewcode: 将源代码包含进文档项目, 并在 api 文档中创建指向源代码的链接
- githubpages: create .nojekyll file to publish the document on GitHub pages

第三方插件
----------

- :doc:`graphviz`, 可在文档中嵌入 graphviz 代码, 在构建时生成图片
- :doc:`matplotlib`, 在文档中嵌入 matplotlib 代码, 在构建时生成图片

toctree
========

在 source 目录下添加 .rst 文件, 但是如果要在编译项目后从首页 (index.html) 进行访问, 还需要在 index.rst 中将这个文件添加到 ``toctree`` 中. 在原始的 index.rst 中, 应当有如下 toctree.

::

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

要在 toctree 中添加一个文件, 应当在上面那个 toctree 结构下空一行, 添加文件名(不需要扩展)

例如, 有一个 example.rst 就将 toctree 编辑为

::

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       example

如果, 在 source 目录中, 添加了子目录, 将文档放在子目录里了, 那么, 只需要在原来 example 里面按相对于 index.rst 的路径填就可以了, 例如 /source/text/example.rst 就填:

::

    .. toctree::
       :maxdepth: 2

       text/example

toctree 参数
------------

toctree 下的 ``:maxdepth: 2``, ``:caption: Contents:`` 等就是它的参数, 可以选用的参数有:

- ``:maxdepth: n`` 将目录的标题深度设为 n. 意思是 example 文件为目录的根标题, 在这个标题下, 会建立文件中的 1, 2, ..., n 级标题的索引.
- ``:numbered:`` 给标题自动编号.
- ``:caption: xxx``

更改 html 页面主题
==================

默认的 html 页面看起来并不是很好看, 可以使用 pip 安装 ``sphinx_*_theme`` 等包, 然后在 ``conf.py`` 中引用, 就可以使用更多的主题.

例如 `sphinx_rtd_theme <https://sphinx-rtd-theme.readthedocs.io/en/latest/` 这个受很多人欢迎的主题.

.. code-block:: sh

    # 下载
    pip install sphinx_rtd_theme

::

    # conf.py 中配置
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'

在 GitHub Page 上展示文档
=========================

在使用 Sphinx 构建完毕后, 生成的 html 项目可以直接拿来用.

GitHub Page 可以将 master, gh-pages 分支下的根目录或 master 分支的 /doc 目录渲染成页面.

为了方便管理, 可以在 build/html 目录下新建一个 git 仓库, 并重命名为 gh-pages 分支. 将这个分支 push 到 github 的 gh-pages 上, 充当 GitHub Page 的资源. (注意, build 目录应当在根目录下的 .gitignore 中被忽略)

这样, 在项目根目录只需要一个 master 分支, 在这个分支编辑源文件, 然后 ``make html``, ``git add *``, ``git commit``, ``git push``, 之后就进入 ``build/html`` 目录, 再 ``git`` 一通即可. 非常舒服.
