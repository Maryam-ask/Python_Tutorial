import re

phone_number = input()

pattern = r"^(1|8|9)+[0-9]{7}$"


if re.match(pattern, phone_number):
  print("Valid")
else:
  print("Invalid")