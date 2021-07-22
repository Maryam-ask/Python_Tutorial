import re

pattern = r"(\D+\d)"
# (\D+\d) matches one or more non-digits followed by a digit.

match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

if re.match(pattern," ! $?"):
    print("Match 3")


# ******************************************************************

print()
pattern_2 = r"\b(cat)\b"
# \b(cat)\b" basically matches the word "cat" surrounded by word boundaries.

if re.search(pattern_2, "THe cat sat!"):
    print("Match 1")

if re.search(pattern_2, "We s>cat<tered?"):
    print("Match 2")

if re.search(pattern_2, "We scattered."):
    print("Match 3")