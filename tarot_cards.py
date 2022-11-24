# tarot_cards.py
# By: Aidan
# Date: 16/9/2022


suits = ["cups", "swords", "wands", "pentacles"]
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "page", "knight", "queen", "king"]

cards = ["The Fool" , 
    	"The Magician",
        "The High Priestess",
        "The Empress",
        "The Emperor",
        "The Hierophant",
        "The Lovers",
        "The Chariot" ,
        "Strength",
        "The Hermit",
        "Wheel of Fortune" ,
        "Justice",
        "The Hanged Man" ,
        "Death",
        "Temperance",
        "The Devil",
        "The Tower",
        "The Star",
        "The Moon",
        "The Sun",
        "Judgment",
        "The World"
]

for suit in suits:
    for number in numbers:
        card = f"{ number } of { suit }"
        cards.append(card)


print (cards)        

print (len(cards))