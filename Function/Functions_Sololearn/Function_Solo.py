# Function can also be used as arguments of other function
def add(a, b):
    return a + b


def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

# func(5,10) = 15
# func(5,10) = 15
# func(func(5,10) , func(5,10)) = func(15,15) = 30


number1 = 5
number2 = 10

print(add(number1, number2))
print(do_twice(add, number1, number2))

# ***************************************************************


def square(x):
    return x * x


def test(func, x):
    print(func(x))


test(square, 4)