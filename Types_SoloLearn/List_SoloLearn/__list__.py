squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

print(squares[:7])
print(squares[7:])

print(squares[::2])  # Khane har a 2 ta 2 ta tey konam az khaneye 0 ta akhar
print(squares[2:8:3]) # khanehara 3 ta darmian tey konad az khaneye 2 ta 8

print(squares[1:-1]) # az khaneye 1 ta khaneye -1 ke haman 81 ast
print(squares[::-1]) # barax khanehara tey mikonad.

# ***********************************************************
# List Comprehensions:

cubes = [i ** 3 for i in range(5)] # yani i hara ke beine 0 va 5 hastand be tavane 3 beresanad.
print(cubes)

nums = [j * 2 for j in range(10)]
print(nums)


# *****************************
evens = [i ** 2 for i in range(10) if i**2 % 2 == 0]
print(evens)

a = [j for j in range(20) if j % 3 == 0]
print(a)