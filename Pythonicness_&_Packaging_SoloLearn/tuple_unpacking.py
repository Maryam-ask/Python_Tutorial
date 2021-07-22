# Tuple Unpacking:
numbers = (1, 2, 3, 4)

a, b, c, d = numbers
a, b = b, a
# This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side forms the tuple (b, a) which is then unpacked.

print(a)
print(b)
print(c)
print(d)

# *************************************************************
print()

a, b, *c, d, e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a)
print(b)
print(c)
print(d)
print(e)