import dataclasses
import typing


@dataclasses.dataclass
class Student:
    name: str
    family: str
    age: int
    id: str

    students: typing.ClassVar[list[str]] = list()

    def __post_init__(self):
        cls = self.__class__
        cls.students.append(f"{self.name} {self.family}")


if __name__ == "__main__":
    Student("Parham", "Alvani", 30, "9231058")
    Student("Elahe", "Dastan", 20, "9631025")

    print(Student.students)
