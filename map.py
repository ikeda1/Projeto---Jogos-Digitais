import pygame as pg
from settings import *

class Map:
    def __init__(self, file):
        self.data = []

        with open(file, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tileW = len(self.data[0])
        self.tileH = len(self.data)
        self.width = self.tileW * TILESIZE
        self.height = (self.tileH * TILESIZE)# + 160

# this class will keep track of the whole view area, calculating an offset based on the movement from the player.
# the objects will be drawn on screen according to the offset calculated
class Camera:

    def __init__(self, width, heigth):
        self.camera = pg.Rect(0, 0, width, heigth) # this will keep track of the offset
        self.width = width
        self.heigth = heigth+160

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self, target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT/2)
        
        
        # camera scrolling limit
        x = min(0, x) # Left Limit
        x = max(-(self.width - WIDTH), x) # Right Limit
        y = min(0, y) # Top Limit
        y = max(-(self.heigth - HEIGHT), y) # Bottom Limit

        self.camera = pg.Rect(x, y, self.width, self.heigth)

class Hud:
    def __init__(self, time, score):
        # self.hudBackground = pg.image.load("")
        self.hudW = WIDTH
        self.hudH = 160
        self.hudBackground = pg.image.load("wall_front.png")
        self.hudBackground = pg.transform.scale(self.hudBackground, (WIDTH, self.hudH))
        self.x = 0
        self.y = HEIGHT-self.hudH
