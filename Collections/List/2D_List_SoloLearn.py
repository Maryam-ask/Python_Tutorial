m = [
    [1, 2, 3],
    [4, 5, 6]
]

print(m[1][2])

# Strings can be indexed like lists too!
str = "Hello world!"
print(str[6])

# we can do with lists just keeps growing!
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

# It returns True if the item occurs one or more times in the list, and False if it doesn't.
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

# Example:
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])