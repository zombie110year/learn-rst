##################
|a_rst| 自定义扩展
##################

|a_rst| 提供了基于 docutils 模块的扩展支持能力。
扩展以 Python 代码编写，以新的指令或角色的形式提供。
由于 Python 的能力，还可以调用外部程序对内容进行处理。

在编写扩展之前，建议先掌握加载扩展的方法，这里提供一份 HelloWorld 扩展的代码，
作用是提供 `helloworld` 指令，将该指令转换为形如 `Hello World! {{ 时间日期 }}` 的段落：

.. literalinclude:: /_ext/helloworld.py
    :name: ext_helloworld
    :language: python
    :lines: 1-3,8-12
    :linenos:

本文提供了 `Sphinx <Sphinx 加载扩展>`_ 的扩展加载方式和 `Nikola <Nikola 加载插件>`_ 加载插件的方式。
请在阅读这两个章节之一并成功运行上面的例子后，阅读后续的 `编写扩展`_ 章节。

Sphinx 加载扩展
===============

Sphinx 的扩展可以通过预安装的包的形式来加载，也可以放置在当前项目的 *source/_ext* 目录下，
*_ext* 目录名前的下划线是告诉模板引擎此文件夹内容不渲染，也可以将此文件夹任意取名，我们将在
*source/conf.py* 中配置它。

在 *source/conf.py* 中，通过 Python 的功能将扩展所在的文件夹加载到路径中，然后配置 `extensions` 变量，
在列表中添加模块名：

.. code:: python

    # ...
    import sys
    from pathlib import Path
    sys.path.insert(0, Path("_ext").absolute().as_posix())
    # ...
    extensions = [
        "helloworld"
    ]

为了让 Sphinx 加载此扩展，你需要在上面提供的功能代码 `ext_helloworld`_ 的基础上再添加一个 `setup` 函数：

.. literalinclude:: /_ext/helloworld.py
    :language: python
    :emphasize-lines: 15-29
    :linenos:

::

    .. helloworld::

.. helloworld::

Nikola 加载插件
===============

编写扩展
========

扩展的两种形式：Directive 和 Role。
前者是 :class:`docutils.parsers.rst.Directive` 实例，后者可以通过一个函数来加载。

创建一个角色
------------

我们先了解一下角色的创建方式，可以参考官方文档创建 |a_rst| 解释性文本角色
https://docutils.sourceforge.io/docs/howto/rst-roles.html
。

一个角色是一个函数：

.. function:: role_function(name, rawtext, text, lineno, inliner, options={}, content=[])

    :param str name: 该角色的名称
    :param str rawtext: 包含该角色完整标记的纯文本，常用来在发生错误时通过 problematic 结点来抛出错误信息。
    :param str text: 该角色的内容
    :param int lineno: 该角色在源文件中所处的行数
    :param inliner: 调用该函数的 :class:`docutils.parsers.rst.states.Inliner` 对象，
        提供报告错误和访问文档树的一些有用的属性。
    :param options: 通过 role 指令创建的角色会传入此参数，是 role 指令设置的选项和它们的值。
    :type options: Dict[str, str]
    :param content: 通过 role 指令创建的角色会传入此参数，是 role 指令的内容。
        TODO:（截至 2012 年官方文档撰写时，没有角色会使用此参数)
    :type content: List[str]
    :returns: 一个元组，包含两个元素：

        1. 一组结点，将被插入到文档树中角色出现的位置。
        2. 一组系统信息，将被插入到文档数中角色出现的块的后一个块中。

        它们都可以是空列表。
    :rtype: Tuple[List[nodes], List[messages]]

以下面的角色为例::

    :github:`zombie110year/learn-rst`

当调用时，各参数的值将是

name
    `github`
rawtext
    ::

        :github:`zombie110year/learn-rst`
text
    `zombie110year/learn-rst`
lineno
    看情况，从 0 开始。

对于一个标准的角色，需要用 `register_canonical_role` 将其注册进 docutils 的解析器中：

.. code:: python

    docutils.parsers.rst.roles.register_canonical_role("github", github_role)

如果该角色是与所使用的应用程序相关的，则需要使用 `register_local_role` 函数来注册：

.. code:: python

    from docutils.parsers.rst import roles
    roles.register_local_role(name, role_function)

另外还提供一个 `register_generic_role` 的注册函数，这个函数是为了便于将那些只是将文本处理为某个结点
的角色注册的，这样的角色没有其他功能：

.. code:: python

    from docutils.parsers.rst import roles, nodes
    roles.register_generic_role("emphasize", nodes.emphasis)

对于我们的 `github` 角色 :github:`zombie110year/learn-rst` 来说，我们的目的就是将它转换成
链接到 GitHub 仓库的链接，那么就可以这么编写：

.. literalinclude:: /_ext/github.py
    :language: python
    :lines: 9-11,54-61

这个功能将会判断我们提供的是一个仓库的名称还是一个用户的名称，
并且格式化为不同的显示名。例如::

    本仓库为 :github:`zombie110year/learn-rst`，
    它的创建者是 :github:`zombie110year`。

本仓库为 :github:`zombie110year/learn-rst`，
它的创建者是 :github:`zombie110year`。
