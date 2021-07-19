thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# halate 1:
x = thisdict["model"]
print(x)

# halate 2: estefade az methode get():
y = thisdict.get("model")
print(y)

# Get keys:
# The keys() method will return a list of all the keys in the dictionary.
key = thisdict.keys()
print("List of keys are: ", key)

# Get values:
# The values() method will return a list of all the values in the dictionary.
value = thisdict.values()
print("list of values are: ", value)

# Get items:
# The items() method will return each item in a dictionary, as tuples in a list.
items = thisdict.items()
print("list of items are: ", items)

# ************************************************************************
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

carKeys = car.keys()
print(carKeys)

car["color"] = "White"
print(carKeys)

carValues = car.values()
print(carValues)

car["year"] = 2020
print(carValues)

if "model" in car:
    print("yes, 'model' is one of the kes in the car dictionary.")
    