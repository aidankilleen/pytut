# tk_bouncing_ball.py
# By: Aidan
# Date: 4/11/2022

from tkinter import messagebox
from tkinter import *


root = Tk()
root.title("Bouncing Ball")
root.geometry("600x400")
root.resizable(True, True)

width = 600
height = 400

canvas = Canvas(root, width=width, height=height, bg="blue")
canvas.pack()

x = 300
y = 200
radius = 5

ball = canvas.create_oval(x, y, x+(radius*2), y+(radius*2), fill="black")

timeout = 3

xdir = 3
ydir = 2

def timer():

    global xdir, ydir
    coords = canvas.coords(ball)

    if coords[1] > height-(radius*2):
        ydir = -ydir
    elif coords[0] > width-(radius*2):
        xdir = -xdir
    elif coords[1] <= 0:
        ydir = -ydir
    elif coords[0] <= 0:
        xdir = -xdir
    canvas.move(ball, xdir, ydir)
    root.after(timeout, timer)

root.after(timeout, timer)

root.mainloop()
