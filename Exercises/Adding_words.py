"""
Adding Words:


You need to write a function that takes multiple words as its argument and
returns a concatenated version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.

Sample Input
this
is
great

Sample Output
this-is-great
"""


def concatenate(*args):
    result = ""
    for str in range(len(args) - 1):
        result += args[str] + "-"

    return result + args[len(args) - 1]


print(concatenate("I", "love", "Python", "!"))
