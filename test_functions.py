# test_functions.py
# By: Aidan
# Date: 23/9/2022

#print("====================")
#print(__name__)
#print ("========================")

def first_function():
    print ("first function")

def greeting(name):
    print (f"hello {name}")

names = ["Alice", "Bob", "Carol", "Dan", "Eve"]


# is this the main module
# or is this module being imported from another module?
if __name__ == "__main__":

    print ("this is the main application")
    first_function()
    greeting("Aidan")


    for name in names:
        greeting(name)

    # DRY - don't repeat yourself
    name = "Aidan"
    print (f"Hello {name}")
    name = "Bob"
    print (f"Hello {name}")





