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
