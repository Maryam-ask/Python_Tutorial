car = {
    "brand": "volvo",
    "model": "X60",
    "year": 1999
}

# taghire year
# car["year"] = 2018

# Ba estefade az Method Update():
car.update({"year":2020})

car.update({"color":"red"})

# *********************************************************************
# Remove Dictionary Items:
# 1. pop():
car.pop("model")
print(car)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead).
car.popitem()
print(car)

# 2. del:
del car["brand"]
print(car)

# 3. clear()
car.clear()
print(car)
