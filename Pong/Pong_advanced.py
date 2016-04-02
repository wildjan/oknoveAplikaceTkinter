# Implementation of classic arcade game Pong
# Changes:
# Only one "direction" variable, "left = True" is LEFT and/or RIGHT is not left :)
# ball position change: ds = v * dt (dt is time interval in seconds)
# ad 9) if STATUS = "Hard" ball velocity is multiplied by 1.1 after each hit 

from Tkinter import *
import random

root = Tk()
root.title("Ping Pong")
root.geometry("800x400")

# initialize globals - pos and vel encode vertical info for paddles
TIME = 17
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
left = random.choice([False, True]) # left = False (RIGHT) xor left = True (LEFT)
PADDLE_VEL = 4 # velocity of paddles if moving
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
ball_pos = [WIDTH / 2, HEIGHT / 2] #
ball_vel = [0, 0]
score1 = 0
sc1 = StringVar()
score2 = 0
sc2 = StringVar()
difficulty = 1
diff_koef = 1.1
diff_text  = StringVar()
sc1 = str(score1)
sc2 = str(score2)
diff_text = "Velocity is " + str(int(round(difficulty * 100))) + "%"    
hard = False
#t = 0
dt = 0.02 # time interval in seconds

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction_is_left):
    global ball_pos, ball_vel # these are vectors stored as lists
    global difficulty
    difficulty = 1
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = random.randrange(120, 240)
    ball_vel[1] = -random.randrange(60, 180)
    if direction_is_left:
        ball_vel[0] = -ball_vel[0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, sc1, sc2, difficulty, diff_text  # these are ints
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    score1 = 0
    score2 = 0
    difficulty = 1
    sc1 = str(score1)
    sc2 = str(score2)
    diff_text = "Velocity is " + str(int(round(difficulty * 100))) + "%"
    canvas.itemconfig(t_sc1, text = str(score1))
    canvas.itemconfig(t_sc2, text = str(score2))
    left = random.choice([False, True])
    spawn_ball(left)

def update_canvas():
    global score1, score2, difficulty, paddle1_pos, paddle2_pos
    global ball_pos, ball_vel
       
    # update ball
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            if hard:
                difficulty *= diff_koef
                ball_vel[0] *= diff_koef
                ball_vel[1] *= diff_koef
                canvas.itemconfig(t_vel, text = "Velocity is " + str(int(round(difficulty * 100))) + "%")
        else:
            score2 += 1
            canvas.itemconfig(t_sc2, text = str(score2))
            spawn_ball(False)

    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            if hard:
                difficulty *= diff_koef
                ball_vel[0] *= diff_koef
                ball_vel[1] *= diff_koef
                canvas.itemconfig(t_vel, text = "Velocity is " + str(int(round(difficulty * 100))) + "%")
        else:
            score1 += 1
            canvas.itemconfig(t_sc1, text = str(score1))
            spawn_ball(True)

    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0] * dt
    ball_pos[1] += ball_vel[1] * dt

    # move ball
    ball_box = (ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS, \
                ball_pos[0] + BALL_RADIUS, ball_pos[1] + BALL_RADIUS)    
    canvas.coords(ball, ball_box)    

    # update paddle's 1 vertical position, keep paddle on the screen
    if (HALF_PAD_HEIGHT < paddle1_pos and paddle1_vel < 0) or \
       (paddle1_pos < HEIGHT - HALF_PAD_HEIGHT and paddle1_vel > 0):
        paddle1_pos += paddle1_vel

    # update paddle's 2 vertical position, keep paddle on the screen
    if (HALF_PAD_HEIGHT < paddle2_pos and paddle2_vel < 0) or \
       (paddle2_pos < HEIGHT - HALF_PAD_HEIGHT and paddle2_vel > 0):
        paddle2_pos += paddle2_vel

    # move paddles    
    canvas.coords(paddle1, (HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT, HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT))
    canvas.coords(paddle2, (WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT, WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT))

# Define key_press events
def key_press(event):
    global paddle1_vel, paddle2_vel
    key_code = repr(event.keycode)
    if key_code == '87':
        paddle1_vel = -PADDLE_VEL
    if key_code == '83':
        paddle1_vel = PADDLE_VEL
    if key_code == '38':
        paddle2_vel = -PADDLE_VEL
    if key_code == '40':
        paddle2_vel = PADDLE_VEL

# Define key_release events
def key_release(event):
    global paddle1_vel, paddle2_vel
    key_code = repr(event.keycode)
    if key_code == '87':
        paddle1_vel = 0
    if key_code == '83':
        paddle1_vel = 0
    if key_code == '38':
        paddle2_vel = 0
    if key_code == '40':
        paddle2_vel = 0


# Define buttons handlers
def restart():
    new_game()

def status():
    global hard
    if hard:
        hard = False
        b_status.config(text = "Easy")
    else:
        hard = True
        b_status.config(text = "Hard")

def quit():
    root.quit()
    root.destroy()

def tick():
    update_canvas()
    root.after(TIME, tick)

# create frame and register handlers
frame = Frame(root)
frame.grid(row = 0, column = 0)

b_restart = Button(frame, text = "Restart", command = restart, width = 14)                             
b_restart.grid(row = 1, column = 0, padx = 2, pady = 2)

l_empty = Label(frame, text = '\n \n')
l_empty.grid(row = 2, column = 0, padx = 2, pady = 2)

l_diff = Label(frame, text = 'Difficulty: \n "Hard means increasing velocity"', fg = 'red')
l_diff.grid(row = 3, column = 0, padx = 2, pady = 2)

b_status = Button(frame, text ="Easy", command = status, width = 14)
b_status.grid(row = 4, column = 0, padx = 2, pady = 2)

b_quit = Button(frame, text ="Quit", command = quit, width = 14)
b_quit.grid(row = 6, column = 0, padx = 2, pady = 40)

#frame.set_key_handler(key)
frame.bind("<KeyPress>", key_press)
frame.bind("<KeyRelease>", key_release)
frame.focus_set()

# create canvas and canvas objects
canvas = Canvas(root, width = WIDTH, height = HEIGHT, bd = 0, bg = "Black")
canvas.grid(row = 0, column = 1, padx = 10)

# draw mid line and gutters
canvas.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, width = 1, fill ="White")
canvas.create_line(PAD_WIDTH, 0,PAD_WIDTH, HEIGHT, fill ="White")
canvas.create_line(WIDTH - PAD_WIDTH, 0,WIDTH - PAD_WIDTH, HEIGHT, fill = "White")

# draw paddles
paddle1 = canvas.create_line(HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT,\
            HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT,\
            width = PAD_WIDTH, fill = 'White')
paddle2 = canvas.create_line(WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT,\
            WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT,\
            width = PAD_WIDTH, fill = 'White')

# draw ball
ball_box = (ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS, \
    ball_pos[0] + BALL_RADIUS, ball_pos[1] + BALL_RADIUS)
ball = canvas.create_oval(ball_box, fill = "White")

# draw texts
t_sc1 = canvas.create_text(WIDTH / 2 - 40, 80, text = sc1, fill = 'White', font = "Verdana 32")
t_sc2 = canvas.create_text(WIDTH / 2 + 40, 80, text = sc2, fill = 'White', font = "Verdana 32")
t_vel = canvas.create_text(70, 20, text = diff_text, fill = 'Red', font = "Verdana 10")    


# start frame
root.after(TIME, tick)
new_game()
root.mainloop()
