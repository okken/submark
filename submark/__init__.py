"""
A Subset of Markdown

Use it like this:
submark something.md > something.html

or:
cat something.html | submark > something.html

or:
$ echo '**hi**' | submark
<strong>hi</strong>
"""

__version__ = "0.6"

from .submark import convert  # noqa
from .cli import main  # noqa
