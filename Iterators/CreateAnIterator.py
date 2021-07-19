# Create an Iterator:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a +=1
        return x


# Create Object:
myClass = MyNumbers()
myiterator = iter(myClass)

print(next(myiterator))
print(next(myiterator))
print(next(myiterator))