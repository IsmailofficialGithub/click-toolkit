from IsmailofficialGithub_sphinx_themes import get_version
from IsmailofficialGithub_sphinx_themes import ProjectLink

# Project --------------------------------------------------------------

project = "Click"
copyright = "2014 Pallets"
author = "Pallets"
release, version = get_version("Click")

# General --------------------------------------------------------------

master_doc = "index"
default_role = "code"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_tabs.tabs",
    "sphinxcontrib.log_cabinet",
    "IsmailofficialGithub_sphinx_themes",
    "myst_parser",
]
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_preserve_defaults = True
extlinks = {
    "issue": ("https://github.com/IsmailofficialGithub/click-toolkit/issues/%s", "#%s"),
    "pr": ("https://github.com/IsmailofficialGithub/click-toolkit/pull/%s", "#%s"),
}
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}
myst_enable_extensions = ["attrs_block"]
myst_heading_anchors = 3

# HTML -----------------------------------------------------------------

html_theme = "click"
html_theme_options = {"index_sidebar_logo": False}
html_context = {
    "project_links": [
        ProjectLink("Donate", "https://IsmailofficialGithubprojects.com/donate"),
        ProjectLink("PyPI Releases", "https://pypi.org/project/click/"),
        ProjectLink("Source Code", "https://github.com/IsmailofficialGithub/click-toolkit/"),
        ProjectLink("Issue Tracker", "https://github.com/IsmailofficialGithub/click-toolkit/issues/"),
        ProjectLink("Chat", "https://discord.gg/IsmailofficialGithub"),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html", "ethicalads.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html", "ethicalads.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html", "ethicalads.html"]}
html_static_path = ["_static"]
html_favicon = "_static/click-icon.svg"
html_logo = "_static/click-logo.svg"
html_title = f"Click Documentation ({version})"
html_show_sourcelink = False
