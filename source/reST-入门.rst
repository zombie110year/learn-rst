############
入门 |a_rst|
############

由于使用 |a_rst| 的情况以撰写文档居多，因此我们以 Sphinx 为入口学习 |a_rst|。
要开始一个 Sphinx 项目，可以使用其提供的命令行工具 :program:`sphinx-quickstart`
来创建一个模板项目。

按照命令行的指引，将在当前文件夹生成以下文件结构::

    build/
    source/
        conf.py
        index.rst
    Makefile

其中， *build* 是 sphinx 的输出目录，其中按照输出格式不同划为多个文件夹，
例如 html 输出将位于 *build/html*，对于每一种输出格式，都会生成 *build/doctree*，
这是 sphinx 用于缓存文档结构的目录。

*source* 目录则是原始 |a_rst| 文档存储的位置，sphinx 将会根据其中的内容生成文档。

*source/conf.py* 是对 sphinx 的配置，以 Python 的形式存储配置。

*source/index.rst* 是整个文档的入口。

*Makefile* 是便于控制此文档编译的脚本，在 Windows 下会生成替代的 *make.bat* 脚本。
你可以使用 `make html` 来一键生成 HTML 输出。*source* 目录和 *build* 目录其实是由 Makefile
决定的，其默认内容如下：

.. code:: makefile

    # Minimal makefile for Sphinx documentation

    # You can set these variables from the command line.
    SPHINXOPTS    =
    SPHINXBUILD   = sphinx-build
    SOURCEDIR     = source
    BUILDDIR      = build

    # Put it first so that "make" without argument is like "make help".
    help:
        @$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

    .PHONY: help Makefile

    # Catch-all target: route all unknown targets to Sphinx using the new
    # "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
    %: Makefile
        @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

可以看到，输出格式以 `-M <format>` 选项传递给 sphinx-build 程序，*build*, *source* 目录也是它的参数。
你可以在 Makefile 中修改 Makefile 变量 `SOURCEDIR` 和 `BUILDDIR` 来修改这两个目录的路径。

在 *source/index.rst* 中，需要有一个 `toctree` directive 来表达该文档的整体结构。
例如，假设文件结构如下::

    source/
        index.rst
        conf.py
        一篇新文档.rst
        anothor-document.rst

那么，为了将所有文档串联起来，需要在 *source/index.rst* 中编辑：

.. code:: rst

    .. toctree::

        一篇新文档
        anothor-document

在 directive 空一行并缩进一次后的文本将被作为 content 传递给 directive，
该 toctree 接收到的 content 是两行文件名（无需后缀名）。
这将在目录中添加此两篇文档，并且在 index 页面上创建链接列表。

实际上，未输入 toctree 的文档也会被渲染，只不过可能无法通过超链接访问。

单篇 |a_rst| 文档的内建标记
===========================

`toctree` 是 sphinx 提供的，来自于 docutils 的内建标记可以满足单篇文档的表达需求。
这些内建的标记在 :doc:`reST-标记规范` 的总览章节已经很好地描述了，建议先去阅读第一部分。
剩下的内容旨在完整地表述 |a_rst| 的规范，不需要在此时阅读。

此后地内容会尽可能地与使用时的需求对照。

段落
----

|a_rst| 最基本的被识别的结构是段落。一个段落就是一段用空行与其他结构进行分隔的文本区域。
在一个段落中，可以用换行来划分不同的部分，只要它们中间没有产生空行就会被解析为同一个段落。
这个特性主要是考虑到在纯文本编辑器中，避免编写太长的行，以至于无法在屏幕上显示（旧的基于终端的文本编辑器可能存在此问题）。
但这些文本行需要有相同的缩进 -- 即它们的左边缘需要对齐。如果有缩进的段落，则在语义上表示一段引言。例如::

    这是一个段落，有点短。
    新的一行具有相同缩进，那么这两句是同一段。

        如果加一个缩进，那么这一段在渲染时也会缩进；
        通常用来表达引言语义。

            -- 沃・兹基硕德

    缩进结束后又变成普通的段落。

渲染效果如下：

这是一个段落，有点短。
新的一行具有相同缩进，那么这两句是同一段。

    如果加一个缩进，那么这一段在渲染时也会缩进；
    通常用来表达引言语义。

        -- 沃・兹基硕德

缩进结束后又变成普通的段落。

在需要保留段落的换行情况时，可以在行首使用管道符 ``|`` 来创建 line block::

    | 你好世界，虽然没有空行，
    | 但仍然换行了。
    | 而且它们在同一个段落中。

| 你好世界，虽然没有空行，
| 但仍然换行了。
| 而且它们在同一个段落中。

内联标记
--------

在段落和其他块元素内，可以使用内联的文本记号来为某个片段的文本标记语义。
例如 `*着重*`，`**强调**` 表达对应的语义，在默认情况下，它们在样式上会被渲染为 *斜体* 和 **粗体** 。

.. tip::

    你可以将内联标记想象成特殊的『括号』，并以相同的形式使用它们 --
    在标记文本的前后使用它们。由空格包围或单词中间的内联标记不会被识别，
    详细信息参考 :doc:`reST-标记规范`。

实际上，这些内联标记都是 :doc:`reST-角色` 的简写，有：

着重
    实际上是 `emphasis` 角色，用一对单星号表示::

        *着重*，:emphasis:`着重`

    *着重*，:emphasis:`着重`

强调
    实际上是 `strong` 角色，一对双星号表示::

        **强调**，:strong:`强调`

    **强调**，:strong:`强调`

字面量
    实际上是 `literal` 角色，用一对双反引号表示::

        ``字面量``，:literal:`字面量`

    ``字面量``，:literal:`字面量`

.. _标题参考:

标题参考
    `title-reference` 角色，别名 `title` 或 `t`，它也可以用一对单反引号表示::

        `入门 |a_rst|`，:title:`入门 |a_rst|`

    `入门 |a_rst|`，:title:`入门 |a_rst|`

    虽然它的默认渲染样式和着重一样，都是 *斜体*，但更重要的是语义，对吧？

    一般，会这么用::

        :title:`不存在的章节` [不存在的书籍]_

        .. [不存在的书籍] 《冇书》

    :title:`不存在的章节` [不存在的书籍]_

    .. [不存在的书籍] 《冇书》

.. _解释性文本角色:

解释性文本角色
    即一对单反引号所包括的文本角色。它默认指 标题参考_，
    但可以用一个 `default-role` 指令更改它在接下来的文本处理中的行为::

        .. default-role:: math

        现在是数学角色了： `\LaTeX`

        .. default-role:: literal

        `现在是字面量了`

    .. default-role:: math

    现在是数学角色了： `\LaTeX`

    .. default-role:: literal

    `现在是字面量了`

另外的内联标记需要以完整的角色形式表述，它们是：

代码
    `code` 角色::

        :code:`println!("{}", 8usize)`

    :code:`println!("{}", 8usize)`

    默认的代码角色是回退到 literal 的，没有高亮，
    可以通过 role 指令创建新的代码角色以启用高亮::

        .. role:: code-py(code)
            :language: python

        这是一行 Python 代码： :code-py:`print(f"{8}")`

    .. role:: code-py(code)
        :language: python

    这是一行 Python 代码： :code-py:`print(f"{8}")`

    由于 docutils 使用 pygments 作为高亮分析器，所以只能支持高亮
    pygments 实现了词法分析器的语言。

    你可以打开浏览器开发者工具查看上面 code-py 的 DOM 结构，
    可以发现已经分词了，但不知道哪里出了问题，既没有高亮，还把引号给转义了。

数学
    `math` 角色，用来表示一段内联的数学公式::

        :math:`\LaTeX`

    根据生成器的配置，可能使用 MathJax, KaTeX 渲染，
    或者使用本地 LaTeX 编译成 SVG 嵌入。

    这个得看生成器的配置，docutils 只管语义表达。
    Sphinx 默认使用 MathJax，但是推荐使用以下设置配置成 :math:`\KaTeX`，
    比前者性能高出不少：

    .. code:: python

        # conf.py

上标与下标
    上标是 `superscript` ，别名 `sup`，下标是 `subscript`，`sub`。
    由于内联标记需要与其他构造保持一个空格，因此像这样的写法是不会按预期渲染的::

        He:sub:`2`:sup:`4`

    He:sub:`2`:sup:`4`

    你需要用空格隔开的同时，将空格转义以便在输出中不渲染它们::

        He\ :sub:`2`\ :sup:`4`

    He\ :sub:`2`\ :sup:`4`

    呕，在 HTML 中表达化学符号真是一件难事，我还是用 :math:`\LaTeX` 吧：
    :math:`\text{He}_{2}^{4}` 。

原始
    `raw` 角色，表示将内容原封不动地传递给输出。
    这个角色不能直接使用，而是使用 `role` 指令定义一个新角色，并指定输出格式::

        .. role:: html(raw)
            :format: html

    这样，将会限制其只在 html 输出格式下以原始文本渲染该角色的内容，而在其他输出格式下，将如同注释一般不会渲染。

    例如::

        .. role:: raw-html(raw)
            :format: html

        .. role:: raw-latex(raw)
            :format: latex

        在 HTML 中，将会渲染
        :raw-html:`<ruby><rb>拼</rb><rt>pin</rt><rb>音</rb><rt>yin</rt></ruby>`，
        而 :raw-latex:`怎么做哦` 应该是不会在 HTML 输出中渲染的。

    .. role:: raw-html(raw)
        :format: html

    .. role:: raw-latex(raw)
        :format: latex

    在 HTML 中，将会渲染
    :raw-html:`<ruby><rb>拼</rb><rt>pin</rt><rb>音</rb><rt>yin</rt></ruby>`，
    而 :raw-latex:`怎么做哦` 应该是不会在 HTML 输出中渲染的。

    .. warning::

        raw 角色本身在某格式下的 :raw:`渲染样式` 是未定义的。

列表
----

有三种风格来表示一列项目。无序列表用 `*`, `-`, `+` 做项目符号，
有序列表可以用 数字、字母、罗马数字 加上 点（`.`）、右英文括号（`)`）或用英文括号完全包围 -- 无论你偏好什么，都能识别::

    *   无序 1

    -   无序 2

    +   无序 3

    1.  有序 1

    2)  有序 2)

    (3) 有序 (3)

    i.  有序 一

    II.  有序 贰

    c.  有序 three

*   无序 1

-   无序 2

+   无序 3

1.  有序 1

2)  有序 2)

(3) 有序 (3)

i.  有序 一

II.  有序 贰

c.  有序 three

.. tip::

    无序列表的项目符号可以混用，只需要保持缩进即可。

    但有序列表的项目符号不可混用，并且需要保持编号连续且单调。
    不过，你可以使用 `#` 符号来进行编号的自动推导::

        1. 第一项
        #. 第二
        #. 第三

    1. 第一项
    #. 第二
    #. 第三

列表可以通过增减缩进来表达嵌套关系::

    -   无序 1

        1. 可嵌套有序
        #. 有序 2

    -   无序回来

-   无序 1

    1. 可嵌套任意类型列表，例如有序列表
    #. 有序 2

-   无序回来

超链接
------

|a_rst| 一个超链接需要有两个部分：引用和靶标::

    引用部分需要在名称后加下划线：链接_
    如果名称中包含了空格，则需要用反引号包括起来：`链 接`_。

    靶标部分的下划线在名称前面：

    .. _链接: https://docutils.sourceforge.io/docs/user/rst/quickref.html

    如果留空，则会将靶标引至下一个块元素。

引用和靶标也可以写在同一处::

    `名称 <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`__

    即 `name <target>`_ 的形式。前者将会渲染为显示名称，后者将会作为靶标。

靶标也有内联形式，例如::

    _`靶标` 在这里，而引用将会引至前面的 靶标_ 处。

_`靶标` 在这里，而引用将会引至前面的 靶标_ 处。

隐式超链接可以将引用引至标题::

    正如下面的 `标题`_ 章节所说一样。

正如下面的 `标题`_ 章节所说一样。

任何满足 Uri 形式的文本会在渲染流程的最后被识别为超链接::

    -   https://docutils.sourceforge.io/docs/user/rst/quickref.html#hyperlink-targets
    -   ftp://firefox.fake-mozilla.org/

-   https://docutils.sourceforge.io/docs/user/rst/quickref.html#hyperlink-targets
-   ftp://firefox.fake-mozilla.org/

标题
----

标题是划分章节的依据。将单行文本缀以下划符号则构成标题。
可用的符号有 :literal:`#=-~:'"^_*+<>`，以及反引号。
需要满足长度条件：下划符号的数目与标题文本一致，（中文这类宽字符算两个字符）。

章节的大小关系与符号无关，只与符号出现的顺序有关。一般来讲，习惯用 `#` 做一级标题，`=`, `-` 分别做 二、三 级标题。

并且，可以使用双划线::

    ##########
    双划线风格
    ##########

    单划线风格
    ==========

标题本身会提供一个锚点，可以使用 `超链接`_ 的方式来指向本文的一个章节::

    `标题`_

例子：`标题`_ 。

分割线
------

任何四个以上的重复横线将会渲染为分割线::

    ----

----

常用指令
========

任何满足::

    +-------+-------------------------------+
    | ".. " | directive type "::" directive |
    +-------+ block                         |
            |                               |
            +-------------------------------+

例如::

    .. image:: example.png

形式的块都将尝试作为指令解析。

紧跟着指令名之后的内容为指令的 argument，
在指令后一行，添加缩进并以字段列表的形式输入的为指令的 options，
在 options 后空一行，并相对指令缩进一次的输入，是指令的 content::

    .. {{ 指令名 }}:: {{ argument }}
        :{{ field name }}: {{ field value }}

        {{ content }}

大概是以上这个样子。
利用指令，可以：

-   引入资源
-   格式化代码块
-   运行 Python 代码或借用进程间通信机制调用其他代码，并将结果嵌入输出中
-   ……

图像
----

插入图像可以使用 `image` 或 `figure` 指令。

image 属于直接插入图片用的，而 figure 则可以添加更详细的描述。

image 接受一个参数：图像的 Uri，如果是相对路径，则起点是当前文档。
image 可接受零个或多个选项，可选的选项有：

height
    图像高度，可以使用 |a_rst| 支持的长度单位，见
    https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#length-units

width
    图像宽度，同上。

scale
    图像缩放，使用百分比。

align
    可以是以下值之一：*top*, *middle*, *bottom*, *left*, *center*, *right*，设置图像对齐方式。

target
    如果设置，需要传入一个超链接靶标。这会让图片可点击，点击后跳转到靶标。
    对于 HTML，是将 img 元素放在了 a 元素内部。

::

    .. image:: img/59498721_p0.jpg
        :height: 400px
        :width: 600px
        :scale: 50%
        :align: center
        :target: https://docutils.sourceforge.io/docs/ref/rst/directives.html#image

.. image:: img/59498721_p0.jpg
    :height: 400px
    :width: 600px
    :scale: 50%
    :align: center
    :target: https://docutils.sourceforge.io/docs/ref/rst/directives.html#image

figure 由 image 和一段标题（一个单行段落），以及可选的图例组成。
对于基于页的媒体（如PDF），在排版时，figure 可能会浮动到合适的地方。

figure 拥有 image 所有的选项，在以下几处有所不同：

align
    可传入 *left*, *center*, *right*。
    只能设置水平方向上的对齐方式。

figwidth
    设置图像宽度，这将影响图像标题和图例的折行方式，以确保它们的宽度不会超过这个值。
    但是这并不影响内嵌的图片宽度，图片的宽度需要用 width 选项设置::

        +---------------------------+
        |        figure             |
        |                           |
        |<------ figwidth --------->|
        |                           |
        |  +---------------------+  |
        |  |     image           |  |
        |  |                     |  |
        |  |<--- width --------->|  |
        |  +---------------------+  |
        |                           |
        |The figure's caption should|
        |wrap at this width.        |
        +---------------------------+

表格
----

除了网格式和简单式的表格之外，还可以使用 `list-table` 或 `csv-table` 来创建表格，
和前两种相比，后两种比较不美观，但是不需要做 "字符画" 了。

table
    table 指令的内容可以是任意表格，包括 grid table, simple table
    以及通过 list-table, csv-table 创建的表格。

    它的作用主要是为表格添加标题，以及设置一下各列的宽度。

    接受以下选项：

    widths
        可以是 *auto*, *grid* 或用一列整数（用逗号或空格分隔）设置各列的宽度（按字符数计算）。
        如果传入 auto 或 grid，则由后端来推测列宽。

    width
        表格整体的宽度。如果忽略，则由后端自动推测。

    align
        表格整体的对齐方式。*left*, *center*, *right*。

csv-table
    从 CSV 数据创建表格::

        .. csv-table:: Frozen Delights!
            :header: "Treat", "Quantity", "Description"
            :widths: 15, 10, 30

            "Albatross", 2.99, "On a stick!"
            "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
            crunchy, now would it?"
            "Gannet Ripple", 1.99, "On a stick!"

    以下选项可被识别：

    widths
        *auto* 或一组整数，设置列宽。默认每列一致。

    width
        整体的宽度。

    header-rows
        整数，表示接下来的 CSV 数据中前几行为表头。默认 0.

    header
        一列 CSV 内容，用作表头。将插入到 header-rows 所设定的行前面。

    stub-columns
        整数，表示 CSV 数据中左几列为存根。默认 0.

    file
        从文件系统读取 CSV 数据。

    url
        从网络地址读取 CSV 数据。

    encoding
        设置外部 CSV 数据的字符编码。默认和当前文档相同。

    delim
        分隔符，默认逗号 ``,``。

    quote
        括号，用来包括表格中的单元。默认双引号 ``"``。

    keepspace
        保留分隔符旁的空白。默认忽略。

    escape
        转义符号。默认是将需要转义的字符重复两遍::

            "He said, ""Hi!"", and go away."

    align
        水平对齐方式。

list-table
    用列表的形式来创建表格。
    列表的顶级项表示一行，次级项表示一行的各元素::

        .. list-table::

            *   -   表头1
                -   表头2
                -   表头3
            *   -   内容11
                -   内容12
                -   内容13
            *   -   内容21
                -   内容22
                -   内容23

    .. list-table::

        *   -   表头1
            -   表头2
            -   表头3
        *   -   内容11
            -   内容12
            -   内容13
        *   -   内容21
            -   内容22
            -   内容23

    可接受 `widths`, `width`, `header-rows`, `stub-columns`, `align` 选项。

目录
----

`contents` 指令可以渲染出该篇文档的目录::

    .. contents::

.. contents::

可接受以下选项：

depth
    整数，设置目录层级深度，默认无限。

local
    如果提供，则会生成该章节以及子章节的目录而非全篇目录。

backlinks
    是否生成目录项和文档项之间的链接。

替换引用
--------

替换引用可以将一个指定的片段替换为另一个结构。

替换文本
    ::

        .. |a_rst| replace:: `restructuredtext <https://docutils.sourceforge.io/docs/>`__

        然后使用 |a_rst|，渲染时将被替换。

    然后使用 |a_rst|，渲染时将被替换。

Unicode
    ::

        .. |c| unicode:: 0xa9

        这是版权符号 |c|，Unicode 码点是 169，用十六进制表达就是 0xa9。

    .. |c| unicode:: 0xa9

    这是版权符号 |c|，Unicode 码点是 169，用十六进制表达就是 0xa9。

    可以使用三个选项：

    ltrim, rtrim, trim
        是否移除左、右、两侧的空白字符。

时间日期
    ::

        .. |date| date::

        .. |time| date:: %H:%M:%S

        将会渲染为编译文档时的时间日期，可以用 Python 标准库 time 中 strftime 相同的
        格式化字符串设置渲染格式。
        默认是当前日期 |date|，可以用 ``%H:%M:%S`` 渲染为当前时间 |time|。

    .. |date| date::

    .. |time| date:: %H:%M:%S

    将会渲染为编译文档时的时间日期，可以用 Python 标准库 time 中 strftime 相同的
    格式化字符串设置渲染格式。
    默认是当前日期 |date|，可以用 ``%H:%M:%S`` 渲染为当前时间 |time|。

警告
----

|a_rst| 提供了一些警告指令，如

-   attention
-   caution
-   danger
-   error
-   hint
-   important
-   note
-   tip
-   warning

用来将传入的体元素表达为指定的语义。::

    .. warning::

        毫无营养的随便写写是没有意义的！

.. warning::

    毫无营养的随便写写是没有意义的！

比较通用的是 `admonition` 指令，上述指令其实是它的子类。::

    .. admonition:: 标题
        :class: 类型，用于决定渲染样式

    .. admonition:: 你瞅啥？
        :class: dongbei warning

        瞅你咋地？

.. admonition:: 你瞅啥？
    :class: dongbei warning

    瞅你咋地？

导入
----

可以将外部文档导入进来，使用 `include` 指令。

将外部文档作为 |a_rst| 导入，使用相同的渲染方式::

    .. include:: path/to/document.rst

相对路径的起点是当前文档所在的文件夹。可接受以下选项：

start-line
    整数，从文件的第几行开始读取。
    和 Python 一样，第一行的索引值是 0 。

end-line
    整数，到文件的第几行结束。
    第一行零。

start-after
    字符串，将从文件中第一次找到的指定字符串后开始读取。

end-before
    字符串，将在文件中第一次找到的指定字符串前结束。

encoding
    字符编码。

literal
    是否以纯文本字面量的形式导入。

code
    输入 Pygments 支持的分词器名，以指定语言的词法规则将导入内容格式化。

number-lines
    整数。设置第一样的行号。仅在 literal 或 code 选项被设置时工作。

tab-width
    整数。设置制表符所渲染的空格的数目。仅在 literal 或 code 选项被设置时工作。

原始输入
--------

`raw` 指令将其内容在指定的输出格式下原样传递给输出::

    .. raw:: html

        <hr width=50 size=10>

可选参数：

file
    从文件系统中读取内容。

url
    从网络读取内容。

encoding
    外部内容的字符编码。

类
--

`class` 指令用于声明其内容或接下来的内容的类型。
对于 HTML 输出而言，这会在其内容的 class 属性中添加指定的名称。

::

    .. class:: special

    一个『特殊的』段落。

    .. class:: exceptional remarkable

    一个『例外』的章节
    ==================

    这是个普通段落。

    .. class:: multiple

        如果要传递内容，那么需要是体元素。
        比如一个或多个段落。

        这是第二段。

上面的渲染效果用一段伪 XML 来表示::

    <paragraph classes="special">
        一个『特殊的』段落。
    <section classes="exceptional remarkable">
        <title>
            一个『例外』的章节
        <paragraph>
            这是个普通段落。
        <paragraph classes="multiple">
            如果要传递内容，那么需要是体元素。比如一个或多个段落。
        <paragraph classes="multiple">
            这是第二段。

配置角色
--------

可以使用 `role` 来创建一个新的角色，使用 `default-role` 来配置 `解释性文本角色`_ 的默认含义。

::

    .. role:: custom

    An example of using :custom:`interpreted text`.

定义必须在使用的前面。
可以用一个括号来表达继承关系（类似 Python 的 class）::

    .. role:: custom(strong)

    :custom:`强调`。

特殊的例子是 `raw` 角色，它必须继承后使用::

    .. role:: raw-html(raw)
        :format: html

    :raw-html:`<br>`

::

    .. default-role:: math

    会将之后的默认角色设置为 math，例如 `\LaTeX` 和 :math:`\LaTeX` 是一样的含义了。

对任何指令都同样的选项
----------------------

任何指令都可设置 class 和 name 选项，前者效果与 `类`_ 相同，
后者会将该结构设置成一个可超链接的锚点::

    .. image:: bild.png
        :name: my picture

    在文章中可以使用 `my picture`_ 来链接至上面的图片。
    它的效果和

    .. _my picture:

    .. image:: bild.png

    是一样的。

常用角色
========

在 `内联标记`_ 章节已经介绍了一部分，接下来是

doc
    这会创建一个引向项目中其他
