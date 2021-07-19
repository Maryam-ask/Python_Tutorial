# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red,"\n")

# ********************************************************
# Using Asterisk* :
"""
If the number of variables is less than the number of values,
you can add an * to the variable name and the values will be assigned to the variable as a list
"""
fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits1

print(green)
print(yellow)
print(red, "\n")

# ********************************************************
fruits2 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits2

print(green)
print(tropic)
print(red)

# ********************************************************
# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print("\nMultiply Tuples: ", mytuple)