# Boolean 2 meghdar ra barmigardanad -----> 1. True   &    2. False
# When you run a condition in an if statement, Python returns ----> True or False

print(10 > 9)
print(10 == 9)
print(10 < 9)

# **************************************************

print()
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# **************************************************
# The bool() function allows you to evaluate any value, and give you True or False in return.
print()
# Evaluate a string and a number
print(bool("Hello"))
print(bool(15))

# **************************************************
print("Most Values are True")
# The following will return True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# **************************************************
print()
print("bool(False): " + bool(False))
print("bool(None): "+bool(None))
print("bool(0): "+bool(0))
print("bool(""): "+bool(""))
print("bool(()): "+bool(()))
print("bool([]): "+bool([]))
print("bool({}): "+bool({}))

# **************************************************
x = 200
print(isinstance(x,int))