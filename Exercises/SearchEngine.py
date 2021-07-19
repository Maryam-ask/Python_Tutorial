"""
Search Engine:

You’re working on a search engine. Watch your back Google!
The given code takes a text and a word as input and passes them to a function called search().
The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

Sample Input
"This is awesome"
"awesome"

Sample Output
Word found
"""

def search(txt, wd):
    txtList = txt.split(" ")
    for x in txtList:
        if x == wd:
            return "Word found"

    return "Word not found"


text = input()
word = input()

print(search(text, word))