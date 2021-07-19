thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[0])

# ************************************************************
# Negative Index:
# -1 refers to the last item, -2 refers to the second last item etc.
thistuple2 = ("apple", "banana", "cherry")
print("\nLast item with Negative Index:", thistuple2[-1])

# ************************************************************
# Range Of Indexes:

thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("\nBetween 3-5 elements: ", thistuple3[2:5])

print("Elements before 4th: ", thistuple3[:4])

print("Elements after 3red one: ", thistuple3[2:])

print(thistuple3[-4:-1])

# ************************************************************
# Check if Item Exists:
thistuple4 = ("apple", "banana", "cherry")
if "apple" in thistuple4:
    print("Yes, 'apple' is in the fruits tuple")