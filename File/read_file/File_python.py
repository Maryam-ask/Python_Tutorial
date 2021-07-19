# the open() ----> returns file object ---> which has a read() method.
file = open("D:\Python_Home\Files\demo.txt", "r")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
print(file.read())


# Return the 5 first characters of the file:
print(file.read(5))