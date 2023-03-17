from functools import singledispatch
import html


@singledispatch
def htmlize(obj: object) -> str:
    return f"<pre>{html.escape(repr(obj))}</pre>"


@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace("\n", "<br />\n")
    return f"<p>{content}</p>"


if __name__ == "__main__":
    print(htmlize("Hello\nElahe"))
    print(htmlize(12))
    print(htmlize(max))
