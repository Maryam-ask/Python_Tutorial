thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# ************************************************************
# Print the last item of the list
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# ************************************************************
# Return the third, fourth, and fifth item.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # khaneye 2 niz dar an vojood darad.

# ************************************************************
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # az khoneye 0 ta 4

# ************************************************************
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# ************************************************************
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# ************************************************************
# Check if item Exists:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")