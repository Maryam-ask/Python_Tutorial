# The while Loop:
i = 1
while i < 6:
    print(i)
    i += 1

# **************************************************************
print(" EXAMPLE 2: ")

# The break statement:
j = 1
while j < 6:
    print(j)
    if j == 3:
        break
    j += 1

# **************************************************************
print(" EXAMPLE 3: ")

# The continue statement:
z = 0
while z < 6:
    z += 1
    if z == 3:
        continue
    print(z)

# **************************************************************
print(" EXAMPLE 4: ")

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true.
p = 1
while p < 6:
    print(p)
    p += 1
else:
    print("p is no longer less than 6.")


# **************************************************************
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        print("Skipping 3")
        continue