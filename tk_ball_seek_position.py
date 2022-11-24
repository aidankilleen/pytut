# tk_mouse_event.py
# By: Aidan
# Date: 18/11/2022

from tkinter import messagebox
from tkinter import *

def on_click(event):
    #messagebox.showinfo("you clicked the mouse", f"({event.x},{event.y})")

    # ball is currently at (x, y)
    # mouse was clicked at (event.x, event.y)
    global xdir, ydir
    global desired_x, desired_y

    coords = canvas.coords(ball)
    current_x = coords[0]
    current_y = coords[1]


    desired_x = event.x
    desired_y = event.y

    # figure out xdir and ydir to get from here to desired location
    if current_x < desired_x:
        xdir = (desired_x-current_x)/10
    
    if current_x > desired_x:
        xdir = -(current_x-desired_x)/10

    if current_y < desired_y:
        ydir = (desired_y-current_y)/10

    if current_y > desired_y:
        ydir = -(current_y-desired_y)/10

    print(f"move to ({desired_x}, {desired_y})")

    #canvas.moveto(ball, event.x, event.y)


def timer():

    global current_x, current_y
    global desired_x, desired_y
    global xdir, ydir

    coords = canvas.coords(ball)
    current_x = coords[0]
    current_y = coords[1]
    print (f"{current_x} {desired_x} {xdir}")
    if xdir > 0 and current_x >= desired_x:
        xdir = 0
    if xdir < 0 and current_x <= desired_x:
        xdir = 0        

    if ydir > 0 and current_y >= desired_y:
        ydir = 0

    if ydir < 0 and current_y <= desired_y:
        ydir = 0

    #if current_x != desired_x and current_y != desired_y:
    canvas.move(ball, xdir, ydir)
    root.after(timeout, timer)

root = Tk()
root.title("Ball Seek Position")
root.geometry("600x400")
root.resizable(True, True)

width = 600
height = 400

canvas = Canvas(root, width=width, height=height, bg="blue")
canvas.pack()

radius=10
current_x = 100
current_y = 100

desired_x =0
desired_y =0

xdir = 0
ydir = 0

ball = canvas.create_oval(current_x, current_y, current_x+(radius*2), current_y+(radius*2), fill="black")

canvas.bind("<Button-1>", on_click)

timeout = 1000

root.after(timeout, timer)

root.mainloop()