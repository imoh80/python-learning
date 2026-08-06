employee = {
    "name": "Mary Imoh",
    "department": "AI Engineering",
    "salary": 500000
}

print("Employee Record")
print("-" * 25)

print(f"Name: {employee['name']}")
print(f"Department: {employee['department']}")
print(f"Salary: ₦{employee['salary']:,}")

employee["salary"] = 600000
employee["country"] = "Nigeria"

print("\nUpdated Record")
print("-" * 25)

print(f"Name: {employee['name']}")
print(f"Department: {employee['department']}")
print(f"Salary: ₦{employee['salary']:,}")
print(f"Country: {employee.get('country')}")