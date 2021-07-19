set1 = {"maryam", "nadia", "mohammad", "ali", "hasan", "sara"}
set1.remove("ali")
print("set1 after removing 'ali' is: ",set1)

# !!! If the item to remove does not exist, remove() will raise an error.

# ****************************************************************
# Discard()
# !!! If the item to remove does not exist, discard() will NOT raise an error.
set1.discard("hasan")
print("s1 after discard 'hasan' is: ",set1)

# ****************************************************************
# pop(): ---->  but this method will remove the last item
# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
set1.pop()
print("set1 after pop(): ", set1)

# ****************************************************************
# Clear():
set2 = {"apple", "banana", "cherry", "mango"}
set2.clear()
print("set2 after clear(): ",set2)

# ****************************************************************
# del: ----> will delete the set completely:
set3 = {"apple", "banana", "cherry"}
del set3
print("set3 after del: ",set3)