try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero! Error!")
finally:
    print("This code will run no matter what!")


# **************************************************************

try:
    print(1)
    print(10 / 0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("this is executed last")