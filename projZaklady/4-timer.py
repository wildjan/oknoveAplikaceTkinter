# -*- coding: utf8 -*-
"""
Timer (casovac) spousti udalost po uplynuti zadaneho casu
Zpravidla provadi akce 'update' a 'draw'
Timer ma v teto aplikaci nazev timer a vola kazdych DELTAT v ms funkci tick()
Zmena pozice se odehrava podle vzorce pos = pos + vel * dt
kde vel je rychlost a dt je zmena casu za jeden tick() (s = v * t)
Jedna se o pohyb rovnoverny a primocary
"""

from Tkinter import *

# Hlavni okno se jmenuje 'root'
root = Tk()
root.title("Timer a animace pohybu")
root.geometry("800x600")

# initializace globalnich promennych, konstant
WIDTH = 600
HEIGHT = 600
DELTAT = 100
text = "000"
time = 0
timer_is_running = True
pos = (300, 300)
vel = (0.05,0.05)
polomer = 50
box = (pos[0] - polomer,pos[1] - polomer,pos[0] + polomer,pos[1] + polomer)
barva = "Red"

# Pomocne funkce
def update():
    global pos
    canvas.itemconfig(time_text, text = str(time))
    posX, posY = pos 
    posX += vel[0] * DELTAT
    posY += vel[1] * DELTAT
    pos = posX, posY
    box = (pos[0] - polomer,pos[1] - polomer,pos[0] + polomer,pos[1] + polomer)
    canvas.coords(kruh, box)

# EVENT HANDLERS
# Timer handler
def tick():
    global time, time_is_running
    update()
    #draw()
    if timer_is_running:
        time += 1
        root.after(DELTAT, tick)

# Button handler
def quit():
    root.quit()
    root.destroy()

# VYTVORENI a REGISTRACE OBJEKTU HLAVNIHO OKNA
# Vytvoreni ramce = Frame
frame = Frame(root, bd = 2, width=200, height = HEIGHT)
frame.grid(row = 0, column = 0)

# Vytvoreni objektu ramce (Labels, Buttons,...)
text_label = Label(frame, text=u"Stiskni 'Quit' pro ukončení", fg = "Blue", font="Verdana 12")
text_label.grid(row = 0, column = 0)

quit_button = Button(frame, text ="Quit", command = quit, width = 14)
quit_button.grid(row = 1, column = 0)

# Vytvoreni kresliciho platna = Canvas
canvas = Canvas(root, width=WIDTH, height=WIDTH, bd=0, bg ="White")
canvas.grid(row = 0, column = 1)

# Vytvoreni objektu kresliciho platna- oval a text pro zobrazeni casu na Canvasu!
kruh = canvas.create_oval(box,fill = barva)
time_text = canvas.create_text(160, 30, text = "000", font = "Verdana 24", fill = "Green")

# Vytvoreni a registrace timeru DELTAT je prodleva, tick je obsluzna funkce (handler) 
timer = root.after(DELTAT, tick)

# SPUSTENI Oknove aplikace
root.mainloop()

