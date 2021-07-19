list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

# Raveshe 1
list3 = list1 + list2
print(list3)

# Raveshe 2
for x in list1:
    list2.append(x)
print(list2)

# Raveshe 3
list1.extend(list2)
print(list1)