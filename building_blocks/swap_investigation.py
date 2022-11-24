# swap_investigation.py
# By: Aidan
# Date: 13/09/2022


from re import A


a = 100
b = 20

print(f"a={ a } b={ b }")
# swap the two variables

temp = b
b = a
a = temp

print(f"a={ a } b={ b }")


# you can acutally swap them back using tuples:

(a, b) = (b, a)
print(f"a={ a } b={ b }")








