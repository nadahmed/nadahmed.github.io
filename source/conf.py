import datetime

project = "Noor Al Din Ahmed — Portfolio"
copyright = f"{datetime.date.today().year}, Noor Al Din Ahmed"
author = "Noor Al Din Ahmed"
release = "0.1.0"

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_copybutton",
    'sphinx.ext.intersphinx',
    'sphinxcontrib.youtube'
]

templates_path = ["_templates"]
exclude_patterns = []

html_permalinks_icon = '<span>#</span>'
html_theme = "sphinxawesome_theme"
html_static_path = ["_static"]
html_title = "Noor Al Din Ahmed — Portfolio"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

todo_include_todos = True
