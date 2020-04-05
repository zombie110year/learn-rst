################################
欢迎来到 reStructureText 的世界!
################################

什么是 |a_rst|？ |a_rst| 是一种基于 Python 的 docutils 模块提供解析功能的标记语言。
它具有以下特点：

简洁
    解析前的纯文本仍具有良好可读性。

强大
    强大的 role、directive 以及扩展系统可以极大地增强表达能力。

统一
    不论是任何平台，其解析功能都统一在 docutils 模块下。

相比流传广泛的 Markdown，|a_rst| 具有更好的表达能力、扩展能力以及稳定性。
Markdown 根据其扩展标准、具体实现、使用环境的不同，有多个社区提供了不同的 Markdown 支持。
在具有丰富生态的同时，也陷入了生态分裂的窘境。

由于使用 Markdown 不可避免的表现力不足的缺点，各个实现往不同的方向寻找扩展方法。
有的 Markdown 使用 `{% parameters %}` 形式的 *shortcode* 来提供扩展，如 markdown-it；
有的 Markdown 将额外的功能写入解析器，如最为强大的 pandoc；
有的 Markdown 试图添加新的语法，例如 latex 风格的指令。

但它们的生态是分裂的，在前者提供的扩展，后者可能未提供，或者以另一种形式提供，
导致文档难以迁移。

而 |a_rst| 在这一方面拥有巨大的优势：它以及提供了一个完善的扩展开发环境。
任何表达都可以通过统一的 role 或 directive API 来实现！

|a_rst| 可用于：

-   文档生成工具 `Sphinx <https://www.sphinx-doc.org/>`__
-   静态站点生成器 `Nikola <https://getnikola.com/>`__
-   静态博客系统 `Pelican <https://blog.getpelican.com/>`__

以及任何 docutils 能去到的地方。

.. toctree::
    :maxdepth: 2
    :numbered:
    :caption: 本书目录：

    reST-入门
    reST-标记规范
    reST-角色
    reST-指令
    reST-扩展/index
    nikola
    sphinx

目录与表格
==========

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
