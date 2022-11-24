# string_operations.py
# By: Aidan
# Date: 16/9/2022


from re import S


s = "abcdefghijklmnopqrstuvwxyz"


print (s[0])
print (s[1])

print (len(s))

for c in s:
    print (c)

print (s[-1])
print (s[-2])

print (s[5:10])

print (s[:5])
print (s[5:])

cp = s

cp = s[:] # this is a true copy

print (s[:])

rev = s[::-1]

print (rev)




