# Match Object:
import re
txt = "The rain in Spain"

m1 = re.search("ain", txt)
print(m1) # this will print an object

# Print the position (start- and end-position) of the first match occurrence.
m2 = re.search(r"\bS\w+", txt)
# Search for an upper case "S" character in the beginning of a word, and print its position:
print(m2.span()) # The regular expression looks for any words that starts with an upper case "S".


# The string property returns the search string:
print(m2.string)


# Search for an upper case "S" character in the beginning of a word, and print the word:
print(m2.group())

