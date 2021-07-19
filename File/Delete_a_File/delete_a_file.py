# Delete a file
import os

if os.path.exists("D:\Python_Home\Files\myfile_create.txt"):
    os.remove("D:\Python_Home\Files\myfile_create.txt")
else:
    print("the file does not exist!")


# delete a folder:
os.rmdir("D:\Python_Home\Files\My new folder")
# !!! You can only remove empty folders.