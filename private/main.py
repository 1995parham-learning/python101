class Vector2D:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y


v1 = Vector2D(3, 4)
# The following lines wants to print x property from Vector2D which is private.
# The first line seems okay but it is not working because of name mangling.
# print(v1.__x)
# print(v1._Vector2D__x)
