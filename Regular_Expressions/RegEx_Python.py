# Regular_Expressions in Python:
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) # Search the string to see if it starts with "The" and ends with "Spain"

if x:
    print("Yes! we have a match!")
else:
    print("No match!")

# ***************************************
# findall() Function:
a = re.findall("ain", txt)
print(a)

b = re.findall("portugal", txt)
print(b)
# ***************************************
# search() Function:
# The search() function searches the string for a match, and returns a Match object if there is a match.
c = re.search("\s", txt)
print("The first white-space character is located in position:", c.start())
# Search for the first white-space character in the string.

d = re.search("portugal", txt)
print(d)

# ***************************************
# split() Function:
e = re.split("\s", txt) # Split at each white-space character
print(e)

f = re.split("\s", txt, 1) # Split the string only at the first occurrence.
print(f)

# ***************************************
# sub() Function:
g = re.sub("\s", "9", txt) # Replace every white-space character with the number 9.
print(g)

# ***************************************
h = re.sub("\s", "000", txt, 2)
print(h)