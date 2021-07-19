# For building a Function we need to start with def

x = "My Love"


def printMe():  # Baraye eijade yek Function
    print(x + " is András")  # Mitavanim az variable khareje function estefade konim darone function


printMe()  # Dar inja function ya hamon method ra seda mizanim

print("----------------------------------")
# **************************************************************

y = "Maryam"


def myFunction():
    y = "Saaaalaaaam"
    print(y)


myFunction()
print("Y = " + y)
print("----------------------------------")
# **************************************************************

# The global Keyword
print("# The global Keyword")

"""
Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
"""


def myGlobalV():
    global z
    z = "Hello world!"


myGlobalV()
print("The Global variable is: " + z)

# use the global keyword if you want to change a global variable inside a function.

name = "Nadia"


def changeName():
    global name
    name = "Maryam"


changeName()  # !!! Baraye estefade az function hatman bayad an ra seda bezanim
print(name)
