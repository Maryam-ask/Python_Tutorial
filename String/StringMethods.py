"""
Format method:
format() --->   takes the passed arguments, formats them,
 and places them in the string where the placeholders {} are
"""
age = 26
text = "My name is Maryam & I am {} years old"
formatedText = text.format(age)
print(formatedText)

print("*****************************************")

a1 = 24
a2 = 28.5
a3 = 2
text2 = "I bought {} pieces of product number {} which cost {}"
formatedText2 = text2.format(a3, a1, a2)
print(formatedText2)

print("*****************************************")

# Mitavan hata baraye etminan az tartibe doroste estefade az format dakhele {} shomare index ya tartibe delkhah ra
# bezarim

i0 = 12
i1 = 43.96
i2 = 52.054
text3 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(text3.format(i0, i1, i2))

print("*****************************************")

"""
Escape Character: \
\"  Double Quote 
\' 	Single Quote 	
\\ 	Backslash 	
\n 	New Line 	
\r 	Carriage Return 	
\t 	Tab 	
\b 	Backspace 	
\f 	Form Feed 	
\ooo 	Octal value 	
"""
matn = "Salam, man Maryam hastam. \nMan \"András\" ra dost daram"
print(matn)

t = "Harry potter"
t_count = str(t.__len__())
t_first = t[0]
print(t_first + t_count)
