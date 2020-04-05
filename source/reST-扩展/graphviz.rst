########
graphviz
########

见 https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html

.. highlight:: rst

语法
====

可以使用指令::

    .. graphviz:: /code/example.gv

来包含一个用 graphviz 语法编辑的文件, 将在构建时渲染为图片.

.. graphviz:: /code/example.gv

或者用同样的指令::

    .. graphviz::

        digraph foo {
            "bar" -> "baz";
        }

.. graphviz::

    digraph foo {
        "bar" -> "baz";
    }

或者用子指令, 分别生成有向图与无向图::

    .. digraph:: 名字

        foo -> bar;

    .. graph:: 另一个名字

        foo -- bar;

.. digraph:: 名字

    foo -> bar;

.. graph:: 另一个名字

    foo -- bar;

配置
====

在 ``conf.py`` 中的 ``extensions`` 列表中添加项目 ``"sphinx.ext.graphviz"`` 以启用本插件.

- ``graphviz_dot`` 设置渲染器路径, 默认为 ``dot``, 如果下载安装的 graphviz 套件未添加进 PATH, 那么需要完整的绝对路径.
- ``graphviz_dot_args`` 传递给渲染器的命令行参数, 应该为一个列表, 类似于 :data:`sys.argv`, 或者说 :mod:`argparse` 所解析的格式. 默认为空列表 ``[]``.
- ``graphviz_output_format`` 设置构建 HTML 时的输出格式, 默认为 ``'png'``, 必须在 ``'png'`` 或 ``'svg'`` 中二选一. 如果选择了 svg, 那么为了使图片超链接正常工作, 需要在代码中指定相关的 HTML 属性::

    .. graphviz::

        digraph example {
            a [label="sphinx", href="http://sphinx-doc.org", target="_top"];
            b [label="other"];
            a -> b;
        }
