file = open("filename.txt", "r")

cont = file.read()
print(cont)

file.close()
# This will print all of the contents of the file "filename.txt".

# ****************************************************
file = open("filename.txt", "r")

print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())

file.close()

# ****************************************************
file = open("filename.txt", "r")

file.read()

print("Re-reading")

print(file.read())

print("Finished")

file.close()

# ****************************************************
file = open("filename.txt", "r")

print(file.readlines())
file.close()

# You can also use a for loop to iterate through the lines in the file:
file = open("filename.txt", "r")
for line in file:
    print(line)
file.close()