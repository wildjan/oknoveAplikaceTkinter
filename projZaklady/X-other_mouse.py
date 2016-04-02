from Tkinter import *
root = Tk()
label_udalost = Label(root, text="Starting...")
label_udalost.grid()
label_udalost.bind('<Enter>', lambda e: label_udalost.configure(text='Moved mouse inside'))
label_udalost.bind('<Leave>', lambda e: label_udalost.configure(text='Moved mouse outside'))
label_udalost.bind('<1>', lambda e: label_udalost.configure(text='Clicked left mouse button'))
label_udalost.bind('<Double-1>', lambda e: label_udalost.configure(text='Double clicked'))
label_udalost.bind('<B3-Motion>', lambda e: label_udalost.configure(text='right button drag to %d,%d' % (e.x, e.y)))
root.mainloop()