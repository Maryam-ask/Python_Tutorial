# StopIteration:
class MyNumbers:
    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        if self.number <= 20:
            x = self.number
            self.number +=1
            return x
        else:
            raise StopIteration


ob1 = MyNumbers()
obIter = iter(ob1)
for i in obIter:
    print(i)