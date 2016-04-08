"""
Objekty v okenni aplikaci
"""

from Tkinter import *

# Hlavni okno se jmenuje 'root'
root = Tk()
root.title("Frame and Canvas (Ramec a Kreslici platno)")
root.geometry("800x600")

# initializace globalnich promennych, konstant
WIDTH = 600
HEIGHT = 600

# Pomocne funkce

# Event handlers


# VYRVORENI a REGISTRACE OBJEKTU HLAVNIHO OKNA
# Vytvoreni ramce = Frame
frame = Frame(root, bd = 2, width=200, height = HEIGHT, bg = "Red")
frame.grid(row = 0, column = 0)

# Vytvoreni objektu ramce Label (Labels, Buttons,...)
text_label = Label(frame, text="Label text", fg = "Blue", bg = "Red", font="Verdana 12")
text_label.place(relx=0, rely=0, x=2, y=2, anchor=NW)

# Vytvoreni kresliciho platna = Canvas
canvas = Canvas(root, width=WIDTH, height=WIDTH, bd=0, bg ="White")
canvas.grid(row = 0, column = 1)

# Vytvoreni objektu kresliciho platna oval (dalsi tvary: line, rectangle, oval, text...)
box = (100,250,300,350)
telo = canvas.create_rectangle(box,fill = "Violet")

box = (300, 250, 370, 300, 300, 350)
hlava = canvas.create_polygon(box, fill = "Red")

canvas.create_line(100, 350, 70, 400, fill = "Black", width = "5")
canvas.create_line(100, 350, 130, 400, fill = "Black", width = "5")
canvas.create_line(300, 350, 270, 400, fill = "Black", width = "5")
canvas.create_line(300, 350, 330, 400, fill = "Black", width = "5")
canvas.create_line(100, 250, 70, 220, fill = "Black", width = "5")
canvas.create_oval(310, 270, 320, 290, fill = "Blue")
canvas.create_text(200,300,text="Pig John", fill = "Dark Green", font = ("Comic Sans MS", 32))

# SPUSTENI Oknove aplikace
root.mainloop()
