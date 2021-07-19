nameList = ["Maryam", "Nadia", "Sara", "Mohammad", "Nili", "Nasser", "Farah", "Marzieh"]
newList = []

for x in nameList:
    if "m" in x:
        newList.append(x)
print(newList)

# Kholaseye khathaye bala:
newList = [x for x in nameList if "M" in x]
print(newList)

# Yek Iterator baraye anke tamame horof ra bozorg konad.
newNameList = [name.upper() for name in nameList]
print("\n",newNameList)

# *************************************************************
fruitList = ["Apple", "Banana", "Mango", "Orange", "Chary"]
newFruitList = [x for x in fruitList if x != "Banana"]
print("\n",newFruitList)

newList = ["Potato" for x in fruitList] # Bejaye tamame item ha dar list "potato" migozarad.
print("\n",newList)

newFruitList2 = [fruit if fruit != "Banana" else "Orange" for fruit in fruitList]
print("\n",newFruitList2)

print("****** Iterable ********")
newList = [x for x in range(10)]
print(newList) # Adade beine 0 ta 10 ra neshan midahad

numberList = [i for i in range(10) if i < 6]
print("\n",numberList)