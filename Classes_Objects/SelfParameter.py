"""
The self Parameter:

The self parameter is a reference to the current instance of the class,
 and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like,
 but it has to be the first parameter of any function in the class
"""

class Person:
    def __init__(thisObject, name, lastname, age):
        thisObject.name = name
        thisObject.lastName = lastname
        thisObject.age = age

    def myFunc(abc):
        print("Hello" + abc.name)


p1 = Person("Maryam", "Askari", 26)
print(p1.myFunc())

# Delete Objects:
del p1
# or
del p1.age



"""
The pass Statement:
class definitions cannot be empty,
but if you for some reason have a class definition with no content,
put in the pass statement to avoid getting an error.
"""
class Person:
    pass