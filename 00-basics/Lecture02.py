# ==========================================
# LECTURE 2: STRINGS IN PYTHON
# ==========================================

# 1. Creating a String

name = "Jay"

print(name)


# 2. String with Single Quotes

name = 'Jay'

print(name)


# 3. String with Double Quotes

name = "Python"

print(name)


# 4. Multiline String

text = """Hello
Welcome to Python
Full Course"""

print(text)


# 5. String Indexing

name = "Python"

print(name[0])
print(name[1])
print(name[-1])


# 6. String Slicing

name = "Python"

print(name[0:3])
print(name[2:6])
print(name[:4])
print(name[2:])


# 7. String Length

name = "Python"

print(len(name))


# 8. Convert to Uppercase

name = "python"

print(name.upper())


# 9. Convert to Lowercase

name = "PYTHON"

print(name.lower())


# 10. Capitalize

name = "python"

print(name.capitalize())


# 11. Title

text = "python programming"

print(text.title())


# 12. Replace

text = "I like Java"

print(text.replace("Java", "Python"))


# 13. Check String

name = "Python"

print("Python" in name)
print("Java" in name)


# 14. String Concatenation

first_name = "Jay"
last_name = "Dixit"

full_name = first_name + " " + last_name

print(full_name)


# 15. String Repetition

text = "Python "

print(text * 3)