dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(dict)

# print the brand value:
print("brand is: ", dict["brand"])
# *******************************************************
# Duplicate values will overwrite existing values:
thisdict1 =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict1)

# the number of items in the dictionary
print("Thisdict's length is: ", len(thisdict1))

# *******************************************************
cardict1 = {
    "brand" : "volvo",
    "electric" : True,
    "year" : 2019,
    "colors" : ["red", "blue", "gray", "white"]
}
print("car info: ",cardict1)

# Print the data type of a dictionary
print("Type of dictionary: ", type(cardict1))