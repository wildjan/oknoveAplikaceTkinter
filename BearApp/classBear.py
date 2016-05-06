TICKT = 10
dt = 10. / TICKT
# Helper functions
import math, random

# Resi fyzikalni ulohu pruzny raz ctvercu k je koeficient pruznosti 0 az 1-nepruzny az pruzny

def bear_bear_collide(v1, v2):
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

class Bear(object):
    """Implementace tridy Bear pro animaci medveda v prostredi Tkinter"""
    def __init__(self, canvas, position, velocity, width, height, sprite, lives):
        self.pos = position
        self.vel = velocity
        self.width = width
        self.height = height
        self.sprite = sprite
        self.life = lives
        self.image = canvas.create_image(self.pos, image = self.sprite)
        text_pos = (self.pos[0], self.pos[1] - self.sprite.height()/2 - 10)
        self.lives = canvas.create_text(text_pos, text = str(self.life), font="Verdana 8", fill="Red")

    def get_pos(self):
        """Vraci aktualni pozici ctverce"""
        return self.pos
    
    def get_vel(self):
        """Vraci aktualni rychlost ctverce"""
        return self.vel

    def set_vel(self, new_vel):
        """Nastavuje aktualni rychlost ctverce"""
        self.vel = new_vel

    def get_life(self):
        """Vraci zivot"""
        return self.life

    def delete(self, canvas):
        """deletes self ctveres with text"""
        canvas.delete(self.image)
        canvas.delete(self.lives)

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

        canvas.coords(self.image, self.pos)
        canvas.itemconfig(self.lives, text=str(self.life))
        text_pos = (self.pos[0], self.pos[1] - self.sprite.height()/2 - 5)
        canvas.coords(self.lives, text_pos)

    def bounce_vert(self):
        if self.pos[0] <= self.sprite.width()/2 or self.pos[0] >= self.width - self.sprite.width()/2:
            self.vel = -self.vel[0], self.vel[1]

    def bounce_horz(self):
        if self.pos[1] <= self.sprite.height()/2 or self.pos[1] >= self.height - self.sprite.height()/2:
            self.vel = self.vel[0], -self.vel[1]

    def colide(self, other):
        pos1 = self.get_pos()
        pos2 = other.get_pos()
        vel1 = self.vel
        vel2 = other.vel
        if abs(pos1[0] - pos2[0]) < (self.sprite.width() / 2 + other.sprite.width() / 2) and\
           abs(pos1[1] - pos2[1]) < (self.sprite.height() / 2 + other.sprite.height() / 2):
            vel1, vel2 = bear_bear_collide(vel1, vel2)
            self.set_vel(vel1)
            self.life -= 1
            other.set_vel(vel2)
            other.life -= 1
