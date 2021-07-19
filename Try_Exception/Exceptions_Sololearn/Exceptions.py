# ZeroDivisionError:
num_1 = 7
num_2 = 0
try:
    print(num_1 / num_2)
except:
    print("zeroDevisionError")

# *****************************************

try:
    number1 = 89
    number2 = 0
    print(number1/number2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("Due to zero division")
# In the code above, the except statement defines the type of exception to handle
# (in our case, the ZeroDivisionError).

# *****************************************

try:
    variable = 10
    print(variable + "hello")
    print(variable/2)
except ZeroDivisionError:
    print("Divided by zero")
except(ValueError, TypeError):
    print("Error occurred!")

# *****************************************
try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred!")