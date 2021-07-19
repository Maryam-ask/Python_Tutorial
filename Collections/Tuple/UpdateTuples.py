# Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print("Change Tuple Values: ", x)

# ****************************************************************
# Add Items:
thistuple1 = ("apple", "banana", "cherry")
# Halate 1:
z = list(thistuple1)
z.append("orange")
thistuple1 = tuple(z)
print("Add Items: (Halate 1) ", thistuple1)
# Halate 2:
y = ("orange",)
thistuple1 += y
print("Add Items: (Halate 2) ", thistuple1)

# ****************************************************************
# Remove Items:
thistuple2 = ("apple", "banana", "cherry")
y = list(thistuple2)
y.remove("apple")
thistuple2 = tuple(y)
print("Remove Items: (apple) ",thistuple2)

# ****************************************************************
# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
