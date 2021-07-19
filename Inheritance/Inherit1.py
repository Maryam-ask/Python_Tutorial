# adding the __init__() Function
class Person:
    def __init__(self, id, name, family):
        self.id = id
        self.name = name
        self.family = family


class Teacher(Person):
    def __init__(self, id, name, family, title):
        super().__init__(id, name, family)
        self.techingTitle = title

    def welcome(self):
        print("Welcome ",self.name, self.family)


t1 = Teacher(124, "Marzieh", "Abbasi", "Java Teacher")
print(t1.name, t1.techingTitle)
