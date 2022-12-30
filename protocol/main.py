import typing
import dataclasses


class SupportLessThan(typing.Protocol):
    def __lt__(self, other: typing.Any) -> bool:
        # cannot use _pass_ here, should use _..._
        ...


LT = typing.TypeVar("LT", bound=SupportLessThan)


def top(series: typing.Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]


@dataclasses.dataclass
class Person:
    first_name: str
    sur_name: str
    age: int

    def __lt__(self, other: typing.Any) -> bool:
        if isinstance(other, Person):
            return self.age < other.age
        raise ValueError("person is only comparable to person")


if __name__ == "__main__":
    persons = [Person("Elahe", "Dasta", 25), Person("Parham", "Alvani", 30)]
    print(f"the oldest person is {top(persons, 1)}")
