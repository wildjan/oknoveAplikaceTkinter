"""
Tlacitka a zmena atributu objektu
Button, item_config()
"""

from Tkinter import *
import math

# Hlavni okno se jmenuje 'root'
root = Tk()
root.title("Mouse-click a zmeny atributu")
root.geometry("600x600")

# initializace globalnich promennych, konstant
WIDTH = 600
HEIGHT = 600
text = "Použijte kurzorové klávesy pro pohyb kruhu"
pos = (300, 300)
polomer = 50
SPEED = 5
vel = (0, 0)
box = (pos[0] - polomer,pos[1] - polomer,pos[0] + polomer,pos[1] + polomer)
LEFT = '37'
RIGHT = '39'
UP = '38'
DOWN = '40'
KEYSMAPPING = {'37':'LEFT', '39':'RIGHT', '38':'UP', '40':'DOWN'}

# Pomocne funkce
def update(key_code):
    global pos
    if key_code in KEYSMAPPING.keys():
        text = "Poslední stisknutá klávesa " + KEYSMAPPING[key_code]
        canvas.itemconfig(status_text, text = text)
    posX, posY = pos 
    posX += vel[0]
    posY += vel[1]
    pos = posX, posY
    box = (pos[0] - polomer,pos[1] - polomer,pos[0] + polomer,pos[1] + polomer)
    canvas.coords(kruh, box)

# Define key_press events
def key_press(event):
    global vel
    key_code = repr(event.keycode)
    if key_code == UP:
        vel = (0, -SPEED)
    if key_code == DOWN:
        vel = (0, SPEED)
    if key_code == LEFT:
        vel = (-SPEED, 0)
    if key_code == RIGHT:
        vel = (SPEED, 0)
    update(key_code)

# Define key_release events
def key_release(event):
    global vel
    key_code = repr(event.keycode)
    if key_code == UP:
        vel = (0, 0)
    if key_code == DOWN:
        vel = (0, 0)
    if key_code == LEFT:
        vel = (0, 0)
    if key_code == RIGHT:
        vel = (0, 0)
    update(key_code)

# Vytvoreni kresliciho platna = Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bd=0, bg ="White")
canvas.grid(row = 0, column = 0)

# Vytvoreni objektu kresliciho platna- oval, text
kruh = canvas.create_oval(box,fill = "Blue")
status_text = canvas.create_text(300, 30, text = text, font = "Verdana 12", fill = "Green")

# Registrace udalosti 'stisknuti a uvolneni klaves ', vola mouse handler
canvas.bind("<KeyPress>", key_press)
canvas.bind("<KeyRelease>", key_release)
canvas.focus_set()

# SPUSTENI Oknove aplikace
root.mainloop()

