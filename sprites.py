import pygame as pg
# from settings import *
import settings as s

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # self.groups = game.all_sprites
        self.groups = game.player
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((s.TILESIZE, s.TILESIZE*s.PLAYER_HEIGHT_MULTIPLIER))
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.image = s.jack_front[0]
        self.right = False 
        self.left = False
        self.up = False
        self.down = False
        self.last_dir = 'down'
        self.walk_count = 0
        self.vx, self.vy = 0, 0
        self.x = x * s.TILESIZE
        self.y = y * s.TILESIZE
        self.score = s.SCORE
        self.scoreArr = list(map(int, str(self.score)))


    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -s.PLAYER_SPEED
            self.right = False
            self.left = True
            self.last_dir = 'left'

        else:
            self.left = False

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = s.PLAYER_SPEED
            self.left = False
            self.right = True
            self.last_dir = 'right'

        else:
            self.right = False
        
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -s.PLAYER_SPEED
            self.down = False
            self.up = True
            self.last_dir = 'up'

        else:
            self.up = False

        # if not keys[pg.K_s] and not keys[pg.K_DOWN]:
        #     self.down = False
        #     self.image = jack_front[0]

        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = s.PLAYER_SPEED
            self.up = False
            self.down = True
            self.last_dir = 'down'

        
        else:
            self.down = False

        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
        
    

    def update_sprite(self):
        
        if self.walk_count >= 9:
            self.walk_count = 0

        # moving up
        if self.up:
            self.image = s.jack_back[self.walk_count//3]
            self.walk_count += 1
            if self.walk_count >= 9:
                self.walk_count = 0
        # else:
        #     self.image = jack_back[0]
        #     self.walk_count = 0

        # moving down
        if self.down:
            self.image = s.jack_front[self.walk_count//3]
            self.walk_count += 1
            if self.walk_count >= 9:
                self.walk_count = 0
        # else:
        #     self.image = jack_front[0]
        #     self.walk_count = 0

        # moving right
        if self.right:
            self.image = s.jack_right[self.walk_count//3]
            self.walk_count += 1
            if self.walk_count >= 9:
                self.walk_count = 0
        # else:
        #     self.image = jack_right[0]
        #     self.walk_count = 0

        # moving left
        if self.left:
            self.image = s.jack_left[self.walk_count//3]
            self.walk_count += 1
            if self.walk_count >= 9:
                self.walk_count = 0
        # else:
        #     self.image = jack_left[0]
            # self.walk_count = 0
        else:
            if self.last_dir == 'left' and not self.left:
                self.image = s.jack_left[0]
            elif self.last_dir == 'right' and not self.right:
                self.image = s.jack_right[0]
            elif self.last_dir == 'up' and not self.up:
                self.image = s.jack_back[0]
            elif self.last_dir == 'down' and not self.down:
                self.image = s.jack_front[0]
        



    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
    
    def collide_with_item(self):
        if pg.sprite.spritecollide(self, self.game.items, True):
            self.score += 1
            s.TOTALSCORE += 1
            self.scoreArr = list(map(int, str(self.score)))
            s.item_snd.play()
            # print(self.scoreArr)

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        self.collide_with_item()

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, image):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((s.TILESIZE, s.TILESIZE))
        self.rect = self.image.get_rect()
        # self.image.fill(VIOLET)
        self.image = image
        self.x = x
        self.y = y
        self.rect.x = x * s.TILESIZE
        self.rect.y = y * s.TILESIZE

class Item(pg.sprite.Sprite):
    def __init__(self, game, x, y, item):
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((s.TILESIZE, s.TILESIZE))
        # self.image.fill(s.GREEN)
        self.rect = self.image.get_rect()
        self.image = item
        self.x = x + s.TILESIZE
        self.y = y + s.TILESIZE
        self.rect.x = x * s.TILESIZE
        self.rect.y = y * s.TILESIZE

class Floor(pg.sprite.Sprite):
    def __init__(self, game, x, y, image):
        self.groups = game.all_sprites, game.floors
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((s.TILESIZE, s.TILESIZE))
        self.rect = self.image.get_rect()
        self.image = image
        self.x = x
        self.y = y
        self.rect.x = x * s.TILESIZE
        self.rect.y = y * s.TILESIZE

# class SpriteSheet():
# 	def __init__(self, image):
# 		self.sheet = image

# 	def get_image(self, width, height, scale, colour, frame=1):
# 		image = pg.Surface((width, height)).convert_alpha()
# 		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
# 		image = pg.transform.scale(image, (width * scale, height * scale))
# 		image.set_colorkey(colour)

# 		return image


