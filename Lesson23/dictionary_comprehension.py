# Dictionary Comprehension

employee_salary = {
    "Mary": 500000,
    "John": 450000,
    "Sarah": 550000
}

updated_salary = {
    name: salary + 50000
    for name, salary in employee_salary.items()
}

print("Original Salary")

print(employee_salary)

print()

print("Updated Salary")

print(updated_salary)