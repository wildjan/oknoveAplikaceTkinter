"""
Tlacitka a zmena atributu objektu
Button, item_config()
"""

from Tkinter import *

# Hlavni okno se jmenuje 'root'
root = Tk()
root.title("Tlacitka a zmeny atributu")
root.geometry("800x600")

# initializace globalnich promennych, konstant
WIDTH = 600
HEIGHT = 600
text = "Pocet = "
citac = 0
pozice = 100
polomer = 50
box = (pozice - polomer,pozice - polomer,pozice + polomer,pozice + polomer)
barva = "Red"

# Pomocne funkce
def format_text(citac):
    return "Pocet = " + str(citac)

# Event handlers
def press():
    global pozice, citac, barva
    citac += 1
    text = format_text(citac)
    text_label.config(text = text)
    pozice += 5
    box = (pozice - polomer, pozice - polomer, pozice + polomer, pozice + polomer)
    if barva == "Red":
        barva = "Blue"
    else:
        barva = "Red"
    canvas.itemconfig(kruh, fill = barva)
    canvas.coords(kruh, box)

# VYRVORENI a REGISTRACE OBJEKTU HLAVNIHO OKNA
# Vytvoreni ramce = Frame
frame = Frame(root, bd = 2, width=200, height = HEIGHT)
frame.grid(row = 0, column = 0)

# Vytvoreni objektu ramce (Labels, Buttons,...)
text_label = Label(frame, text=text, fg = "Blue", font="Verdana 12")
text_label.grid(row = 0, column = 0)

click_button = Button(frame, text ="Klikni!", command = press, width = 14)
click_button.grid(row = 1, column = 0)

# Vytvoreni kresliciho platna = Canvas
canvas = Canvas(root, width=WIDTH, height=WIDTH, bd=0, bg ="White")
canvas.grid(row = 0, column = 1)

# Vytvoreni objektu kresliciho platna- oval
kruh = canvas.create_oval(box,fill = barva) 

# SPUSTENI Oknove aplikace
root.mainloop()

