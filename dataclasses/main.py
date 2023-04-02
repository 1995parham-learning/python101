import dataclasses
import typing


@dataclasses.dataclass(slots=True)
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
    s1 = Student("Parham", "Alvani", 30, "9231058")
    s2 = Student("Elahe", "Dastan", 20, "9631025")

    print(Student.students)

    # Member "score" is unknown because we are using __slots__
    # s1.score = 80

    # 'Student' object has no attribute '__dict__'
    # because we are using __slots__
    # print(s1.__dict__)
