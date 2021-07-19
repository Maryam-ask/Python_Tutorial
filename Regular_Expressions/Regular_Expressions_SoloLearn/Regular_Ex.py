import re

pattern = r"spam"

if re.match(pattern,"spamspamspam"):
    print("Match")
else:
    print("No match")

# The above example checks if the pattern "spam" matches the string and prints "Match" if it does.
