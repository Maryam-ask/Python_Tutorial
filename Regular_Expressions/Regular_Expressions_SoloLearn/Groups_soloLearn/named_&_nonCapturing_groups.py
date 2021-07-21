import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")

if match:
    print(match.groups("first"))
    print(match.groups())


# ******************************************************************

pattern_2 = r"(a)(b(?:c)(d)(?:e))"

print(len(match.groups()))