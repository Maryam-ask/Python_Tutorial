print("Hi")
print(2 + 3)
print("Maryam" + " " + "András")

# **************************************
print("---------------------------------------------")
if 6 < 7:
    print("Hello, world!")

"""
This is a comment
written in
more than just one line
"""

# **************************************

#       Python variables:
print("Python Variables")
x = 12
y = "Maryam"
z = 12.304
print("X: " + str(x) + " y= " + y + " Z: " + str(z))
print("---------------------------------------------")

x = 2  # x is of type int
y = "Sara"  # y is of type str
print(x)
print(y)
print("---------------------------------------------")

x = int(3)  # x is 3
y = str(3)  # y is '3'
z = float(3)  # z is 3.0
print("---------------------------------------------")

print("For Gettin Type of the Variables")
# Get the TYPE
print(type(x))
print(type(y))
print(type(z))
print("---------------------------------------------")

# *****************
# Single or double quotation are same

x = "Maryam"
print(x)
x = 'Maryam'
print(x)
print("---------------------------------------------")
# *********************************

"""
 Rules for Python variables:

    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    
    Camel Case  :   myVariableName
    Pascal Case  :   MyVariableName
    Snake Case   :  my_variable_name
"""

# *********************************************************

#           Many Values to Multiple Variables
print("We can have Many Values to Multiple Variables")
x, y, z = 12, "Marya", 13.2    # !!!!!! Beine Variable ha hatman bayad , (Virgul) bezarim
print("X = "+str(x))
print("Y = "+y)
print("Z = "+str(z))

print("Multiple variables can have one value")
x = y = z = "I Love András"         # !!!!! Tavajoh dashte bash inja bejaye , bayad = begozarim
print("X = "+x)
print("Y = "+y)
print("Z = "+z)
print("---------------------------------------------")

# *********************************************************

print("Unpack a Collection")

"""
If you have a collection of values in a list, tuple etc. 
Python allows you extract the values into variables. 
This is called unpacking.
"""
fruits = ["Apple", "Orange", "banana"]
x, y, z = fruits
print("X = "+x)
print("Y = "+y)
print("Z = "+z)
