import re

pattern = r"egg(spam)*"
# matches strings that start with "egg" and follow with zero or more "spam"s.

if re.match(pattern,"egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")