# conditional.py
# By: Aidan
# Date: 2/9/2022

from random import randint

r = randint(1, 100)

if r < 30:
    print (f"{r} is small")
elif r < 70:
    print (f"{r} is medium")
else: 
    print (f"{r} is large")

