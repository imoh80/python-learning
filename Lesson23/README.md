# Lesson 23: Comprehensions (List, Dictionary, Set)

## Overview

Comprehensions provide a concise way to create new collections from existing ones.

Instead of writing multiple lines using loops, Python allows us to generate lists, dictionaries, and sets in a single line.

---

## What You'll Learn

- List Comprehensions
- Filtering with Comprehensions
- Dictionary Comprehensions
- Set Comprehensions
- When to use comprehensions

---

# 1. List Comprehension

Syntax

```python
[expression for item in iterable]
```

Example

```python
numbers = [1, 2, 3]

doubled = [num * 2 for num in numbers]

print(doubled)
```

Output

```
[2, 4, 6]
```

---

# 2. Filtered List Comprehension

Syntax

```python
[expression for item in iterable if condition]
```

Example

```python
numbers = [1,2,3,4,5]

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)
```

Output

```
[2,4]
```

---

# 3. Dictionary Comprehension

Syntax

```python
{
    key: value
    for key, value in dictionary.items()
}
```

Example

```python
prices = {
    "Rice": 5000,
    "Beans": 3500
}

updated = {
    item: price + 500
    for item, price in prices.items()
}
```

---

# 4. Set Comprehension

Syntax

```python
{
    expression
    for item in iterable
}
```

Example

```python
names = ["MARY", "Mary", "John"]

clean = {name.lower() for name in names}

print(clean)
```

Output

```
{'mary', 'john'}
```

---

# Comprehension Comparison

List

```python
[x * 2 for x in numbers]
```

Produces a list.

Set

```python
{x * 2 for x in numbers}
```

Produces a set.

Dictionary

```python
{x: x * 2 for x in numbers}
```

Produces a dictionary.

---

## When to Use Comprehensions

Use comprehensions when you need to

- create a new list
- create a new dictionary
- create a new set
- transform every item
- filter items

Avoid comprehensions when the logic becomes difficult to read.

---

## Key Takeaways

- Comprehensions are shorter than loops.
- List comprehensions use []
- Dictionary comprehensions use {}
- Set comprehensions use {}
- Dictionary comprehensions require key:value pairs.
- Filters come at the end of the comprehension.