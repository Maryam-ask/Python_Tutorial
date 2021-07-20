import re

pattern = r"9{1,3}$"
# "9{1,3}$" matches string that have 1 to 3 nines.

if re.match(pattern, "9"):
    print("Match 1")

if re.match(pattern, "999"):
    print("Match 2")

if re.match(pattern, "9999999"):
    print("Match 3")