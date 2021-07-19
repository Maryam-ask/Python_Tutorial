# return an Iterator from atuple, and print each value?
tuple1 = ("apple", "banana", "mango", "cherry")
iterator1 = iter(tuple1)  # methode iter() mojod dar tuple

print(next(iterator1))
print(next(iterator1))
print(next(iterator1))


# ********************************************************************
print()
fruitName = "banana"
iterator2 = iter(fruitName)

print(next(iterator2))
print(next(iterator2))
print(next(iterator2))