"""
提供 GitHub 链接，我们提供了基于段落的卡片样式的

.. github:: owner/repo

和内联样式的 :github:`owner/repo`。
"""
from docutils.parsers.rst import Directive
from docutils.parsers.rst import nodes
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner


class Null:
    pass


try:
    # 引入 Sphinx 类，为 vscode 提供智能提示
    from sphinx.application import Sphinx
except ImportError:
    Sphinx = Null

try:
    # nikola 需要使用 RestExtension 来加载插件
    from nikola.plugin_categories import RestExtension
except ImportError:
    RestExtension = Null


def setup(app: Sphinx):
    """Sphinx 加载函数，可以不引入 docutils 来加载，因为 Sphinx 本身提供了部分渲染功能"""
    app.add_directive("github", GitHubCard)
    app.add_role("github", github_role)


# nikola 加载类
if RestExtension:
    from docutils.parsers.rst.roles import register_canonical_role
    from docutils.parsers.rst.directives import register_directive

    class Plugin(RestExtension):
        """nikola 需要将插件加载到 docutils 中，因为内容生成完全依赖 docutils。
        """
        name = "rest_github"

        def set_site(self, site):
            self.site = site
            register_canonical_role("github", github_role)
            register_directive("github", GitHubCard)
            return super(Plugin, self).set_site(site)


def github_role(name: str, rawtext: str, text: str, lineno: int, inliner: Inliner, options={}, content=[]):
    """格式化为链接
    """
    # 判断是仓库还是用户
    title = f"Github - {text}" if "/" in text else f"{text}@GitHub"
    url = f"https://github.com/{text}"
    # 返回一个超链接结点
    return [nodes.reference(rawsource=rawtext, text=title, refuri=url)], []


class GitHubCard(Directive):

    def run(self):
        pass
