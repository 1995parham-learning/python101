def y(f):
    return lambda *args: f(y(f))(*args)


def factorial(combinator):
    def _factorial(n):
        if n:
            return n * combinator(n - 1)
        else:
            return 1

    return _factorial


print(y(factorial)(5))
