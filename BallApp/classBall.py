TICKT = 10
dt = 10. / TICKT
# Helper functions
import math, random

# Resi fyzikalni ulohu pruzny raz kouli k je koeficient pruznosti 0/1-nepruzne/pruzne
def ball_ball_collide(v1, v2):
    """
    Bere dve rychlosti v1 a v2 pred odrazem
    Vraci rychlosti u1 a u2 po odrazu
    k je koeficient pruznosti 0<=k<=1 (k=1 - dokonele pruzny raz)
    """
    k = 1.
    v = ((v1[0] + v2[0]) / 2, (v1[1] +v2[1]) / 2)
    u1 = (v[0] - k * (v1[0] - v2[0]) / 2, v[1] - k * (v1[1] - v2[1]) / 2)
    u2 = (v[0] + k * (v1[0] - v2[0]) / 2, v[1] + k * (v1[1] - v2[1]) / 2)
    return u1, u2

def dist(p1, p2):
    """Vraci eukleidovskou vzdalenost dvou pozic p1 a p2"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class Ball(object):
    """Implementace tridy Ball pro animaci mice v prostredi Tkinter"""
    def __init__(self, canvas, position, velocity, radius, width, height, color = "Black"):
        self.pos = position
        self.vel = velocity
        self.rad = radius
        self.col = color
        self.width = width
        self.height = height
        box = self.get_box()
        self.sprite = canvas.create_oval(box, fill = self.col)

    def get_box(self):
        """Vraci ctverec pro zobrazeni mice-kruhu""" 
        box = (self.pos[0] - self.rad,\
               self.pos[1] - self.rad,\
               self.pos[0] + self.rad,\
               self.pos[1] + self.rad)
        return box

    def get_pos(self):
        """Vraci aktualni pozici mice"""
        return self.pos
    
    def get_vel(self):
        """Vraci aktualni rychlost mice"""
        return self.vel

    def set_vel(self, new_vel):
        """Nastavuje aktualni rychlost mice"""
        self.vel = new_vel

    def get_rad(self):
        """Vraci polomer mice"""
        return self.rad

    def update(self):
        """
        Obnovuje pozici mice"
        """
        # Odrazy

        # Nastaveni pozice pos = pos + vel * dt


    def draw(self, canvas):

        box = self.get_box()
        canvas.coords(self.sprite, box)

    def bounce_vert(self):
        if self.pos[0] <= self.rad or self.pos[0] >= self.width - self.rad:
            self.vel = -self.vel[0], self.vel[1]

    def bounce_horz(self):
        if self.pos[1] <= self.rad or self.pos[1] >= self.height - self.rad:
            self.vel = self.vel[0], -self.vel[1]

    def colide(self, other):
        pos1 = self.get_pos()
        pos2 = other.get_pos()
        vel1 = self.vel
        vel2 = other.vel
        if dist(pos1, pos2) <= self.get_rad() + other.get_rad():
            vel1, vel2 = ball_ball_collide(vel1, vel2)
            self.set_vel(vel1)
            other.set_vel(vel2)
