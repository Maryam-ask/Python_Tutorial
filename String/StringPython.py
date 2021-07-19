# both 'hello' and "hello" are the same
print('hello')
print("hello")

# mitavanim hamzaman chandta string baham vared konim vali bayad ---> 3 ta quote bezarim

a = """Maryam Python mikhanad,
Nadia corona gerefte ast,
Mohammad pesare khobi ast."""
print(a)

# *****************************************************************************
"""
dar Python String manande array amal mikonad.
mitavanim khanehaye an string ra be sorate array seda bezanim manande mesale zir:
"""
b = "Marzieh"
print(b[1])
print(b[0])

# baraye khandane horoofe marzieh mitavan az for loop estefade kard:
print("****** Estefade az for loop *****")
for x in b:
    print(x)

# Baraye gereftane size String ----> len()
print("**** Estefade az len() ****")
a = "Hello"
print(len(a))

# Baraye peidakardane ye Character da ye String
print("**** in *****")
text = "Maryam dokhtare khobi ast."
print("khobi" in text)  # ----> in ---> be ma boolean midahad.

# ye tamrin ba if va in :
matn = "Maryam dar sweden zendegi mikonad"
if "sweden" in matn:
    print("yes, Maryam dar sweden ast")

# **************************** NOT IN
print("**** NOT IN *****")
text1 = "Nadia corona gerefte ast."
print("Maryam" not in text1)  # ---> agar nabashad treue midahad
print("Nadia" not in text1)

# ***************************
# Baraye khandane characterha dar yek range moshakhas:
print("**** A range of characters ****")
b = "Salam Donya!!!!!"
print(b[3:5])  # khaneye 3 va 4 ra midahad
print(b[:7])  # az ebteda ta khaneye 7 vali khode 7 hesab nist
print(b[2:])  # az khaneye 2 ta akhrin khane
print(b[-8:-2])  # 8-2 = 6 ---> 6 ta khaneye akhar ra neshan midahad

# ************************************
print("**** UPPER CASE ****")
b1 = "khanom khoshkel"
print(b1.upper())

print("**** LOWER CASE ****")
b2 = "MARYAM banoo"
print(b2.lower())

# ****************************
# Baraye hazf kardane Space ezafeye ebteda va enteha
print("*** removing space from start and end of the String ***")
a1 = "  Donya Zibast!!   "
print(a1.strip())

# ********************************
# Baraye replace kardane yek harf ba harfe digar ---- method ---> replace()
print("***** replace() for replacing one charachter or string with another one ******")
m = "Hello World!"
print(a.replace("H", "mary"))

# ********************************
# for spliting a String ----> split() -----> Methode split() yek Array bar migardanad.
print("******* split() ********")
i = "Salam Donya"
print(i.split(" "))  # split() ---> ye array bar migardanad az space" " joda mikonad va dar array mirizad

# **********************************
# some funny exercises:

a = "Maryam"
b = "András"
c = a + b
print(c)

c1 = a + " & " + b
print(c1)