# *arg in function Arguments ----> then accessible as the tuple


def my_function(named_arg, *args):
    print(named_arg)
    print(args)


my_function(1, 2, 3, 4, 5)
# !! The parameter *args must come after the named parameters to a function.
# !! The name args is just a convention; you can choose to use another.

# ****************************************************************************
print("\nDefault Values:")


def func(x, y, food = "spam"):
    print(food)


func(1, 2)
func(3, 4, "egg")


# ****************************************************************************

# **kwargs (keyword arguments): ----> a dictionary
print("\n**kwargs")


def my_funvtion_2(x, y = 7, *args, **kwargs):
    print(kwargs)


my_funvtion_2(2, 3, 4, 5, 6, a = 7, b = 8, c = "Mary", d =12.876)
# The arguments returned by **kwargs are not included in *args.
