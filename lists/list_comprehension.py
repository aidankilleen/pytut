# list_comprehension.py
# By: Aidan
# Date: 16/9/2022


suits = ["cups", "swords", "wands", "pentacles"]
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "page", "knight", "queen", "king"]



list = [1, 6, 3, 8, 9, 10, 2, 5]

even_numbers = []

for item in list:
    if item % 2 == 0:  # remainder when dividing by 2 is 0 => this is an even number
        even_numbers.append(item)

print (even_numbers)

even_list = [item for item in list if item % 2 == 0]
odd_list = [item for item in list if item % 2 == 1]

print (even_list)
print (odd_list)












