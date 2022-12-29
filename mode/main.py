from collections import Counter
from collections.abc import Iterable, Hashable
from typing import TypeVar


# golang way of using interfaces for having generics.
# the return type is not concrete so you cannot do anything
# useful with it.
def mode_in_go_way(data: Iterable[Hashable]) -> Hashable:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError("no mode for empty data")

    return pairs[0][0]


HashableT = TypeVar("HashableT", bound=Hashable)


def mode(data: Iterable[HashableT]) -> HashableT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError("no mode for empty data")

    return pairs[0][0]


mgo = mode_in_go_way(["Hello", "Hi", "Hello"])
print(mgo)
# you have only hash method on your shoes.

m = mode(["Hello", "Hi", "Hello"])
print(m)
# you have all methods of your type, because
# return type has the same type as your given iterable type.
