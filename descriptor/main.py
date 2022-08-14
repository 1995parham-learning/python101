from __future__ import annotations
import abc


class Alg(abc.ABC):
    def __init__(self):
        self.core: Core | None = None

    def __get__(self, obj: Core, objtype):
        assert objtype is Core
        self.core = obj
        return self

    def __call__(self):
        return self.run()

    @abc.abstractmethod
    def run(self):
        pass


class Alg1(Alg):
    def run(self):
        if self.core is not None:
            return f"Alg-1 from {self.core.name}"


class Alg2(Alg):
    def run(self):
        if self.core is not None:
            return f"Alg-2 from {self.core.name}"


class Core:
    alg: Alg = Alg1()

    def __init__(self, name: str = "default"):
        self.name = name


c1 = Core("elahe")
c2 = Core("raha")

assert c1.alg() == "Alg-1 from elahe"
assert c2.alg() == "Alg-1 from raha"

Core.alg = Alg2()

assert c1.alg() == "Alg-2 from elahe"
assert c2.alg() == "Alg-2 from raha"
