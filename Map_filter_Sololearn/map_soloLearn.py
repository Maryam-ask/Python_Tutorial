# Map:

def add_five(x):
    return x + 5


nums = [10, 22, 34, 60]
result = list(map(add_five, nums)) # To convert the result into a list, we used list explicitly.
print(result)


# ***********************************************
# Lambda:
nums = [11, 22, 45, 6, 7]

result = list(map(lambda x: x + 5, nums))
print(result)


# ***********************************************

# Filter: (boolean)

nums = [11, 22, 39, 45, 60, 3, 80, 24]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)