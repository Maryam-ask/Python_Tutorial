num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)     # true
print("spam" not in word_set)

# !!! To create an empty set, you must use set(), as {} creates an empty dictionary.

# **************************************************************************************************

nums = {1, 2, 1, 3, 4, 5, 6, 7, 8, 1, 4, 22}

print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
print(len(nums))

# Basic uses of sets include membership testing and the elimination of duplicate entries.

# **************************************************************************************************

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

# Union | : ----> combines two sets to form a new one containing items in either.
print("Union: ", first | second)

# Intersection & : ----> gets items only in both.
print("Intersection: ", first & second)

# Difference - : ----> gets items in the first set but not in the second.
print("Difference: ", first - second)

# Symmetric difference ^ : ----> gets items in either set, but not both.
print("Symmetric difference: ", first ^ second)