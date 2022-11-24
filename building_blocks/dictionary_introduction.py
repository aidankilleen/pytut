# dictionary_introduction.py
# By: Aidan
# Date: 9/9/2022

list = [1,2,3]

print (list[1])

car = {
    "make": "Nissan", 
    "model": "Micra", 
    "colour": "Blue"
}

print (car["model"])
print (car["make"])
print (car["colour"])

car["year"] = 2016

print (car.items())
print (car.keys())

for key in car.keys():
    print (f"{ key } = { car[key] }")
