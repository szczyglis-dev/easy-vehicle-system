"""Sphinx configuration for the Easy Vehicle System manual."""
project = 'Easy Vehicle System'
author = 'Marcin Szczygliński'
copyright = '2026, Marcin Szczygliński'
version = '1.0'
release = '1.0.0'
language = 'en'
root_doc = 'index'
source_suffix = {'.rst': 'restructuredtext'}
extensions = ['sphinx_rtd_theme']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_title = 'Easy Vehicle System 1.0.0'
html_theme_options = {'navigation_depth': 3, 'collapse_navigation': True}
html_show_sourcelink = False
html_context = {
    'display_github': True,
    'github_user': 'szczyglis-dev',
    'github_repo': 'easy-vehicle-system',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}
numfig = False
