"""
Longest Word:

Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
"""


def count_char(txt):
    counter = 0
    i = 0
    while (i < len(txt)):
        counter +=1
        i += 1


    return counter


text = input("Enter your text: ")

txt_list = text.split(" ")
bigger_word = txt_list[0]

for i in range(1, len(txt_list)):
    if count_char(bigger_word) < count_char(txt_list[i]):
        bigger_word = txt_list[i]


print(bigger_word)
