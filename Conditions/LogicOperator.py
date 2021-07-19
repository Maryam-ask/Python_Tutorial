# And:

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

# ****************************************************************************************************
# or:

a1 = 200
b1 = 33
c1 = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# ****************************************************************************************************
# Nested If:
# You can have if statements inside if statements, this is called nested if statements.

x = 40
if x > 10:
    print("Above 10,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# ****************************************************************************************************
# pass statement:
"""
if statements cannot be empty,
 but if you for some reason have an if statement with no content,
 put in the pass statement to avoid getting an error.
"""
a2 = 33
a3 = 200
if b > a:
    pass

# ****************************************************************************************************