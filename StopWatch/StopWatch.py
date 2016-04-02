# StopWatch Tkinter implementation
# For Python 2.7

from Tkinter import *

# Main window 'root'
root = Tk()
root.geometry("320x220")
root.title('Stopwatch: The Game')

frame = Frame(root)
frame.grid(row = 0, column = 0)

canvas = Canvas(root, width = 200, height = 200, bg='Black')
canvas.grid(row = 0, column = 1)

# global CONSTANTS (colors) and timer constant
CLR_SCORE = "yellow"
CLR_NORM = "white"
CLR_HIT = "green"
CLR_OOPS = "red"
DELTAT = 100

# global variables
time = 0
timer_is_running = False
attempts = 0
hits = 0
clr_time = CLR_NORM

# define helper function format that converts time t
# in tenths of seconds into formatted string m:ss.d
def format(t):
    m = str((t // 10) // 60)
    s = str((t // 10) % 60) 
    if len(s) == 1:
        s = "0" + s
    d = str(t % 10)
    return m + ":" + s + "." + d

# define event handlers for buttons; "Start", "Stop", "Reset", "Quit"

# starts only STOPPED watch
def start():
    global clr_time, timer_is_running
    if not timer_is_running:
        timer_is_running = True
        clr_time = CLR_NORM
        root.after(DELTAT, tick)

# stops only RUNNING watch
def stop():
    global attempts, hits, clr_time, timer_is_running
    if timer_is_running:
        root.after_idle(tick)
        timer_is_running = False
        attempts += 1
        if time % 10 == 0:
            hits += 1
            clr_time = CLR_HIT
        else:
            clr_time = CLR_OOPS

# resets only STOPPED watch
def reset():
    global time, attempts, hits, clr_time
    if not timer_is_running:
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
