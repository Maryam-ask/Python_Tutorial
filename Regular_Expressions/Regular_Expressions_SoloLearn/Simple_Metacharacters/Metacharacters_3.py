import re

pattern = r"g+"
# * ---> matches 0 or more occurrences of the preceding expression.
# + ---> matches 1 or more occurrence of the preceding expression.

if re.match(pattern, "g"):
    print("Match 1")

if re.match(pattern, "gggggggggg"):
    print("Match 2")

if re.match(pattern, "abc"):
    print("Match 3")

# ***********************************************************
print("************************")

pattern_2 = r"ice(-)?cream"

if re.match(pattern_2, "ice-cream"):
    print("Match 1")

if re.match(pattern_2, "icecream"):
    print("Match 2")

if re.match(pattern_2, "sausages"):
    print("Match 3")

if re.match(pattern_2, "ice--ice"):
    print("Match 4")

# ************************************************

pattern_3 = r"colo(u)?r"

if re.match(pattern_3, "color"):
    print("pattern_3 is match with \'color\'")

if re.match(pattern_3, "colour"):
    print("pattern_3 is match with \'colour\'")