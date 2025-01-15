class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.marks > 50

    def __str__(self):
        return f"{self.name} {self.marks}"


def main():
    student = Student("Maciek", 55)
    student2 = Student("Norbert", 49)

    print(student.is_passed())
    print(student2.is_passed())


if __name__ == "__main__":
    main()
