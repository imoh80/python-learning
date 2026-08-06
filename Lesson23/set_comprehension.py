# Set Comprehension

languages = [
    "Python",
    "PYTHON",
    "Java",
    "JAVA",
    "Go",
    "GO"
]

clean_languages = {
    language.lower()
    for language in languages
}

print(clean_languages)

messy_names = [
    " Mary ",
    "MARY",
    "John ",
    " john"
]

clean_names = {
    name.strip().lower()
    for name in messy_names
}

print(clean_names)