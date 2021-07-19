file_1 = open("D:\Python_Home\Files\demo.txt", "a") # "a" khili mohem ast baraye ghabeliate neveshtan
file_1.write("Now I add new line in the file!")
file_1.close()

# Open and read the file after the appending:
file_1 = open("D:\Python_Home\Files\demo.txt", "r")
print(file_1.read())


# ******************************************************************************************************

test_file = open("D:\Python_Home\Files\Test_write.txt", "w")
test_file.write("Woops! I am a crazy lover!")
test_file.close()

# Open and read:
test_file = open("D:\Python_Home\Files\Test_write.txt", "r")
print(test_file.read())