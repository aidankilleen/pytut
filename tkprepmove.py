import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

canvas_width, canvas_height = 600, 400

x1 = 300
y1 = 200

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)

canvas.pack()

r = canvas.create_oval(x1, y1, x1+10, y1+10,width=1,fill="black")



def keypress (event):
    # messagebox.showinfo("Information", "The Message")
    print ("moving")
    x = 0
    y = 0

    if event.char == 'a': x=-10
    elif event.char == 'd': x=10
    elif event.char == 'w': y=+10
    elif event.char == 's': y=-10

    canvas.move(r, x, y)

root.bind("<Key>", keypress)

root.mainloop()


