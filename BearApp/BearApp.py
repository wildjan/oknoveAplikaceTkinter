"""
Micky v okenni aplikaci
"""

from Tkinter import *
from classBear import *
from PIL import Image, ImageTk
import random

# Hlavni okno se jmenuje 'root'
root = Tk()
root.title("Beer or Bear?")
root.geometry("800x600")

# initializace globalnich promennych, konstant
WIDTH = 600
HEIGHT = 600
SIDE = 23
beer = Image.open(r'img\teddybeer.png')
sprite = ImageTk.PhotoImage(beer)
bear0 = Image.open(r'img\teddybear0.png')
sprite0 = ImageTk.PhotoImage(bear0)
bear1 = Image.open(r'img\teddybear1.png')
sprite1 = ImageTk.PhotoImage(bear1)
bear2 = Image.open(r'img\teddybear2.png')
sprite2 = ImageTk.PhotoImage(bear2)

BEARS = [sprite, sprite0, sprite1, sprite2]
bears = []

# Pomocne funkce
def resolve_destroyed(bears):
    """Odstrani vsechny 'vyslouzile' medvedy"""
    for idx in range(len(bears) - 1, -1, -1):
        if bears[idx].get_life() <= 0:
            bears[idx].delete(canvas)
            del bears[idx]

def resolve_colisions(bears):
    for idi in range(len(bears) - 1):
        for idj in range(idi + 1,len(bears)):
            first = bears[idi]
            second = bears[idj]
            first.colide(second)

# Event handlers
def spawn_bear():
    posx = random.randrange(SIDE, WIDTH - SIDE)
    posy = random.randrange(SIDE, HEIGHT - SIDE)
    velx = random.randrange(-5, 5)
    vely = random.randrange(-5, 5)
    bear_sprite = random.choice(BEARS)
    if bear_sprite == sprite:
        lives = 10
    else:
        lives = 5
    bear = Bear(canvas, (posx, posy), (velx, vely), WIDTH, HEIGHT, bear_sprite, lives)
    bears.append(bear)

def quit():
    root.quit()
    root.destroy()

def tick():
    for bear in bears:
        bear.update()
        bear.draw(canvas)
    resolve_destroyed(bears)
    resolve_colisions(bears)
    root.after(TICKT, tick)

# VYRVORENI a REGISTRACE OBJEKTU HLAVNIHO OKNA
# Vytvoreni ramce = Frame
frame = Frame(root, bd = 2, width=200, height = HEIGHT)
frame.grid(row = 0, column = 0)

# Vytvoreni objektu ramce Label (Labels, Buttons,...)
text_label = Label(frame, text="Vypust medu", fg = "Blue", font="Verdana 12")
text_label.grid(row = 0, column = 0, pady = 10)

spawn_button = Button(frame, text ="Spawn bear!", command = spawn_bear, width = 14)
spawn_button.grid(row = 1, column = 0, pady = 30)

quit_button = Button(frame, text ="Quit", command = quit, width = 14)
quit_button.grid(row = 3, column = 0)

# Vytvoreni kresliciho platna = Canvas
canvas = Canvas(root, width=WIDTH, height=WIDTH, bd=0, bg ="light sky blue")
canvas.grid(row = 0, column = 1)

# Vytvoreni objektu canvasu 'image'
canvas.create_image((100, 100), image = sprite)

pos = sprite0.width()/2, sprite0.height()/2
canvas.create_image(pos, image = sprite0)

# Vytvoreni timeru
timer = root.after(TICKT, tick)

# SPUSTENI Oknove aplikace
root.mainloop()

