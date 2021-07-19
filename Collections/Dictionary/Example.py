print("Example 1: ")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

# ***************************************************************
print("Example 2: ")
car2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car2.values()

print(x) #before the change

car2["year"] = 2020

print(x) #after the change

# ***************************************************************
print("Example 3: ")
dict3 = {
    "name": "maryam",
    "family": "Askari",
    "ageYear": 1994,
    "status": "student"
}
del dict3
print(dict3) # this will cause an error because "thisdict" no longer exists.

