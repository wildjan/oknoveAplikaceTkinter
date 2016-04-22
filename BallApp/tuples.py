pos = (1, 2)
vel = (1, 1)
dt = 1

posX, posY = pos
velX, velY = vel
posX += velX * dt
posY += velY * dt
pos = posX, posY
print pos
