# convert from python to JSON:
import json

# a Python object (dict): ye dictionary mikhahim.
x = {
    "name": "Maryam",
    "Family": "Askari",
    "country": "Sweden",
    "age": 26
}

# convert into JSON:
j = json.dumps(x)

# The result is a JSON string:
print(j)


# **********************************************************

print(json.dumps({"name": "Nadi", "age": 23, "reshteh": "Gerafik"})) # a dictionary
print(json.dumps(["apple", "banana", "mango", "cherry"])) # a list
print(json.dumps(("apple", "mango"))) # a tuple
print(json.dumps("Hello world")) # a string
print(json.dumps(265)) # an integer
print(json.dumps(132.98)) # a float
print(json.dumps(True)) # True
print(json.dumps(False)) # a False
print(json.dumps(None)) # a None

# **********************************************************
person = {
  "name": "Maryam",
  "age": 26,
  "married": True,
  "divorced": False,
  "children": ("Anna","Billy"),
  "pets": None,
  "cars": [  # List of cars
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(person))