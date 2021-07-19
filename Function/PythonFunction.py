def my_function():
    print("Hello from a function!")


# calling function
my_function()


# *************************************************************************
def printMyName(name):
    print("your name is " + name)


printMyName("Maryam")
printMyName("András")


# *************************************************************************
def writeFullName(name, family):
    print("your fullname is: " + name + " " + family)


writeFullName("Maryam", "askari")


# *************************************************************************
# Arbitrary Arguments, *args:
def my_function1(*kids):
    print("The youngest child is " + kids[2])


my_function1("Emil", "Tobias", "Linus")


# *************************************************************************
# Keyword Arguments
# You can also send arguments with the key = value syntax.
def my_function2(child3, child2, child1):
    print("The youngest child is " + child3)


my_function2(child1="Maryam", child2="Nadia", child3="Mohammad")


# *************************************************************************
# Arbitrary Keyword Arguments, **kwargs:
def my_function3(**kids):
    print("The youngest child is " + kids["lname"])


my_function3(fname="tobias", lname="refsens")

# *************************************************************************
# Default Parameter Value:
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def countryName(country = "Norway"):
    print("I am from " + country)

countryName("Sweden")
countryName("Iran")
countryName()   # be tore pishfarz Norway migozarad.!!!!
countryName("Hungary")


# *************************************************************************
# Passing a List as an Argument:
def listOfFoods(food):
    for x in food:
        print(x)


foods = ["lasaig", "ghormesabzi", "pizza", "makaroni"]
listOfFoods(foods)