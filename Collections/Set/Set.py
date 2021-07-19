set1 = {"apple", "banana", "mango", "cherry"}
print(set1)

# *****************************************************
# Duplicates Not Allowed
thisset1 = {"apple", "banana", "cherry", "apple", "mango", "banana", "apple"}
print(thisset1)

# *****************************************************
# Get the Length of a Set
thisset2 = {"apple", "banana", "cherry"}
print("\nLength :", len(thisset2))

# *****************************************************
# Set - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# *****************************************************
# A set can contain different data types:
set4 = {"abc", 34, True, 40, "male"}

# *****************************************************
# type():
print("\nset4 type is: ", type(set4))

# *****************************************************
# set() Constructor
thisset2 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset2)