"""
Doplnte kod pro
- odrazy micku od sten (bouncing)
zmena pozice micku: ds = v * dt (dt je casovy interval v ms)
"""

from Tkinter import *
import random

root = Tk()
root.title("Ping Pong")
root.geometry("800x400")

# initialize globals - pos and vel encode vertical info for paddles
DELTAT = 24
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [100, 100]
dt = 0.024 # time interval in ms

# define event handlers
def update_canvas():
    global ball_pos, ball_vel

    # UPDATE BALL
    # levy odraz

    # pravy odraz
 
    # horni a dolni odraz
 
    # zmena pozice ball_pos
    ball_pos[0] += ball_vel[0] * dt
    ball_pos[1] += ball_vel[1] * dt

    # move ball
    ball_box = (ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS, \
                ball_pos[0] + BALL_RADIUS, ball_pos[1] + BALL_RADIUS)
    canvas.coords(ball, ball_box)

# Define buttons handlers
def quit():
    root.quit()
    root.destroy()

def tick():
    update_canvas()
    root.after(DELTAT, tick)

# create frame and register handlers
frame = Frame(root)
frame.grid(row = 0, column = 0)

b_quit = Button(frame, text ="Quit", command = quit, width = 14)
b_quit.grid(row = 0, column = 0, padx = 2, pady = 40)


# create canvas and canvas objects
canvas = Canvas(root, width = WIDTH, height = HEIGHT, bd = 0, bg = "Black")
canvas.grid(row = 0, column = 1, padx = 10)

# draw mid line and gutters
# draw ball
ball_box = (ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS, \
    ball_pos[0] + BALL_RADIUS, ball_pos[1] + BALL_RADIUS)
ball = canvas.create_oval(ball_box, fill = "White")

# start frame
root.after(DELTAT, tick)
root.mainloop()
