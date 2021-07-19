# Format the Result:
import Python_Convert_Json
import json

p = Python_Convert_Json.person
print(json.dumps(p, indent=4)) # Use the indent parameter to define the numbers of indents


print("************************************************************")
print(json.dumps(p, indent=4, separators=(".", "=")))


# order the Result:
print("************************************************************")
print(json.dumps(p, indent=2, sort_keys=True)) # Use the sort_keys parameter to specify if the result should be sorted or not
# alphabetic sorting
