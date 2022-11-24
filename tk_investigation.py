# tk_investigation.py
# By: Aidan
# Date: 21/10/2022

from tkinter import *
from tkinter import messagebox
import time
from random import randint

colours = ["red", "green", "blue", "orange", "yellow", "black", "purple", "violet", "white"]
def on_click():
    #messagebox.showinfo("Information", "The Message")
    x = randint(0, 500)
    y = randint(0, 400)
    d = randint(10, 50)
    t = randint(1, 5)

    c = randint(0, len(colours)-1)


    canvas.create_oval(x, y, x+d, y+d, width=t, fill=colours[c])

root = Tk()
root.title("Game Window")
root.geometry("600x400")
root.resizable(0, 0)

canvas = Canvas(root, width=500, height=500, bg="White")
canvas.pack(fill=BOTH, expand=True)

label = Label(canvas, text="Test Label")
label.pack(pady=20)

button = Button(canvas, text="Press Me", command=on_click)
button.pack()

#canvas.create_oval(100, 100, 200, 200, width=3)

#canvas.create_line(0, 0, 100, 250)

#canvas.create_rectangle(300, 200, 400, 300, fill="orange",outline='blue', width=3)

#canvas.create_text(100, 50, text="Is this working?")

#for x in range (10, 100, 10):
#    canvas.create_rectangle(100 + x, 100 + x, 400 - x, 400 - x, fill="red")




root.update()

root.mainloop()


