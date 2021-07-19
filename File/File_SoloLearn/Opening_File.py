myfile = open("filename.txt")

#********************************************************

# write mode
open("filename.txt", "w")


# read mode
open("filename.txt", "r")
open("filename.txt")


# binary write mode
open("filename.txt", "wb")

# You can use the + sign with each of the modes above to give them extra access to files.
# For example, r+ opens the file for both reading and writing.

# ********************************************************
file = open("filename.txt", "w")

# do stuff to the file
file.close()

# We will read/write content to files in the upcoming lessons.