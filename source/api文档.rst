#########################
使用 Sphinx 书写 API 文档
#########################

程序中有哪些结构? 变量,函数,类 ...... 等等. 在 Sphinx 中定义了相应的指令或角色来描述它们, 并且, 也可以写进源代码的 docstring 中, 让 ``sphinx-apidoc`` 自动生成.

此文参考官方文档 http://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html .

.. highlight:: rst

函数
====

.. function:: getDate(time, mode="YYYY-MM-DD hh:mm:ss")

    解析传入的时间, 得到一个可读的时间字符串.

    :param int time: 从 1970 至今的秒数
    :param mode: 解析模式
    :type mode: str

    :return: 表示时间的字符串 ``YYYY-MM-DD hh:mm:ss``
    :rtype: str

    :raise ValueError: 不能传入一个负值
    :var test: 一个无关的测试量

使用 ``function`` 描述一个函数::

    .. function:: getDate(time, mode)

        解析传入的时间, 得到一个可读的时间字符串.

        :param int time: 从 1970 至今的秒数
        :param mode: 解析模式
        :type mode: str

        :return: 表示时间的字符串 ``YYYY-MM-DD hh:mm:ss``
        :rtype: str

        :raise ValueError: 不能传入一个负值
        :var test: 一个无关的测试量

- ``function`` 指令后书写函数原型, 应当处于同一行中.
- ``:param xxx:`` 描述一个参数的名称 ``xxx``.
- ``:type xxx:`` 描述参数 ``xxx`` 的类型.
- ``:param type name:`` 同时描述一个参数的类型与名称.
- ``:return:`` 描述返回值.
- ``:rtype:`` 描述返回值的类型.
- ``:raise xxx:`` 描述抛出的异常.
- ``:var yyy:`` 描述用到的一个变量.

并且可以通过 :func:`getDate` 来创建一个指向该函数的链接::

    并且可以用过 :func:`getDate` 来创建一个指向该函数的链接

类
====

.. class:: Clock(speed=0.0)

    .. method:: gamma()

        求解 :math:`\gamma` 因子

        .. math:: \gamma = \frac{1}{ \sqrt{ 1 - \frac{v^2}{c^2} } }

        :return: gamma
        :rtype: float

    .. method:: speed(v)

        设置该钟表相对观察者的速度.

        :param float v: 速度, 单位 m/s

    .. attribute:: position

        该物体相对观察者的位置 ``(float x, float y)``.

- 方法使用 ``method`` , 可接受的修饰和 `函数`_ 一致.
- 类/方法/属性, 可以使用 :class:`Clock`, :meth:`gamma`, :attr:`position` 来创建链接::

    .. class:: Clock(speed=0.0)

        .. method:: gamma()

            求解 :math:`\gamma` 因子

            .. math:: \gamma = \frac{1}{ \sqrt{ 1 - \frac{v^2}{c^2} } }

            :return: gamma
            :rtype: float

        .. method:: speed(v)

            设置该钟表相对观察者的速度.

            :param float v: 速度, 单位 m/s

        .. attribute:: position

            该物体相对观察者的位置 ``(float x, float y)``.

    类/方法/属性, 可以使用 :class:`Clock`, :meth:`gamma`, :attr:`position` 来创建链接

数据
====

用于解释程序中出现的一些重要数据, 比如全局变量/常量.

.. data:: NULL

    ``0``

并且, 使用 :data:`NULL` 来创建一个指向该块的链接::

    .. data:: NULL

        ``0``

    并且, 使用 :data:`NULL` 来创建一个指向该块的链接
