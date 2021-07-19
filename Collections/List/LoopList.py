nameList = ["Maryam", "Nadia", "Mohammad", "Ali", "Nasser", "András", "Farah"]
# Manande for-each dar java mimanad:
for x in nameList:
    print(x)

print("*************************")
# Yek loop baraye inke khanehaye list ra yeki yeki bekhanad.
for i in range(len(nameList)):
    print(nameList[i])

print("******** While Loop **********")
# Ba estefade az while-loop:
i = 0
while i < len(nameList):
    print(nameList[i])
    i = i + 1

print("***** Looping Using List Comprehension *****")
# A short hand for loop that will print all items in a list:
[print(x) for x in nameList]