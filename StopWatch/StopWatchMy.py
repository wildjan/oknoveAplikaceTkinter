"""
StopWatch je hra, jejimz cilem je zastavit stopky na celych sekundach
Doplnte kod pro:
- formatovani casu M:SS.D
- resetovani hry
- zmena barvy stopek: CLR_NORM/CLR_HIT/CLR_OOPS pri
  normalnim behu/zasahu/nezasahu
"""

from Tkinter import *

# Hlavni okno 'root'
root = Tk()
root.geometry("360x240")
root.title('Stopky: Vzrusujici hra')

# Ramec pro tlacitka
frame = Frame(root)
frame.grid(row = 0, column = 0)

# Canvas na zobrazeni stopek a skore
canvas = Canvas(root, width = 200, height = 200, bg='Black')
canvas.grid(row = 0, column = 1, sticky='E')

# globalni KONSTANTY (barvy) and KONSTANTA casovace
CLR_SCORE = "yellow"
CLR_NORM = "white"
CLR_HIT = "green"
CLR_OOPS = "red"
DELTAT = 100

# globalni promenne
time = 0
timer_is_running = False
attempts = 0
hits = 0
clr_time = CLR_NORM

# definujte pomocnou funkci format(), ktera prevadi cas t
# v desetinach sekundy na formatovany string m:ss.d
def format(t):
    """
    Vstup: t v desetinach sekundy
    Vystup: 'M:SS.D'
    """
    dec = t % 10
    sec = (t / 10) % 60
    min = t / 600
    return "{:}:{:02}.{:}".format(min, sec, dec)

# definujte event handlers pro buttons; "Start", "Stop", "Reset", "Quit"

# spousti pouze zastavene stopky
def start():
    global clr_time, timer_is_running
    if not timer_is_running:
        clr_time = CLR_NORM
        timer_is_running = True
        root.after(DELTAT, tick)

# zastavuje pouze BEZICI stopky
def stop():
    global attempts, hits, clr_time, timer_is_running
    if timer_is_running:
        root.after_idle(tick)
        timer_is_running = False
        attempts += 1
        if time % 10 == 0:
            clr_time = CLR_HIT
            hits += 1
        else:
            clr_time = CLR_OOPS

# resetuje pouze ZASTAVENE stopky
def reset():
    global time, attempts, hits, clr_time
    if not timer_is_running:
        # doplnte kod pro resetovani hry
        time = 0
        attempts = 0
        hits = 0
        clr_time = CLR_NORM
        draw()

# quits the game
def quit():
    root.quit()
    root.destroy()

# define event handler for timer with 0.1 sec interval
def tick():
    global time, time_is_running
    draw()
    if timer_is_running:
        time += 1
        root.after(DELTAT, tick)

# define draw handler
def draw():
    canvas.itemconfig(text_score, text = str(hits) + "/" + str(attempts), fill = CLR_SCORE)
    canvas.itemconfig(text_time, text = format(time), fill = clr_time)

# register timer event handler
timer = root.after(DELTAT, tick)

# register button handlers
start_button = Button(frame, text ="Start", command = start, width = 14)
start_button.grid(row = 0, column = 0, padx = 2, pady = 2)

stop_button = Button(frame, text ="Stop", command = stop, width = 14)
stop_button.grid(row = 1, column = 0, padx = 2, pady = 2)

reset_button = Button(frame, text ="Reset", command = reset, width = 14)
reset_button.grid(row = 2, column = 0, padx = 2, pady = 2)

quit_button = Button(frame, text ="Quit", command = quit, width = 14)
quit_button.grid(row = 3, column = 0, padx = 2, pady = 40)

# draw text ojects on canvas
text_score = canvas.create_text(160, 30, text = "0/0", font = "Verdana 24", fill = CLR_SCORE)
text_time = canvas.create_text(100, 100, text = "0:00.0", font = "Verdana 40", fill = clr_time)

# start frame
mainloop()
