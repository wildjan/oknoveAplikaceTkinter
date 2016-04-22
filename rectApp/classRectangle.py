TICKT = 10
dt = 10. / TICKT
# Helper functions
import math, random

# Resi fyzikalni ulohu pruzny raz ctvercu k je koeficient pruznosti 0/1-nepruzne/pruzne
def rect_rect_collide(v1, v2):
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
    """Vraci taxicab vzdalenost dvou pozic p1 a p2"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class Ctverec(object):
    """Implementace tridy Ctverec pro animaci cverce v prostredi Tkinter"""
    def __init__(self, canvas, position, velocity, side, width, height, color="White"):
        self.pos = position
        self.vel = velocity
        self.side = side
        self.col = color
        self.width = width
        self.height = height
        self.life = 10
        self.alive = True
        box = self.get_box()
        self.sprite = canvas.create_rectangle(box, fill = self.col)
        self.txt_sprite = canvas.create_text(self.pos, text = str(self.life), font = "Verdana 10")

    def get_box(self):
        """Vraci ctverec pro zobrazeni mice-kruhu""" 
        box = (self.pos[0] - self.side/2,\
               self.pos[1] - self.side/2,\
               self.pos[0] + self.side/2,\
               self.pos[1] + self.side/2)
        return box

    def get_pos(self):
        """Vraci aktualni pozici ctverce"""
        return self.pos
    
    def get_vel(self):
        """Vraci aktualni rychlost ctverce"""
        return self.vel

    def set_vel(self, new_vel):
        """Nastavuje aktualni rychlost ctverce"""
        self.vel = new_vel

    def get_side(self):
        """Vraci polomer ctverce"""
        return self.side

    def isAlive(self):
        return self.alive

    def update(self):
        """
        Obnovuje pozici ctverce"
        """
        # Odrazy
        self.bounce_vert()
        self.bounce_horz()

        # Nastaveni pozice pos = pos + vel * dt
        pos_x, pos_y = self.pos
        pos_x += self.vel[0] * dt
        pos_y += self.vel[1] * dt
        self.pos = (pos_x, pos_y)

    def draw(self, canvas):
        if self.life <= 0:
            self.alive = False
            canvas.delete(self.sprite)
            canvas.delete(self.txt_sprite)
        box = self.get_box()
        canvas.coords(self.sprite, box)
        canvas.coords(self.txt_sprite, self.pos)
        canvas.itemconfig(self.txt_sprite, text = str(self.life))

    def bounce_vert(self):
        if self.pos[0] <= self.side/2 or self.pos[0] >= self.width - self.side/2:
            self.vel = -self.vel[0], self.vel[1]

    def bounce_horz(self):
        if self.pos[1] <= self.side/2 or self.pos[1] >= self.height - self.side/2:
            self.vel = self.vel[0], -self.vel[1]

    def colide(self, other):
        pos1 = self.get_pos()
        pos2 = other.get_pos()
        vel1 = self.vel
        vel2 = other.vel
        if dist(pos1, pos2) <= self.get_side()/2 + other.get_side()/2:
            vel1, vel2 = rect_rect_collide(vel1, vel2)
            self.set_vel(vel1)
            self.life -= 1
            other.set_vel(vel2)
            other.life -= 1
            return True
        else:
            return False
