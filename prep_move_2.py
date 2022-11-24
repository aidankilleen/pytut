import tkinter as tk

root = tk.Tk()
WIDTH = HEIGHT = 400
x1 = y1 = WIDTH / 2
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
c1 = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10)
canvas.create_text((100,10), text="Move with a,d,w,s")
left, right, up, down = -10,10,-10,10
key = {}
key["a"] = -10
key["d"] = 10
key["w"] = -10
key["s"] = 10
def keypress(event):
  """If you go down or right increase
     If you go left of up decrease"""
  x = 0
  y = 0

  ad = event.char == "a" or event.char == "d"
  ws = event.char == "w" or event.char == "s"
  if ad:
    x = key[event.char]
  if ws:
    y = key[event.char]
  canvas.move(c1, x, y)


root.bind("<Key>", keypress)
root.mainloop()