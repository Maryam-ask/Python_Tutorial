# Arguments:
# Functions can take arguments, which can be used to generate the function output.
def print_with_exclamation(word):
    print(word + "!")


print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")


# ******************************************************************************************
# Even better, you can define functions with more than one argument; separate them with commas.
def print_sum_twice(x, y):
    print(x + y)
    print(x + y)


print_sum_twice(5, 8)

# ******************************************************************************************
# Returning from Functions:
def max(x, y):
    if x >=y:
        return x
    else:
        return y


print(max(4, 7))
z = max(8, 5)
print(z)


"""
Once you return a value from a function, it immediately stops being executed.

Any code placed after the return statement won’t be executed. 
"""
def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")


print(add_numbers(4, 5))
# ******************************************************************************************
