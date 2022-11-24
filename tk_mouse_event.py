# tk_mouse_event.py
# By: Aidan
# Date: 18/11/2022

from tkinter import messagebox
from tkinter import *

def on_click(event):
    #messagebox.showinfo("you clicked the mouse", f"({event.x},{event.y})")

    # ball is currently at (x, y)
    # mouse was clicked at (event.x, event.y)
    canvas.moveto(ball, event.x, event.y)

    print(event) 

root = Tk()
root.title("Mouse Events")
root.geometry("600x400")
root.resizable(True, True)

width = 600
height = 400

canvas = Canvas(root, width=width, height=height, bg="blue")
canvas.pack()

radius=10
x = 100
y = 100
ball = canvas.create_oval(x, y, x+(radius*2), y+(radius*2), fill="black")

canvas.bind("<Button-1>", on_click)

root.mainloop()