from __future__ import annotations
import abc


class Alg(abc.ABC):
    """
    Abstract implementation of Alg algorithm.

    Alg algorithm uses the information from its attached type.
    it only attaches to Core class.
    """

    def __init__(self):
        self.core: Core | None = None

    def __get__(self, obj: Core, objtype):
        if objtype is Core:
            self.core = obj
            return self
        else:
            raise AttributeError()

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
        if self.core is not None:
            return f"Alg-1 from {self.core.name}"


class Alg2(Alg):
    """
    Second implementation of the Alg algorithm.
    """

    def run(self):
        if self.core is not None:
            return f"Alg-2 from {self.core.name}"


class Core:
    """
    Core uses Alg algorithm and we wnat to control its implementation
    of Alg alorithm.
    """

    # the descriptor must be in either the owner’s class dictionary
    # or in the class dictionary for one of its parents
    # by default core uses first implemtnation of Alg.
    alg: Alg = Alg1()

    def __init__(self, name: str = "default"):
        self.name = name


c1 = Core("elahe")
c2 = Core("raha")

assert c1.alg() == "Alg-1 from elahe"
assert c2.alg() == "Alg-1 from raha"

# sadlly this chnages implementation
# on all instances.
Core.alg = Alg2()

assert c1.alg() == "Alg-2 from elahe"
assert c2.alg() == "Alg-2 from raha"
