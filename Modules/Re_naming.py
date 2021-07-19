import myModule as mx

a = mx.person1["name"]
print(a)


# **************************
import platform

x = platform.system()
d = dir(platform)
# !!! The dir() function can be used on all modules, also the ones you create yourself.

print(x)
print(d)

# *******************************************
# Import From Module:
from myModule import person1

print(person1["country"])