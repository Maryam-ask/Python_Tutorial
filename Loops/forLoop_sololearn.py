# iterates over the string and calculates the count of 't' letters in it.
str = "testing for loops"
count = 0
for x in str:
    if (x == 't'):
        count += 1

print(count)

# ****************************************************************************************

"""
Range:
Python makes it super easy to create number sequences using the range() function.
By default, it starts from 0, increments by 1 and stops before the specified number.
"""
numbers = list(range(10))
print(numbers)

# ****************************************************************************************

numbers1 = list(range(3, 8)) # adade beine 3 ta 8 ra neshan midahad
print(numbers1)

# ****************************************************************************************

# It’s called Step and it determines the interval of the sequence produced.
numbers2 = list(range(5, 20, 2)) # adade beine 5 ta 20 ra 2 ta 2 ta afzayesh midahad va neshan midahad.
print(numbers2)

# ****************************************************************************************

# We can also create a list of decreasing numbers,
# using a negative number as the third argument, for example
numbers3 = (range(20, 5, -2))
print(numbers3)

# ****************************************************************************************

# Don’t worry about calling list on the range object when it is used in a for loop,
# because it isn't being indexed, so a list isn't needed.
for i in range(5):
    print("hello!")
# ****************************************************************************************
"""
List Slices:
The most basic list slicing involves indexing a list with two colon-separated integers.
This will return a new list containing all the values in the old list between the indices. 
"""
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])


# ****************************************************************************************

# If the first number in a slice is omitted, it’s taken to be the start of the list.
# If the second number is omitted, it’s taken to be the end.
squares1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares1[:7])
print(squares1[7:])


# ****************************************************************************************

# Just like with ranges, your list slices can include a third number,
# representing the step,to include only alternate values in the slice.
squares2 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares2[::2])
print(squares2[2:8:3])


# ****************************************************************************************

"""
when negative values are used for the first and second values in a slice (or a normal index),
they count from the end of the list.
"""
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1]) # Az khoneye 1 ta akhar -1 manzoor khoneye akhare.


""" !!!!! Nokte !!!!!
If a negative value is used for the step, the slice will be done backwards.
Using [::-1] as a slice is a common and idiomatic way to reverse a list.
"""
