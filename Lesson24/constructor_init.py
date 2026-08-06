class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

student = Student("Mary", "AI Engineering")

print(student.name)
print(student.course)