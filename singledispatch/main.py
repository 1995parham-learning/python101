from functools import singledispatch
from collections import abc
import html
import numbers


@singledispatch
def htmlize(obj: object) -> str:
    return f"<pre>{html.escape(repr(obj))}</pre>"


@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace("\n", "<br />\n")
    return f"<p>{content}</p>"


@htmlize.register
def _(seq: abc.Sequence):
    inner = "</li>\n\t<li>".join(htmlize(item) for item in seq)
    return "<ul>\n\t<li>" + inner + "</li>\n</ul>"


@htmlize.register
def _(n: numbers.Integral):
    return f"<pre>{n} (0x{n:x})</pre>"


if __name__ == "__main__":
    print(htmlize("Hello\nElahe"))
    print(htmlize([1, 2, 3]))
    print(htmlize(12))
    print(htmlize(max))
