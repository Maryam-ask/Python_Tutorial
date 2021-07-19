import re

pattern = r"[eaiou]"
# The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.

if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")

# *************************************************
print("************************************************")

pattern_2 = r"[A-Z][A-Z][0-9]"
# matches strings that contain two alphabetic uppercase letters followed by a digit.


if re.search(pattern_2, "LS8"):
    print("Match 1")

if re.search(pattern_2, "E3N"):
    print("Match 2")

if re.search(pattern_2, "1ab"):
    print("Match 3")

# *************************************************
print("************************************************")

pattern_3 = r"[^A-Z]"
# The pattern [^A-Z] excludes uppercase strings.
# Note, that the ^ should be inside the brackets to invert the character class.

if re.search(pattern_3, "this is all quiet"):
    print("Match 1")

if re.search(pattern_3, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern_3, "THISISALLSHOUTING"):
    print("Match 3")