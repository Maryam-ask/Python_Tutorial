thisdict={
    "name": "Mary",
    "family": "Askari",
    "age": 27,
    "study": "AI",
    "country": "Sweden"
}

for x, y in thisdict.items():
    print(x, y)

for x in thisdict:
    print(x) # tamame key hara neshan midahad.


for x in thisdict:
    print(thisdict[x]) # value hara neshan midahad.


for x in thisdict.keys():
    print(x)


for x in thisdict.values():
    print(x)

