"""
Screensaver v okenni aplikaci
"""
#from PIL import Image, ImageTk
from classRectangle import *
import random

# Hlavni okno se jmenuje 'root'
root = Tk()
root.title("Screenshot application")
root.geometry("1267x600")

# initializace globalnich promennych, konstant
WIDTH = 1067
HEIGHT = 600
SIDE = 80
NUMBER = 1
screen = Image.open(r'img\myScreen.png')
ctverce = []
saverRunning = False

# Pomocne funkce
def showScreen(canvas):
    """ """
    screenSprite = ImageTk.PhotoImage(screen)
    pos = screenSprite.width()/2, screenSprite.height()/2
    screenCanvas = canvas.create_image(pos, image=screenSprite)
    canvas.image = screenSprite

def resolve_colisions(ctverce):
    for idi in range(len(ctverce) - 1):
        for idj in range(idi + 1,len(ctverce)):
            first = ctverce[idi]
            second = ctverce[idj]
            first.colide(second)

# Event handlers
def start():
    global saverRunning
    if not saverRunning:
        canvas.delete(ALL)
        for dummy_idx in range(NUMBER):
            posx = random.randrange(SIDE, WIDTH - SIDE)
            posy = random.randrange(SIDE, HEIGHT - SIDE)
            velx = random.randrange(-5, 5)
            vely = random.randrange(-5, 5)
            ctverec = Ctverec(canvas, screen, (posx, posy), (velx, vely), SIDE, WIDTH, HEIGHT)
            ctverce.append(ctverec)
        saverRunning = True
        root.after(TICKT,tick)

def stop():
    global saverRunning,ctverce
    if saverRunning:
        saverRunning = False
        root.after_idle(tick)
        canvas.delete(ALL)
        ctverce = []
        showScreen(canvas)

def quit():
    root.quit()
    root.destroy()

def tick():
    if saverRunning:
        for ctverec in ctverce:
            ctverec.update()
            ctverec.draw(canvas)
        resolve_colisions(ctverce)
        root.after(TICKT, tick)

# VYRVORENI a REGISTRACE OBJEKTU HLAVNIHO OKNA
# Vytvoreni ramce = Frame
frame = LabelFrame(root, bd = 2, width=200, height = HEIGHT)
frame.grid(row = 0, column = 0)

# Vytvoreni objektu ramce Label (Labels, Buttons,...)
text_label = Label(frame, text="Spust screensaver", fg = "Blue", font="Verdana 12")
text_label.grid(row = 0, column = 0)

start_button = Button(frame, text ="Start!", command = start, width = 14)
start_button.grid(row = 1, column = 0)

stop_button = Button(frame, text ="Stop!", command = stop, width = 14)
stop_button.grid(row = 2, column = 0)

quit_button = Button(frame, text ="Quit", command = quit, width = 14)
quit_button.grid(row = 3, column = 0)

# Vytvoreni kresliciho platna = Canvas
canvas = Canvas(root, width=WIDTH, height=WIDTH, bd=0, bg ="Black")
canvas.grid(row = 0, column = 1)

# Vytvoreni 'screen'
#screenSprite = ImageTk.PhotoImage(screen)
#pos = screenSprite.width()/2, screenSprite.height()/2
#screenCanvas = canvas.create_image(pos, image=screenSprite)

# Vytvoreni ctverce
#pos = (100,100)
#box = (pos[0]-SIDE/2,pos[1]-SIDE/2,pos[0]+SIDE/2,pos[1]+SIDE/2)
#ctverecImage = screen.crop(box)
#ctverecSprite = ImageTk.PhotoImage(ctverecImage)
#ctverecCanvas = canvas.create_image(pos, image=ctverecSprite)

# Vytvoreni ctverce jako instanci tridy Cverec
#ctverec = Ctverec(canvas, screen, (400, 400), (2, 3), SIDE, WIDTH, HEIGHT)


# SPUSTENI Oknove aplikace
showScreen(canvas)
root.mainloop()

