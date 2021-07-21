import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print("Matched 'gray'")

match = re.match(pattern, "grey")
if match:
    print("Matched 'grey'")

match = re.match(pattern, "griy")
if match:
    print("Matched 'griy'")