# Try to open and write to a file that is not writable.
try:
    f = open("demo.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()