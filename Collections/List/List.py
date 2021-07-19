mylist = ["apple", "banana", "cherry"]
print(mylist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# To determine how many items a list has, use the len()
print("List Length: ", len(thislist))

list1 = ["abc", 34, True, 40, "male"]
print(list1)

# From Python's perspective, lists are defined as objects with the data type 'list' : type()
print("Type of mylist", type(mylist))

# the list() Constructor:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)