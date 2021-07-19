# Convert from JSON to Python
import json

# some JSON:
x = '{ "name":"Marya", "age":26, "city":"Stockholm"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])