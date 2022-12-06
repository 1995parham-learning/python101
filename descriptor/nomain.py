"""
another implementation for what we have in main.py.
without any descriptor
"""
from __future__ import annotations
import abc


class Alg(abc.ABC):
    """
    Abstract implementation of Alg algorithm.
    This algorithm required core to work and you can
    use it as an instance attribute.
    """

    def __init__(self, core: Core):
        if not isinstance(core, Core):
            raise ValueError()
        self.core = core

    def __call__(self):
        return self.run()

    @abc.abstractmethod
    def run(self):
        pass


class Alg1(Alg):
    """
    First implementation of the Alg algorithm.
    """

    def run(self):
        return f"Alg-1 from {self.core.name}"


class Alg2(Alg):
    """
    Second implementation of the Alg algorithm.
    """

    def run(self):
        return f"Alg-2 from {self.core.name}"


class Core:
    """
    Core uses Alg algorithm and we wnat to control its implementation
    of Alg alorithm.
    """

    def __init__(self, name: str = "default", alg: str = Alg1.__name__):
        print(f"selected algorithm is {alg}")

        for cls in [Alg1, Alg2]:
            if alg == cls.__name__:
                self.alg: Alg = cls(self)
                break
        else:
            raise ValueError()
        self.name = name


c1 = Core("elahe", Alg1.__name__)
c2 = Core("raha", Alg2.__name__)
c3 = Core("parham")

assert c1.alg() == "Alg-1 from elahe"
assert c2.alg() == "Alg-2 from raha"
assert c3.alg() == "Alg-1 from parham"

c1.name = "Elahe"

assert c1.alg() == "Alg-1 from Elahe"
