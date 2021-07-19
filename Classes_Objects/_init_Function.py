# The __init__() Function:
class Person:
    def __init__(self, name, age): # hamon constractore.
        self.name = name
        self.age = age


p1 = Person("John",36)
print(p1.name)
print(p1.age)

# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.