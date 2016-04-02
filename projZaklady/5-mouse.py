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
text = "Klikni do kruhu "
pokusy = 0
zasahy = 0
stred = (300, 300)
polomer = 50
box = (stred[0] - polomer,stred[1] - polomer,stred[0] + polomer,stred[1] + polomer)
barva = "Red"

# Pomocne funkce
def format_score(zasahy, pokusy):
    return "Score: " + str(zasahy) + "/ " + str(pokusy)

def jeZasah(mouse):
    if (mouse[0] - stred[0]) ** 2 + (mouse[1] - stred[1]) ** 2 <= polomer ** 2:
        return True
    else:
        return False

# Mouse left-click event handler
def click(mouse):
    global pokusy, zasahy, barva
    click_pos = (mouse.x, mouse.y)
    pokusy += 1
    if jeZasah(click_pos):
        zasahy += 1
        barva = "Red"
    else:
        barva = "Blue"
        
    text = "Kliknuto na " + str(click_pos[0]) + ":" + str(click_pos[1])
    canvas.itemconfig(status_text, text = text)
    text = format_score(zasahy, pokusy)
    canvas.itemconfig(score_text, text = text)
    canvas.itemconfig(kruh, fill = barva)

# Vytvoreni kresliciho platna = Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bd=0, bg ="White")
canvas.grid(row = 0, column = 0)

# Vytvoreni objektu kresliciho platna- oval, text
kruh = canvas.create_oval(box,fill = barva)
status_text = canvas.create_text(300, 30, text = text, font = "Verdana 24", fill = "Green")
score_text = canvas.create_text(300, 60, text = format_score(0,0), font = "Verdana 24", fill = "Green")

# Registrace udalosti 'kliknuti levym tlacitkem mysi', vola mouse handler
canvas.bind("<Button-1>", click)

# SPUSTENI Oknove aplikace
root.mainloop()

