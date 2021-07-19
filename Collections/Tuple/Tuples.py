tuple1 = ("apple", "banana", "cherry")
print(tuple1)

# *****************************************************************************
# Index numbers
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print("\n",thistuple)

# *****************************************************************************
# Tuple Length:
print("\nthistuple length is: ", len(thistuple))

# *****************************************************************************
# !!!! Create Tuple With One Item !!!!
thistuple = ("apple",) # bayad entehaye an hatman comma bashad vaghti faghat yek meghdar darad
print("first type: ", type(thistuple))

#NOT a tuple
thistuple = ("apple")
print("Second type:", type(thistuple))

# *****************************************************************************
# Tuple -Data types:
tuple2 = ("apple", "banana", "cherry")
tuple3 = (1, 5, 7, 9, 3)
tuple4 = (True, False, False)
# A tuple can contain different data types.
tuple5 = ("abc", 34, True, 40, "male")

# *****************************************************************************
# Tuple Constructor: tuple():
thistuple1 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print("Tuple constructor: ", thistuple1)

