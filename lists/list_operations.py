# list_operations.py
# By: Aidan
# Date: 16/9/2022


list = ["zero", "one", "two", "three", "four", "five", "six"]

print (list[0])

print (len(list))

for item in list:
    print (item)

print("######################")

# you can work from the end of the list
print (list[-1]) # last item in the list
print (list[-2]) # 2nd last item in the list

# you can slice the list

print (list)

print (list[2:5]) # : is called the slice operator


print (list[:5]) # you can leave out the left hand number

print (list[5:]) # you can leave out the right hand number too

print (list[:]) # you can leave out both numbers!

# slice the whole list? - [:] makes a copy of the list

copy_list = list[:]

print (list)
print (copy_list)

copy_list[0] = "changed"

print (list)
print (copy_list)

# 

copy_list2 = list

print ("=======================")
print (list)
print (copy_list2)

copy_list2[0] = "changed"

print (list)
print (copy_list2)

# note both lists have changed because there is really only 1 list!!!!

list.append("seven")

print (list)
list.pop(0)
print (list)
list.sort()
print (list)
list.reverse()
print (list)





















