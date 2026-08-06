# Lesson 24: Classes and Objects

## Overview

This lesson introduces one of the most important concepts in Python:

**Object-Oriented Programming (OOP).**

Instead of storing everything in variables or dictionaries, Python allows us to create our own data types using **classes**.

A class acts like a blueprint.

An object is a real item created from that blueprint.

---

## Learning Objectives

After completing this lesson, you should understand:

- What a class is
- What an object (instance) is
- How to create objects
- The purpose of the `__init__()` constructor
- The meaning of `self`
- How to access attributes
- How to modify attributes using dot notation

---

# 1. Creating a Class

A class is created with the `class` keyword.

```python
class Student:
    pass
```

`pass` simply means "do nothing for now."

---

# 2. Creating Objects

Objects are created by calling the class.

```python
student1 = Student()
student2 = Student()
```

Each object is independent.

---

# 3. The Constructor

The constructor is a special function named:

```python
__init__()
```

It automatically runs whenever an object is created.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Now:

```python
student = Student("Mary")
```

Python automatically stores:

```
student.name = "Mary"
```

---

# 4. Understanding self

`self` refers to the current object.

Example:

```python
self.name = name
```

means

```
Store this name inside THIS object.
```

Every object gets its own copy.

---

# 5. Attributes

Attributes are variables that belong to an object.

Example:

```python
student.name
student.course
student.level
```

They are accessed using dot notation.

---

# 6. Modifying Attributes

Attributes can be changed after the object is created.

```python
student.level = "Intermediate"


Output

```

---

# Common Mistakes

### Forgetting self

Wrong

```python
def __init__(name):
```

Correct

```python
def __init__(self, name):
```

---

### Forgetting __init__

Wrong

```python
def init(self):
```

Correct

```python
def __init__(self):
```

---

### Accessing attributes from the class

Wrong

```python
Student.name
```

Correct

```python
student = Student("Mary")
print(student.name)
```

---

# Key Takeaways

✔ A class is a blueprint.

✔ An object is created from a class.

✔ `__init__()` initializes objects.

✔ `self` refers to the current object.

✔ Dot notation accesses object attributes.

✔ Every object has its own data.

---

## mini_project

Create a `Laptop` class with:

- brand
- ram
- storage

Create two laptop objects and print all their information.