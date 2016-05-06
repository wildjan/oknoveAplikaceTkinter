"""
Micky v okenni aplikaci
"""

from Tkinter import *
from classRectangle import *
import random

# Hlavni okno se jmenuje 'root'
root = Tk()
root.title("Ball application")
root.geometry("800x600")

# initializace globalnich promennych, konstant
WIDTH = 600
HEIGHT = 600
SIDE = 40
COLORS = ("Red", "Blue", "Green", "Magenta")
ctverce = []

# Pomocne funkce
# Odstrani mrtve ctverce
def resolve_dead(ctverce):
    for idx in range(len(ctverce) - 1, -1, -1):
        if not ctverce[idx].isAlive():
            ctverce[idx].delete(canvas)
            del ctverce[idx]

def resolve_colisions(ctverce):
    for idi in range(len(ctverce) - 1):
        for idj in range(idi + 1,len(ctverce)):
            first = ctverce[idi]
            second = ctverce[idj]
            first.colide(second)

# Event handlers
def spawn_ctverec():
    posx = random.randrange(SIDE, WIDTH - SIDE)
    posy = random.randrange(SIDE, HEIGHT - SIDE)
    velx = random.randrange(-5, 5)
    vely = random.randrange(-5, 5)
    color = random.choice(COLORS)
    ctverec = Ctverec(canvas, (posx, posy), (velx, vely), SIDE, WIDTH, HEIGHT, color)
    ctverce.append(ctverec)

def quit():
    root.quit()
    root.destroy()

def tick():
    for ctverec in ctverce:
        ctverec.update()
        ctverec.draw(canvas)
    resolve_dead(ctverce)
    resolve_colisions(ctverce)
    root.after(TICKT, tick)

# VYRVORENI a REGISTRACE OBJEKTU HLAVNIHO OKNA
# Vytvoreni ramce = Frame
frame = Frame(root, bd = 2, width=200, height = HEIGHT)
frame.grid(row = 0, column = 0)

# Vytvoreni objektu ramce Label (Labels, Buttons,...)
text_label = Label(frame, text="Vypust mic", fg = "Blue", font="Verdana 12")
text_label.grid(row = 0, column = 0, pady = 10)

spawn_button = Button(frame, text ="Spawn ball!", command = spawn_ctverec, width = 14)
spawn_button.grid(row = 1, column = 0, pady = 30)

quit_button = Button(frame, text ="Quit", command = quit, width = 14)
quit_button.grid(row = 3, column = 0)

# Vytvoreni kresliciho platna = Canvas
canvas = Canvas(root, width=WIDTH, height=WIDTH, bd=0, bg ="Yellow")
canvas.grid(row = 0, column = 1)

# Vytvoreni timeru
timer = root.after(TICKT, tick)

# SPUSTENI Oknove aplikace
root.mainloop()

