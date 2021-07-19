# Raise an error and stop the program if x is lowe than 0:

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# ****************************************************************************

# TypeError if x is not an integer:

a = "hello"

if not type(a) is int:
    raise TypeError("Only integers are allowed")

# ****************************************************************************