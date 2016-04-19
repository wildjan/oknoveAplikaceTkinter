"""
Micky v okenni aplikaci
"""

from Tkinter import *
from classBall import *
import random

# Hlavni okno se jmenuje 'root'
root = Tk()
root.title("Frame and Canvas (Ramec a Kreslici platno)")
root.geometry("800x600")

# initializace globalnich promennych, konstant
WIDTH = 600
HEIGHT = 600
RADIUS = 20
COLORS = ("Red", "Blue", "Green", "Magenta", "Black")
balls = []

# Pomocne funkce
def resolve_colisions(balls):
    for idi in range(len(balls) - 1):
        for idj in range(idi + 1,len(balls)):
            first = balls[idi]
            second = balls[idj]
            first.colide(second)

# Event handlers
def spawn_ball():
    posx = random.randrange(RADIUS, WIDTH - RADIUS)
    posy = random.randrange(RADIUS, HEIGHT - RADIUS)
    velx = random.randrange(-5, 5)
    vely = random.randrange(-5, 5)
    color = random.choice(COLORS)
    ball = Ball(canvas, (posx, posy), (velx, vely), RADIUS, WIDTH, HEIGHT, color)
    balls.append(ball)

def quit():
    root.quit()
    root.destroy()

def tick():
    for ball in balls:
        ball.update()
        ball.draw(canvas)
    resolve_colisions(balls)
    root.after(TICKT, tick)

# VYRVORENI a REGISTRACE OBJEKTU HLAVNIHO OKNA
# Vytvoreni ramce = Frame
frame = Frame(root, bd = 2, width=200, height = HEIGHT)
frame.grid(row = 0, column = 0)

# Vytvoreni objektu ramce Label (Labels, Buttons,...)
text_label = Label(frame, text="Vypust mic", fg = "Blue", font="Verdana 12")
text_label.grid(row = 0, column = 0, pady = 10)

spawn_button = Button(frame, text ="Spawn ball!", command = spawn_ball, width = 14)
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

