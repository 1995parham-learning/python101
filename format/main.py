import datetime
import typing


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __iter__(self) -> typing.Iterator[float]:
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, self.x, self.y)

    def __str__(self) -> str:
        return str(tuple(self))

    def __format__(self, format_spec: str = "") -> str:
        components = (format(c, format_spec) for c in self)
        return "({}, {})".format(*components)


print(f"today {datetime.datetime.now():'%a %-d %b %Y - %H:%M'}")
print(
    "and we are here only to lean format "
    "(f-string, built-in format() and str.format()) in pytyon"
)

origin = Vector2D(0, 0)
destination = Vector2D(2, 2)

print(f"origin: {origin:.4f} using %.4f")
print(f"origin: {origin:g} using %g")
print(f"dest: {destination:.3e} using %.3e")
