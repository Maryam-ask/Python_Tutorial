# Add 10 to argument a, and return the result.
x = lambda a: a + 10
print(x(5))

# ****************************************************************************
# Multiply argument a with argument b and return the result.
y = lambda a, b: a * b
print(y(4, 6))

# ****************************************************************************
# Summarize argument a, b, and c and return the result.
z = lambda a, b, c: a + b + c
print(z(3, 8, 6))

# ****************************************************************************

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2) # n ra tarif mikonim

print(mydoubler(10)) # a ra tarif mikonim
