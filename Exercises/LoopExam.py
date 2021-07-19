x = int(input("Enter your number"))
i = 1
while i <= x:
    print("*" * i)
    i += 1


# **********************************'
print("next example!")
num = int(input("Enter your number?"))
i = num
while i > 0 :
    print("*" * i)
    i -= 1

# **********************************'

number1 = int(input("Enter your number?"))
j = number1
count = 0
while j > 0:
    print(" "* count + "*" * j)
    j -=1
    count +=1

# **********************************'
number2 = int(input("Yek adade fard vared konid"))
c = (number2 // 2) + 1
a = 1
while a <= number2:
    if a == c:
        print("*" * ((c*2)-1))
    else:
        print(" " * (c-1) + "*")
    a += 1

# **********************************'
print("Rasme moraba ba \'*\' :")
myNum = int(input("Enter your number? "))
b = 1
while b <= myNum:
    if b == myNum:
        print("*" * b)
    elif b == 1:
        print("*" * myNum)
    else:
        print("*" + " " * (myNum-2) + "*")
    b +=1