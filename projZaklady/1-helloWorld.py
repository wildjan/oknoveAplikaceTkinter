# -*- coding: cp1250 -*-
"""
Uvod do Tkinter okenni aplikace
Vytvoreni okna Hello world se stitkem "Ahoj světe"
Tutorial: http://tkinter.programujte.com/tkinter-hello-tkinter.htm
"""

from Tkinter import *

hlavni_okno = Tk()
hlavni_okno.title("Okenni aplikace 'Hello world'")

w = Label(hlavni_okno, text = u"Ahoj světe!")
w.pack()

hlavni_okno.mainloop()