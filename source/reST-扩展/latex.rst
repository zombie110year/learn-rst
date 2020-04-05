使用 Sphinx 生成 LaTeX 文件 (最终得到 PDF)
##########################################

在 LaTeX 设置中, 设置以下参数::

    latex_engine = "xelatex"
    latex_elements = {
        'papersize': 'a4paper',
        'utf8extra': '',
        'inputenc': '',
        'cmappkg': '',
        'fontenc': '',
        'preamble': r'''
            \usepackage{xeCJK}
            \parindent 2em
            \setcounter{tocdepth}{3}
            \renewcommand\familydefault{\ttdefault}
            \renewcommand\CJKfamilydefault{\CJKrmdefault}
        ''',
    }

就能获得良好的 TeX 代码输出, 进入到 ``build/latex`` 目录下 ``make``, 就能自动调用 xelatex 编译 PDF 了

注意, make 文件中, 查找的 LaTeX 文件与这个设置有关::

    # Grouping the document tree into LaTeX files. List of tuples
    # (source start file, target name, title,
    #  author, documentclass [howto, manual, or own class]).
    latex_documents = [
        (master_doc, 文件名, 封面标题,
        author, 'manual'),
    ]

在文件名中, 最好不要有非 ASCII 字符, xelatex 恐怕无法找到含还有中文字符的文件名.

默认情况下, 生成的 PDF 是双页打印模式的, 在电脑上浏览会发现有很多空白, 这是那些左侧有文字, 右侧没有内容, 且下面的内容在下一个章节的情况下, 会留空.

要设置这一点, 在 ``latex_elements`` 中添加一项

.. code-block:: python
    :emphasize-lines: 2

    latex_elements = {
        'extraclassoptions': 'openany,oneside',
    }

那么, 就会按照单页样式打印.