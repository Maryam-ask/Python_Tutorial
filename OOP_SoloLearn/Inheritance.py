class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("purr.........")


class Dog(Animal):
    def bark(self):
        print("woof!")


fido = Dog("fido", "brown")
print(fido.color)
fido.bark()