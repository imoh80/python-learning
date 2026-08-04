"""
Why must we assign the result of string methods to a variable?

Answer:
Strings are immutable. Methods such as strip(), title(), and upper()
return a new string instead of changing the original string.


Why does string[0:3] return only the first three characters?

Answer:
The end index is excluded. Python starts at index 0 and stops before index 3.


What is the difference between split() and join()?

Answer:
split() converts a string into a list.
join() combines a list of strings into a single string.


What is sequence unpacking?

Answer:
Sequence unpacking assigns multiple variables to the elements of a list
or another iterable in a single statement.


What does the step value in slicing do?

Answer:
The step controls how Python moves through a string.
It determines which characters are selected or skipped.
"""