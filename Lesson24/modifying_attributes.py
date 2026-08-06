class Student:

    def __init__(self, name, level):
        self.name = name
        self.level = level

student = Student("Mary", "Beginner")

print("Before:")
print(student.level)

student.level = "Intermediate"

print()

print("After:")
print(student.level)