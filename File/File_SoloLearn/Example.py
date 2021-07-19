"""
Book Titles:

You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.

For example, if the books.txt file contains:
Some book
Another book

Your program should output:
S9
A12
"""

file = open("D:\Python_Home\Files\Books.txt", "r")
file_list = file.readlines()


for f in file_list:

    firs_letter = f[0]

    if ( f != file_list[len(file_list)-1]):
        letter_count = len(f) - 1


    else:
        letter_count = len(f)

    result = firs_letter + str(letter_count)
    print(result)

file.close()