import re

str = "My name is Maryam. Hi Maryam."
pattern = r"Maryam"

newstr = re.sub(pattern, "Nadi", str)  #Be jaye hameye "Maryam" ha "Nadi" migozarad
print(newstr)


# *************************************************************************

num = "07987549836"
pattern_2 = r"9"

new_num = re.sub(pattern_2, "00", num)

print(new_num)