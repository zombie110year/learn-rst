########
rst 指令
########

指令语法如下::

    +-------+-------------------------------+
    | ".. " | 指令 "::" 主参数              |
    +-------+    :额外参数:                 |
            |                               |
            |    内容                       |
            +-------------------------------+

目录
====

::

    .. toctree::
        :maxdepth: para
        :caption: para
        :numbered:
        :titlesonly:
        :glob:
        :reversed:
        :hidden:
        :includehidden:

- ``:maxdepth: para`` 接受一个参数, 应该为数字, 设置目录树展开的深度.
- ``:caption: para`` 接受一个参数, 为任意字符串, 设置该目录树的标题.
- ``:numbered:`` 为目录自动编号
- ``:titlesonly:`` 只生成文件的一级标题, 不展开子标题. 会覆盖 ``:maxdepth:``
- ``:glob:`` 启用通配符
- ``:reversed:`` 启用通配符时, 反转目录排序.
- ``:hidden:`` 只显示标题, 而不创建超链接.
- ``:includehidden:`` 只创建一级标题的超链接.

警告
====

警告将会显示为特殊的样式. 在 主参数和内容 位置处, 可以编写段落. 这个指令的所有参数都是被显示的内容.

.. danger:: 危险!

    这是一个危险操作.

::

    .. danger:: 危险!

        这是一个危险操作.

.. tip:: 提示

    提示条目

::

    .. tip:: 提示

        提示条目

.. caution:: 小心

    小心, 注意安全

::

    .. caution:: 小心

        小心, 注意安全

.. note:: 注意

    集中注意力

::

    .. note:: 注意

        集中注意力

.. warning:: 警告

    警告条目

::

    .. warning:: 警告

        警告条目

.. important:: 重要

    重要内容

::

    .. important:: 重要

        重要内容

.. seealso::

    参见某某某

::

    .. seealso::

        参见某某某

版本更新
========

.. versionadded:: 0.0.1
    添加了一些内容

::

    .. versionadded:: 0.0.1
        添加了一些内容

.. versionchanged:: 0.0.1
    修改了一些内容

::

    .. versionchanged:: 0.0.1
        修改了一些内容

.. deprecated:: 0.0.1
    某些功能被删除, 使用 某某 代替

::

    .. deprecated:: 0.0.1
        某某 被删除, 使用 某某 代替

文本样式
========

.. rubric:: 一个标题, 但是不计入 toctree

::

    .. rubric:: 一个标题, 但是不计入 toctree

.. centered:: 居中的文本

::

    .. centered:: 居中的文本

.. hlist::
    :columns: 4

    - 1
    - 2
    - 3
    - 4
    - 5
    - 6
    - 7

::

    .. hlist::
        :columns: 4

        - 1
        - 2
        - 3
        - 4
        - 5
        - 6
        - 7

图片
====

处理图片可能用到两个指令: ``image`` 和 ``figure``.

image
-----

.. image:: img/59498721_p0.jpg
    :alt: 响爷
    :height: 100px

::

    .. image:: path/to/image
        :alt: xxx
        :height: xxx
        :width: xxx
        :scale: xxx
        :align: top | middle | bottom | left | center | right
        :target: path/to/target

- ``alt`` : 文本.
    替换文本: 当应用无法显示图片时, 会显示图片的一个简短的描述或由应用为视觉受损的用户读出.
- ``height`` : 高度. 当高度与宽度只指定一个时, 会按照比例不变的原则进行缩放.
- ``width`` : 宽度.
- ``scale`` : 缩放率.
- ``align`` : "top | middle | bottom | left | center | right" 6 选 1.
    图片的对齐方式, 与 CSS 一致.
- ``target`` : 超链接(URI或引用名称)
    将图片变为超链接引用(可点击), 可选参数是一个URI(相对或绝对), 或一个包含下划线前缀的 "引用名称".

figure
------

一个 ``figure`` 可以理解为 "画布", 在其上可以嵌入其他 rst 结构, 包括 ``image``.

.. figure:: img/59498721_p0.jpg

    这是 figure 的标题, 嵌入其他结构时需保证缩进.

    +-----------------------------------------+
    | 这里随便嵌入了一个列表                  |
    +-----------------------------------------+

::

    .. figure:: img/59498721_p0.jpg

        这是 figure 的标题, 嵌入其他结构时需保证缩进.

        +-----------------------------------------+
        | 这里随便嵌入了一个列表                  |
        +-----------------------------------------+

``figure`` 接受的参数和 image 相同.

代码
====

代码块
------

.. code-block:: c
    :linenos:

    int main()
    {
        return 0;
    }

接受的参数

- ``:linenos:`` 为代码块生成行号.
- ``:linenothreshold: n`` 超过 n 行的代码块才会标注行号.
- ``:lineno-start: n`` 为代码块生成行号, 并且从 n 开始.
- ``:emphasize-lines: m,n,...`` 着重显示 m,n 等行. 行选择可以使用 ``m-n`` 来选择连续的行.
- ``:caption:`` 为该代码块命名.
- ``:dedent: n`` 调整代码缩进, 减少 n 个空格.

引用外部代码
------------

"引用外部代码" 衍生自 ``include`` 指令, 将外部的代码文件内容嵌入文本.

.. literalinclude:: code/example.py
    :language: python

::

    .. literalinclude:: path/to/file
        :language: codelanguage

接受的参数

允许使用 ``code-block`` 的参数, 除此之外可能需要指定文件字符编码. 并且, ``code-block`` 中高亮模式在主参数指定, 而 ``literalinclude`` 需要 ``:language:`` 参数.

- ``:language: example`` 指定高亮模式.
- ``:encoding: gbk`` 指定 gbk 文本编码.
- ``:lines: m,n,a-b,...`` 只嵌入指定行.
- ``:linenos:`` 为代码块生成行号.
- ``:lineno-start: n`` 为代码块生成行号, 并且从 n 开始.
- ``:emphasize-lines: m,n,...`` 着重显示 m,n 等行. 行选择可以使用 ``m-n`` 来选择连续的行.
- ``:caption:`` 为该行代码块命名.
- ``:dedent: n`` 调整代码缩进, 减少 n 个空格.

如果 目标文件是一个 Python 模块, 还可以从 Python 语义结构上引入指定结构::

    .. literalinclude:: code/example.py
        :pyobject: add

.. literalinclude:: code/example.py
    :pyobject: add

还可以与另一个文件做对比::

    .. literalinclude:: code/example.py
        :diff: code/example_diff.py

.. literalinclude:: code/example.py
    :diff: code/example_diff.py

数学环境
========

使用 LaTeX 语法. ``math`` 指令将创建一个段落级别的数学环境, 要在行内使用, 需要用 ``math`` 角色. math 指令唯一的参数就是 LaTeX 语句, 不管它是在主参数位置还是在内容位置, 并且, 没有其他参数.

::

    .. math:: \frac{\partial y}{\partial x} = x

    .. math::

        \begin{bmatrix}
            1 & 2 \\
            3 & 4 \\
        \end{bmatrix}

.. math:: \frac{\partial y}{\partial x} = x

.. math::

    \begin{bmatrix}
        1 & 2 \\
        3 & 4 \\
    \end{bmatrix}

table
-----

table 指令用于生成表格. 实际上, 在用格式符编辑列表时就隐式地使用了该指令. 而显式地使用 table 指令, 可以附加额外的属性.

::

    .. table:: 列表的标题
        :widths: auto
        :align: center

- ``:width:`` 各列的宽度, 用逗号分隔, 或者使用 "auto", "grid" 参数.
- ``:align:`` 整个列表在页面中的对齐方式, 可选 "left", "center", "right".

注意, 编辑的表格仍然需要遵守语法, 而且, 和 ``.. table`` 指令需要有一个单位的缩进.

其他指令
========

include
-------

``include`` 将会把另一个文件嵌入当前文本. 和 ``literalinclude`` 不同, ``include`` 嵌入的不一定是纯文本. 如果嵌入 rst 文件, 那么对应的文字也会被渲染.

::

    .. include:: path/to/file
        :start-line: a  # 从第 a 行开始
        :end-line: b    # 到第 b 行结束
        :start-after: string    # 从这个 string 在目标文本中第一次出现时开始.
        :end-before: string     # 到这个 string 在目标文本中第一次出现时结束.
        :literal:       # 作为纯文本插入, 等同于 literalinclude
        :code: type     # 作为源代码插入, 等同于 literalinclude 设置相应语言模式
        :number-lines: n        # 从 n 开始编号, 默认从 1 开始
        :encoding: utf-8        # 设置字符编码
        :tab-width: 4           # 设置制表符宽度为 4

glossary
--------
