# 1. Create a parent calss:
class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def printName(self):
        print("Person's name is" + self.name + " " + self.family)


# Use the Person class to create an object, and then execute the printname method:
p1 = Person("Maryam", "Askari")
p1.printName()

# 2. Create a child class:
class Student(Person):
    pass

# !!! Use the pass keyword when you do not want to add any other properties or methods to the class.

s1 = Student("Nadia", "Askari")
s1.printName()