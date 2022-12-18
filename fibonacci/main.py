from collections import abc

__author__ = "Parham Alvani"


class Fibonacci(abc.Container):
    """
    A class for making fibonacci number with divide & conquer and
    dynamic programming methods.
    """

    def __init__(self):
        self.list: list[int] = [0, 1]

    def __contains__(self, fn: int) -> bool:
        while fn > self.list[-1]:
            self.list.append(self.list[-1] + self.list[-2])

        return fn in self.list

    def __getitem__(self, index: int) -> int:
        """
        returns fibonacci squence at the given index.
        if it does not have the given index, it will calculate it.
        """
        while len(self.list) - 1 < index:
            self.list.append(self.list[-1] + self.list[-2])
        return self.list[index]


fibonacci = Fibonacci()
var = input("Please enter fibonacci sequence number ")
var = int(var)
print(fibonacci[var])
print(var in fibonacci)

print(fibonacci.list)
