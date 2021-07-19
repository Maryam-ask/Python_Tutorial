set1 = {"maryam", "nadia", "mohammad", "ali", "hasan", "sara"}

for x in set1:
    print(x)

# *********************************************************************
# Join Two Sets:
# 1.union(): ----> The union() method returns a new set with all items from both sets.
set2 = {"aa", "a", "b", "dd", "abcd"}
set3 = {1, 2, 3, 43, 32, 190}
set4 = set2.union(set3)
print("union of set2 and set3 is: ", set4)

# *********************************************************************
# 2.update(): ----> The update() method inserts the items in set6 into set5:
set5 = {"ma", "abs", "dad", "a", "b", "c"}
set6 = {1, 22, 67, 100, 96, 56}
set5.update(set6)
print("set5.update(set6) is: ", set5)

# *********************************************************************
# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print("The duplicate item between set x and y is: ", x)


#  The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("z = x.intersection(y): ", z)

# *********************************************************************
# Keep All, But NOT the Duplicates:
# 1. symmetric_difference_update():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print("Keep All, But NOT the Duplicates between x and y: ", x)


# 2. symmetric_difference():
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

