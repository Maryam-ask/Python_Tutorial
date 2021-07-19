# Python Scope:
def myFunction():
    x = 300
    print(x)  # local scope


myFunction()


# ***************************************
# Function inside function:
def func1():
    num = 2050

    def myInnerFunc():
        print(num)

    myInnerFunc()


func1()

# ***************************************
# Global Scope:
var = "global scope"


def printvar():
    print(var)


printvar()
print(var)  # hardo yeki hastand.

# ***************************************
a = 2021


def yearprint():
    a = 1994
    print(a)


yearprint()  # a drooni ya local ra seda mizanad
print(a)  # a biroony ya global ra seda mizanad


# ***************************************
# Global Keyword:
# !!! The global keyword makes the variable global.
def hello():
    global word
    word = "Hello world!"


hello()
print(word)

# ********************************************
name = "Maryam"


def myname():
    global name
    name = "Nadia"


myname()
print(name)
