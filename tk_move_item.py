# tk_move_item.py
# By: Aidan
# Date: 4/11/2022

from tkinter import messagebox
from tkinter import *


root = Tk()
root.title("Move Using Keyboard")
root.geometry("600x400")
root.resizable(True, True)

canvas = Canvas(root, width=600, height=400, bg="Green")
canvas.pack()

x = 300
y = 200

ball = canvas.create_oval(x, y, x+10, y+10, fill="black")

def handle_keypress(event):

    # print (event)
    dx = 0
    dy = 0

    # messagebox.showinfo("Message", "key pressed")
    if event.keysym == "Right":
        dx = 10    
    elif event.keysym == "Left":
        dx = -10
    elif event.keysym == "Up":
        dy = -10
    elif event.keysym == "Down":
        dy = 10

    canvas.move(ball, dx, dy)

    print (canvas.coords(ball))

root.bind("<Key>", handle_keypress)


root.mainloop()



