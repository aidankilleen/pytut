# function_investigation.py
# By: Aidan
# Date: 9/9/2022

def add(a, b):
    return a + b

x = 100 
y = 200

print (f"{ x } + { y } = { add(x,y) }")

def greeting(name):
    print (f"Welcome {name} ")


people = ["Alice", "Bob", "Carol", "Dan"]

for person in people:
    greeting(person)


name = "Aidan"
greeting(name)
name = "Emily"
greeting(name)






