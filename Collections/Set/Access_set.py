# Access Items:
thisset1 = {"apple", "banana", "cherry"}
for x in thisset1:
    print(x)

# halate 2
print("Halate 2: ")
print("banana" in thisset1)

# ************************************************************
# add() Method:
thisset1.add("orange")
print("adding 'orange' : ", thisset1)

# ************************************************************
# Add Sets
thisset2 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset2.update(tropical)
print(thisset2)

# ************************************************************
# Add Any Iterable
thisset3 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset3.update(mylist)
print(thisset3)
