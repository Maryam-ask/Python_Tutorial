# Dictionary:
age = {"Dave": 24, "Mary": 26, "András": 38, "John": 59}

print(age["Dave"])
print(age["Mary"])

# Each element in a dictionary is represented by a key:value pair.

# *******************************************************************************'

# Trying to index a key that isn't part of the dictionary returns a KeyError.
primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}

print(primary["red"])
# print(primary["yellow"])

# *******************************************************************************
squares = {1: 1, 2: 4, 3: "error", 4: 16, }
squares[8] = 64
squares[3] = 9
print(squares)
print(squares[squares[2]])

# *******************************************************************************
numbers = {
    1: "one",
    2: "two",
    3: "three"
}

print(1 in numbers)  # true
print("three" in numbers)  # false
print(4 not in numbers)  # true

# *******************************************************************************
pairs = {1: "apple",
         "orange": [2, 3, 4],
         True: False,
         None: "True",
         }

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

# *******************************************************************************
fib = {
    1: 1,
    2: 1,
    3: 2,
    4: 3
}

print(fib.get(4,0) + fib.get(7,5))
