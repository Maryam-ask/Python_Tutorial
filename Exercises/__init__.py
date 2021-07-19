"""
Sum of Consecutive Numbers:
No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.
Let’s save some time by creating a program to do the calculation for you!
Take a number N as input and output the sum of all numbers from 1 to N (including N).

Sample Input
100

Sample Output
5050
"""

N = int(input())
#your code goes here
all = list(range(1,N+1))
count = 0
for i in all:
    count += i

print(count)