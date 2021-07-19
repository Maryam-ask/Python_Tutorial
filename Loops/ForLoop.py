# for Loop:
fruits = ["apple", "banana", "cherry"]
# print(type(fruits))
for x in fruits:
    print(x)

# ****************************************************************************
# looping through a String:
for x in "Maryam":
    print(x)

# ****************************************************************************
# break statement:
fruits1 = ["mango", "banana", "cherry", "apple", "orange"]
for i in fruits1:
    print(i)
    if i == "cherry":
        break


for j in fruits1:
    if j == "cherry":
        break
    print(j)

# ****************************************************************************
# continue statement:
students = ["Maryam", "András", "Nadia", "Mohammad"]
for s in students:
    if s == "András":
        continue
    print(s)

# ****************************************************************************
# range() Function:
for n in range(6): # beine 0 ta 6 vali khode 6 nist.
    print(n)

# !!! Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
print("Numbers between 2-8 is:")
for number in range(2,8):
    print(number)

print("Increment the sequence with 3 in range between 2-30:")
for mynum in range(2,30,3):
    print(mynum)

# ****************************************************************************
# Else in For Loop:
print("else in for-loop:")
for n1 in range(8):
    print(n1)
else:
    print("Finally finished!")


print("break and else in for-loop:")
for n2 in range(6):
    if n2 == 3: break
    print(n2)
else:
    print("Finally finished!")

# ****************************************************************************
# Nested Loops: A nested loop is a loop inside a loop:
print("Nested Loops:")
color = ["red", "blue", "white", "gray"]
cars = ["volvo", "Toyota", "Benz", "BMW"]

for y in color:
    for z in cars:
        print(y, z)

# ****************************************************************************
# The pass Statement:
for x1 in [0, 1, 2]:
    pass