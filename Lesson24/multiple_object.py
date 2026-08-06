class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

student1 = Student("Mary", "AI Engineering")
student2 = Student("John", "Python")

print(student1.name)
print(student1.course)

print()

print(student2.name)
print(student2.course)