# -*- coding: cp1250 -*-
from Tkinter import *

def calculate(*args):
    try:
        value = float(feet.get())
        result = 0.3048 * value
        output = "{:10.2f}".format(result)
        meters.set(output)
    except ValueError:
        meters.set(u"Zadej číslo lamo!")
    
root = Tk()
root.title(u"Stopy na Metry")

frame = Frame(root)
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = Entry(frame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

Label(frame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
Button(frame, text=u"Převeď", command=calculate).grid(column=3, row=3, sticky=W)

Label(frame, text="stop").grid(column=3, row=1, sticky=W)
Label(frame, text=u"odpovídá").grid(column=1, row=2, sticky=E)
Label(frame, text=u"metrům").grid(column=3, row=2, sticky=W)

for child in frame.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()