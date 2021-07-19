def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


print(apply_twice(add_five, 10))


# ************************************************************
def test(func, num):
    return func(func(num))


def mult(x):
    return x * x


print(test(mult, 2))
# ************************************************************
