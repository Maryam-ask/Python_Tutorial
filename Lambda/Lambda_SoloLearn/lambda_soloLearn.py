def my_func(f, arg):
    return f(arg)


my_func(lambda x: 2 * x * x, 5)


# *******************************************

# function:

def polynomial(x):
    return x ** 2 + 5 * x + 4


print(polynomial(-4))

# lambda:
print((lambda x: x ** 2 + 5 * x + 4)(-4))


# *******************************************
# Lambda functions can be assigned to variables, and used like normal functions.

double = lambda x: x * 2
print(double(7))

# *******************************************

# EXAMPLE:
triple = lambda x: x * 3
add = lambda x, y: x + y

print(add(triple(3), 4))