class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)


s = Spam()
s.print_egg()

print(s._Spam__egg)  # access from outside of the class.
# print(s.__egg)