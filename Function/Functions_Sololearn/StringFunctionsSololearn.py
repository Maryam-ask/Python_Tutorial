# strin format() function:
# which enables values to be embedded in it, using placeholders.

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)
"""
Each argument of the format function is placed in the string at the corresponding position,
which is determined using the curly braces { }.
"""

# You can also name the placeholders, instead of the index numbers.
a = "{x}, {y}".format(x=5, y=12)
print(a)


# ******************************************************
"""
join ---> joins a list of strings with another string as a separator.

replace ---> replaces one substring in a string with another.

startswith and endswith ---> determine if there is a substring at the start and end of a string, respectively.

lower and upper –--> changes the case of a string

split ---> the opposite of join, turns a string with a certain separator into a list. 
"""
print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
# prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
# prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
# prints "['spam', 'eggs', 'ham']"

# ******************************************************
