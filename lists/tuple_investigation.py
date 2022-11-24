# tuple_investigation.py
# By: Aidan
# Date: 13/09/2022

list = [1, 4, 3, 7, 10]
t = (1, 4, 3, 7, 10)

print(list[0])
print(t[0])

for i in list:
    print (i)

for i in t:
    print(i)

list[0] = 999
# t[0] = 999 - not allowed

# 1. a Tuple is read-only


def do_calculations(list):

    max = list[0]
    min = list[0]
    
    for item in list:
        if item > max:
            max = item

        if item < min:
            min = item

    return (max, min)

result = do_calculations([5, 3, 7, 1, 100, 87, 65, 33])    

print (list)
print (result)

print(f"max={result[0]}")
print(f"min={result[1]}")














