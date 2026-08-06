# Adding items to a set

skills = {"Python", "SQL"}

print("Original")
print(skills)

print()

# Add one item
skills.add("Git")

print("After add()")
print(skills)

print()

# Add multiple items
skills.update(["Machine Learning", "Docker", "Git"])

print("After update()")
print(skills)