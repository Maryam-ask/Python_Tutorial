None
print(None)

print(None == None)

# *******************************************
# The None object is returned by any function that doesn't explicitly return anything else.

def some_func():
    print("Hi!")


var = some_func() # it dosn't return anything ---Z so it is None
print(var)
