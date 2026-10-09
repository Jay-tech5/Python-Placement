
# Python Dictionary Methods

myDict = {
    "name": "Jay",
    "age": 22,
    "course": "BCA",
    "city": "Pune"
}

# 1. keys() - Returns all keys
print("1. keys():")
print(myDict.keys())
print()

# 2. values() - Returns all values
print("2. values():")
print(myDict.values())
print()

# 3. items() - Returns all key-value pairs
print("3. items():")
print(myDict.items())
print()

# 4. get() - Returns the value of a key
print("4. get():")
print(myDict.get("name"))
print(myDict.get("salary", "Key not found"))
print()

# 5. update() - Adds or updates items
print("5. update():")
newDict = {
    "salary": 25000,
    "city": "Delhi"
}

myDict.update(newDict)
print(myDict)
