import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))

# In the example above, the match function did not match the pattern, as it looks at the beginning of the string.
# The search function found a match in the string.

# ********************************************************************************************************************
print()

pattern_2 = r"pam"

match = re.search(pattern_2, "eggspamsausage")

if match:
    print(match.group())    # which returns the string matched
    print(match.start())    # which return the start position of the first match
    print(match.end())      # which return the ending position of the first match
    print(match.span())     # which returns the start and end positions of the first match as a tuple