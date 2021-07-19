def factorial(n):
    if n == 1:  # base case
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# *****************************************************************
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)


def is_odd(x):
    return not is_even(x)


print(is_odd(2))
print(is_even(2))

# *****************************************************************

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(4))

# *****************************************************************
