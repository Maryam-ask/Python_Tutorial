file = open("D:\Python_Home\Files\demo.txt")
# readline() ----> Return one line by using.
# print(file.readline())
# print(file.readline())


print("*******************")
# By looping through the lines of the file, you can read the whole file, line by line:
for x in file:
    print(x)

# close file:
file.close()