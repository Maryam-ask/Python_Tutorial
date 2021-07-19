fruitName = ["Orange", "Kiwi", "Mango", "Apple", "Pineapple", "Banana"]

fruitName.sort()
print(fruitName)

fruitName.sort(reverse=True)
print(fruitName)
# *******************************************************************
# Mesale bedone darnazar gereftane horoofe bozorg o koochak:
myList = ["banana", "mango", "Kiwi", "Orange", "apple", "Strawberry"]
myList.sort(key= str.lower)
print("sort is: ",myList)
myList.reverse()
print(myList)

myList2 = ["banana", "mango", "Kiwi", "Orange", "apple", "Strawberry"]
myList2.reverse()
print("reverse: ", myList2)

# *******************************************************************
numberList = [20, 100, 35, 50, 80, 1]
numberList.sort()
print(numberList)

numberList.sort(reverse=True)
print(numberList)

# *******************************************************************
def myfunc(n):
    return abs(n - 50)

numbers = [100, 50, 85, 20, 10]
numbers.sort(key = myfunc)
print(numbers)
