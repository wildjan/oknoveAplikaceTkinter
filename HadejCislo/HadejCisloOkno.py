# -*- coding: utf8 -*-
# Šablona pro "Hádej číslo" mini-project
# vstup je prostřednictvím vstupního pole a tlačítka
# výstup hry je vytištěn na konzoli

# Program generuje náhodné číslo od 1 do 10 (100, 1000 = horni)
# Začněte s číslem od 1 do 10 pro snadnější ladění
# Maximální počet pokusů se určí: log2(horni)

from Tkinter import *
root = Tk()
root.title(u"Hádej číslo")
root.geometry("450x300")

import random, math

# initializace globalnich promennych
HORNI = 10
cislo = random.randrange(1, HORNI + 1)
zbyva = int(math.ceil(math.log(HORNI, 2)))
odhady = ""

# helper function to start and restart the game
def nova_hra():
    global HORNI, cislo, zbyva, odhady
    cislo = random.randrange(1, HORNI + 1)
    zbyva = int(math.ceil(math.log(HORNI, 2)))
    titul.config(text = u"Nová hra. Číslo je od 1 do " + str(HORNI))
    zbyvajici_text.config(text = u"Počet zbývajících pokusů je " + str(zbyva))
    odhady = ""
    odhady_text.config(text="Tvoje odhady " + odhady)
    status_text.config(text=u"Hádej číslo")

# definovani event handlers pro ridici panel
def vstup_odhadu(*args):
    # hlavni logika hry bude zde
    global cislo, zbyva, odhady
    zbyva -= 1
    zbyvajici_text.config(text = u"Počet zbývajících pokusů je " + str(zbyva))
    
    odhad = int(odhad_entry.get())
    if not odhady:
        odhady = str(odhad)
    else:
        odhady += ", " + str(odhad)
    odhady_text.config(text="Tvoje odhady " + odhady)
    odhad_entry.delete(0, END)

    if odhad == cislo:
        status_text.config(text=u"Tvůj odhad byl správný")
    else:
        if zbyva == 0:
            status_text.config(text=u"Vyčerpal si pokusy. Číslo bylo " + str(cislo))
        else:
            if odhad < cislo:
                status_text.config(text=u"Musíš hádat VYŠŠÍ číslo!")
            else:
                status_text.config(text=u"Musíš hádat NIŽŠÍ číslo!")

# vytvoreni ramce,
frame = Frame(root)
frame.grid(column=0, row=0, sticky=(N, W, E, S))

# registrovani event handleru pro ridici prvky
titul = Label(frame, text=u"Hádej číslo od 1 do " + str(HORNI),font="Verdana 12")
titul.grid(row = 1)

pokyn = Label(frame, text="Zadej odhad!",font="Verdana 10")
pokyn.grid(row = 2)

odhad_entry = Entry(frame)
odhad_entry.grid(row = 3)

odhady_text = Label(frame,text="Tvoje odhady " + odhady, font = "Tahoma 10",fg = "Blue")
odhady_text.grid(row = 4, sticky=(W))

zbyvajici_text = Label(frame,text=u"Zbývá pokusů ", font = "Tahoma 10",fg = "Blue")
zbyvajici_text.grid(row = 5, sticky=(W))

status_text = Label(frame,text=u"Hádej číslo", font = "Tahoma 12",fg = "Red")
status_text.grid(row = 6, sticky=(W))

new_button = Button(frame, text=u"Nová hra", width=10, command = nova_hra)
new_button.grid(row = 7)

odhad_entry.focus()
root.bind('<Return>', vstup_odhadu)

for child in frame.winfo_children(): child.grid_configure(padx=5, pady=5)

# volani nova_hra a spusteni okna
nova_hra()
frame.mainloop()
