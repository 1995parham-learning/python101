import weakref

s = {"Hello"}


def bye():
    print("the object, left us alone")


ender = weakref.finalize(s, bye)

del s
