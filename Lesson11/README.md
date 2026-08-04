# Lesson 11: Strings and String Manipulation

## Lesson Objectives

By the end of this lesson I should be able to:

- Create and work with strings.
- Use common string methods.
- Extract characters using string slicing.
- Format strings using f-strings.
- Split and join strings.
- Understand that strings are immutable.

---

## Questions and Solutions

### Question 1

Clean the customer's name by removing extra spaces and capitalizing it properly.

**Solution:** `string_methods.py`

---

### Question 2

Practice string slicing to extract different parts of a string.

**Solution:** `slicing.py`

---

### Question 3

Use an f-string to print a formatted coffee order receipt.

**Solution:** `formatting.py`

---

### Question 4

Clean and format a drink order before displaying it.

**Solution:** `string_methods.py`

---

### Question 5

Create a formatted receipt from customer, drink and price information.

**Solution:** `formatting.py`

---

### Question 6

Split a comma-separated string into individual values, convert the values to the correct format, and print a receipt.

**Solution:** `split_join.py`

---

### Question 7

Practice reading and predicting string slicing output.

**Solution:** `slicing.py`

---

### Question 8

Practice slicing with step values and reverse slicing.

**Solution:** `slicing.py`

---

### Question 9

Explain what each line of a string manipulation program does.

**Solution:** `challenges.py`

---

### Question 10

Practice more string indexing and slicing exercises.

**Solution:** `slicing.py`

---

### Question 11

Extract the username and domain from an email address using string methods and sequence unpacking.

**Solution:** `split_join.py`

---

### Question 12

Answer theory questions about strings, immutability, slicing, split(), join(), sequence unpacking and slice steps.

**Solution:** `challenges.py`

---

## What I Learned

- Strings are immutable, meaning they cannot be modified directly.
- String methods return a new string and usually need to be assigned to a variable.
- The `strip()` method removes whitespace.
- The `title()` method capitalizes the first letter of every word.
- The `capitalize()` method capitalizes only the first letter of the string.
- The `upper()` and `lower()` methods change letter casing.
- Slicing extracts part of a string using indexes.
- The end index in a slice is excluded.
- Negative indexes count from the end of a string.
- The step value controls how Python moves through a string.
- f-strings provide a clean way to format output.
- `split()` converts a string into a list.
- `join()` combines a list of strings into one string.
- Sequence unpacking allows multiple variables to receive values from a list.

---

## Real-World Application

String manipulation is one of the most frequently used skills in software development. It is used to clean user input, validate email addresses, format reports, generate receipts, process CSV files, prepare data for databases, and build APIs. In AI and data engineering, string manipulation is essential for cleaning and preprocessing text before analysis or machine learning.