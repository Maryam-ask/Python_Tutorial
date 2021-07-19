# Change The second item
print("Change The second item: ")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# **************************************************************
# Change a Range of Item Values:
print("\nChange a Range of Item Values: ")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# **************************************************************
# Change the second value by replacing it with two new values
print("\nChange the second value by replacing it with two new values: ")
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist, "\n")

# **************************************************************
# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# **************************************************************
# Insert() Items
print("\nInsert() Method: ")
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# **************************************************************
# Append():
print("\nAppend() Method: ")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# **************************************************************
# Extend() : Baraye vasl kardane 2 ta list be yekdigar.
print("\nExtend() Method: ")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# **************************************************************
# Add elements of a tuple to a list:
print("\nAdd elements of a tuple to a list with extend() Method: ")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# **************************************************************
# Remove():
print("\nRemove() Method: ")
thislist = ["Maryam", "Nadi", "Mohammad", "Ali"]
thislist.remove("Ali")
print(thislist)

# **************************************************************
# pop(): Baraye pak kardan ba estefade az shomareye index.
print("\nPop() Method: ")
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist.pop() #Remove the last item
print(thislist)
# **************************************************************
# The del keyword also removes the specified index.
print("\ndel keyword: ")
mylist = [78, 98, 20, 18, 1]
del mylist[1]
print(mylist)

# The del keyword can also delete the list completely.
del mylist

# **************************************************************
# clear() Method:
print("\nClear() Method: ")
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# **********************************************************************
# update() Method:
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print("\nUpdate() Method: ",fruits)

