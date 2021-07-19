from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)

print(list(takewhile(lambda x: x <= 6, nums)))


# ********************************************************'
nums_2 = [2, 4, 5, 6, 7, 8, 9]
a = takewhile(lambda n: n%2 == 0, nums_2)

print(list(a))