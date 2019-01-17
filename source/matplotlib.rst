##########
matplotlib
##########

语法
====

提供了 ``plot`` 等指令.

plot
----

见 https://matplotlib.org/devel/plot_directive.html

``plot`` 可以包含一个编写 matplotlib 作图的 Python 代码, 并将其渲染为图形. 同样也可以在下方一个缩进单位的区块中直接编写代码::

    .. plot:: _code/sinx.py
        :include-source:

        添加一些描述(可选的)

    .. plot::

        import matplotlib.pyplot as plt
        import numpy as np

        x = np.linspace(-6, 6, 1000)
        y = np.sin(x)
        plt.plot(x, y)
        plt.title("sin(x)")

        # 最后必须要调用 show 方法, 才能显示
        plt.show()

.. plot:: code/cosx.py
    :include-source:

    添加一些描述(可选的)

.. plot::

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(-6, 6, 1000)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title("sin(x)")

    # 最后必须要调用 show 方法, 才能显示
    plt.show()

默认会生成 png, big png, pdf 三种格式的图片.

- 可以给 ``plot`` 指令使用参数 ``:include-source:`` 将源代码插入到图片上方.

配置
====

需要在conf.py 文件的 extension 列表中添加项目 ``'matplotlib.sphinxext.plot_directive'`` 项目, 以启用 ``plot`` 指令.

其他可设置项:

``plot_pre_code``
-----------------

.. highlight:: python

在每幅图的代码中都会首先执行的代码, 设置后将不需要在代码中重复书写::

    plot_pre_code = """
    import numpy as np
    import matplotlib.pyplot as plt
    """

``plot_include_source``
-----------------------

设置每幅图的 ``:include-source:`` 选项的默认值::

    plot_include_source = False

``plot_basedir``
----------------

生成图像的默认储存位置, 默认为代码文件所在目录::

    plot_basedir = 'img/'