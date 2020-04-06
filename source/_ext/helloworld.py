from docutils import nodes
from docutils.parsers.rst import Directive
from time import localtime, strftime
# 提供智能提示
from sphinx.application import Sphinx


class HelloWorld(Directive):
    def run(self):
        datetime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        paragraph = f"Hello World! {datetime}"
        return [nodes.paragraph(text=paragraph)]


def setup(app: Sphinx):
    """Sphinx 使用的加载函数

    :param app: Sphinx 应用
    :type app: sphinx.application.Sphinx
    :returns: 该扩展的配置信息
    """
    app.add_directive("helloworld", HelloWorld)
    return {
        'version': '0.1',
        # 允许并行读取
        'parallel_read_safe': True,
        # 允许并行写入
        'parallel_write_safe': True,
    }
