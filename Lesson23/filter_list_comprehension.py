# Filtering with List Comprehension

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [num for num in numbers if num % 2 == 0]

odd_numbers = [num for num in numbers if num % 2 != 0]

greater_than_five = [num for num in numbers if num > 5]

print("Even:", even_numbers)
print("Odd:", odd_numbers)
print("Greater than 5:", greater_than_five)