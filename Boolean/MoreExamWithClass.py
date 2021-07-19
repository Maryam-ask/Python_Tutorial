class myclass():
    def __len__(self):
        return 0


# that is if you have an object that is made from a class with a __len__ function that returns 0 or False
myobj = myclass()
print(bool(myobj))


def myFunction():
    return True

print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")