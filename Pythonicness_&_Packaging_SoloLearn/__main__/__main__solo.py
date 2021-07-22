def function():
    print("This is a module function")


if __name__ == "__main__":
    print("This is a script")

# When the Python interpreter reads a source file, it executes all of the code it finds in the file.
# Before executing the code, it defines a few special variables.
# For example, if the Python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value "__main__".
# If this file is being imported from another module, __name__ will be set to the module's name.

