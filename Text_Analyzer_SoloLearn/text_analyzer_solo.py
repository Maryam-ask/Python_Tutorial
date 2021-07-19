filename = input ("Enter a filename: ")

with open(filename) as f:
    text = f.read()

print(text)

# --------------------------------------------------
def count_char(txt, char):
    count = 0

    for c in txt:
        if c == char:
            count += 1

    return count


filename = input("Enter a filename: ")

with open(filename) as f:
    text = f.read()


print(count_char(text, "r"))

# ***************************************************************

