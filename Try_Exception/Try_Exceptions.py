try:
    print(x) # The try block will generate an exception, because x is not defined:
except:
    print("An exception occurred!")


# print(a)


# ************************************************************************************
# Print one message if the try block raises a NameError and another for other errors.
print('***********')
try:
    print(b)
except NameError:
    print("Variable b is not defined")
except:
    print("Something else went wrong")

# ************************************************************************************
# Else:
# You can use the else keyword to define a block of code to be executed if no errors were raised.
print('***********')
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# ************************************************************************************
# Finally:
# the finally block, it specified, will be executed regardless if the try block raises an error or not.
print('***********')
try:
    print(a)
except:
    print("Something went wrong")
finally:
    print("the 'try except' is finished")