import datetime
import math
import typing


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def angle(self):
        return math.atan2(self.y, self.x)

    def __abs__(self):
        # the length of hypotenuse
        return math.hypot(self.x, self.y)

    def __iter__(self) -> typing.Iterator[float]:
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, self.x, self.y)

    def __str__(self) -> str:
        return str(tuple(self))

    def __format__(self, format_spec: str = "") -> str:
        if format_spec.endswith("pd"):
            format_spec = format_spec[:-2]
            cords = (abs(self), math.degrees(self.angle()))
            fmt = "<{}, {}>"
        elif format_spec.endswith("p"):
            format_spec = format_spec[:-1]
            cords = (abs(self), self.angle())
            fmt = "<{}, {}>"
        else:
            cords = (self.x, self.y)
            fmt = "({}, {})"
        components = (format(c, format_spec) for c in cords)
        return fmt.format(*components)


print(f"today {datetime.datetime.now():'%a %-d %b %Y - %H:%M'}")
print(
    "and we are here only to lean format "
    "(f-string, built-in format() and str.format()) in pytyon"
)

origin = Vector2D(0, 0)
destination = Vector2D(2, 2)
polar_bear = Vector2D(4, 4)

print(f"origin: {origin:.4f} using %.4f")
print(f"origin: {origin:g} using %g")
print(f"dest: {destination:.3e} using %.3e")
print(f"polar_bear: {polar_bear:.4fp} using %.4fp!")
print(f"polar_bear: {polar_bear:.4fpd} using %.4fpd!")
