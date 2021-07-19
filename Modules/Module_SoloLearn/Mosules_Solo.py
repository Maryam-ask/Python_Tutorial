# example of using the random module:
import random

for i in range(5):
    value = random.randint(1, 11) # beine adade 1 ta 11 va khode 11 hast.
    print(value)

# ********************************************************************************
import math

num = 128
print(math.sqrt(num))

# ********************************************************************************
from math import pi
print(pi)

# ********************************************************************************
# You can import a module or object under a different name using the as keyword:

from math import sqrt as square_root
print(square_root(100))