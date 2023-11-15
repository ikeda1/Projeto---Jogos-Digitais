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
    def __init__(self, game, time, score):
        # self.hudBackground = pg.image.load("")
        self.game = game
        self.hudW = WIDTH
        self.hudH = 160
        self.hudBackground = pg.image.load("wall_front.png")
        self.hudBackground = pg.transform.scale(self.hudBackground, (WIDTH, self.hudH))
        self.x = 0
        self.y = HEIGHT-self.hudH
    
    def update(self):
        self.game.screen.blit(self.hudBackground, (self.x, self.y))
        self.game.screen.blit(textTime, (self.x+30, self.y+40))
        self.game.screen.blit(textScore, (self.x+30, self.y+100))
        # self.game.screen.blit(textItem, (self.x+300, self.y+40))

        self.show_score()
        self.show_time()
    
        # Shows score on screen
    def show_score(self):
        # score_txt_draw_group.draw(self.game.screen)
        print(self.game.player.scoreArr)
        if len(self.game.player.scoreArr) == 1:
            # print("IF")
            self.game.screen.blit(nums[int(self.game.player.scoreArr[0])], (self.x+160, self.y+98))
            # print(nums[int(scoreArr[0])])
            # print(scoreArr)
        
        else:
            print("else")
            self.game.screen.blit(nums[int(self.game.player.scoreArr[0])], (self.x+160, self.y+98))
            self.game.screen.blit(nums[int(self.game.player.scoreArr[1])], (self.x+177, self.y+98))
    
    def show_time(self):
        self.remainingTime = self.game.remainingTime - self.game.currTime
        self.remainingTime = list(map(int, str(int(self.remainingTime))))
        if len(self.remainingTime) == 1:
            self.game.screen.blit(nums[int(self.remainingTime[0])], (self.x+150, self.y+38))
        else:
            self.game.screen.blit(nums[int(self.remainingTime[0])], (self.x+150, self.y+38))
            self.game.screen.blit(nums[int(self.remainingTime[1])], (self.x+167, self.y+38))

        


    


        
