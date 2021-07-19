price = 49
txt = "The price is {} dollars"
print(txt.format(price)) # format() jaye {} por mikonad

# ***************************************************************
txt1 = "The price is {:.2f} dollars" # ta 2 adade ashar bad ra neshan dahad.

# ***************************************************************
# Multiple Values
quantity = 3
itemno = 567
price =49
myorder = "I want {} prices of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# ***************************************************************
# index Number:
count = 4
itemNo = 5678
price1 = 59
ordertxt = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(ordertxt.format(count, itemNo, price1))

# ***************************************************************
age = 38
name = "András"
message = "My love is {1}. {1} is {0} years old."
print(message.format(age,name))

# ***************************************************************
# Named Indexes:
my_order = "I have a {car_name}, it is a {model_name}."
print(my_order.format(car_name = "Ford", model_name = "Mustang"))