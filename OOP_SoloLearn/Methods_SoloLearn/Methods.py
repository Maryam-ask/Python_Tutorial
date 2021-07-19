class Dog:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("woof!")


fido = Dog("Fido", "brown")
print(fido.name)
print(fido.legs)
fido.bark()

print(Dog.legs)


# *******************************************************
class Student:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("Hi from " + self.name)


s1 = Student("Mary")
s1.sayHi()