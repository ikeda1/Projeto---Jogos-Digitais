import pygame as pg
import sys
from os import path
import settings as s
# from settings import *
from sprites import *
from map import *
import time


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)

    def load_data(self, map):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, map))
        # self.map_data = []
        # with open(path.join(game_folder, map), 'rt') as f:
        #     for line in f:
        #         self.map_data.append(line)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.load_data(f"map{s.MAPNUM}.txt")
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.startTime = time.time()
        print(f"Start Time: {self.startTime}")
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row, 'front')
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == '9':
                    Item(self, col, row)
        
        self.camera = Camera(self.map.width, self.map.height)
        self.hud = Hud(TIMER, SCORE)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

        self.tmpTime = time.time()
        self.currTime = abs((self.startTime - self.tmpTime))
        print(f"current time: {self.currTime:.2f}")

        if self.currTime >= s.TIMER:
            self.playing = False

    # def draw_grid(self):
    #     for x in range(0, WIDTH, TILESIZE):
    #         pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
    #     for y in range(0, HEIGHT, TILESIZE):
    #         pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        # self.draw_grid()
        # self.all_sprites.draw(self.screen)

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.screen.blit(self.hud.hudBackground, (self.hud.x, self.hud.y))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def GOevents(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    s.MAPNUM+=1
                    self.GO_screen = False
    

    def hover_check(self,img):
        return img.rect.collidepoint(pg.mouse.get_pos())

    def main_menu(self):

        # pg.mixer.music.play()
        self.menu_loop = True

        while self.menu_loop:
            
            self.screen.blit(s.BGMENU,[0, 0])

            mm_draw_group1.draw(self.screen)

            if self.hover_check(start_btn1):
                mm_start.draw(self.screen)
            elif self.hover_check(option_btn1):
                mm_option.draw(self.screen)
            elif self.hover_check(exit_btn1):
                mm_quit.draw(self.screen)

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    self.quit()

                elif event.type == pg.MOUSEMOTION:
                    x = pg.mouse.get_pos()[0]
                    y = pg.mouse.get_pos()[1]
                    # print(x, y)

                elif (event.type == pg.MOUSEBUTTONDOWN):
                    print(x, y)
                    # Start
                    if x >= startX and x <= startX+buttonW and y >= startY and y <= startY+buttonH:
                        click_snd.play()
                        self.screen.blit(start_btn3,[startX, startY])
                        pg.display.update()
                        pg.time.wait(400)
                        self.screen.fill(BLACK)
                        pg.display.update()
                        pg.time.wait(1000)
                        self.menu_loop = False
                    
                    # Options
                    elif x >= optionX and x <= optionX+buttonW and y >= optionY and y <= optionY+buttonH:
                        click_snd.play()
                        self.screen.blit(option_btn3,[optionX, optionY])
                        pg.display.update()
                        pg.time.wait(400)
                        self.option_screen()
                    
                    # Quit
                    elif x >= exitX and x <= exitX+buttonW and y >= exitY and y <= exitY+buttonH:
                        click_snd.play()
                        self.screen.blit(exit_btn3,[exitX, exitY])
                        pg.display.update()
                        pg.time.wait(400)
                        self.quit()
                    

            pg.display.update()

    def option_screen(self):
        self.vol = 0.5
        self.vol_msc = 0.05
        self.options = True
        self.snd_state = 1

        while self.options:
            screen.fill(WHITE)
            option_draw_group.draw(screen)
            close_draw_group.draw(screen)
            # print(self.snd_state,self.vol, self.vol_msc)

            font = pg.font.Font('freesansbold.ttf', 32)
 
            # create a text surface object,
            # on which text is drawn on it.
            text = font.render(str(f"{self.vol:.1f}"), True, BLACK)
            
            # create a rectangular object for the
            # text surface object
            textRect = text.get_rect()
            
            # set the center of the rectangular object.
            textRect.center = ((WIDTH // 2), (HEIGHT // 2) + 100)

            if self.hover_check(close_btn1):
                close_hover.draw(screen)
            if self.hover_check(snd_add):
                snd_add_hover.draw(screen)
            if self.hover_check(snd_minus):
                snd_minus_hover.draw(screen)
            if self.snd_state == 1:
                snd_on_button.draw(screen)
                if self.hover_check(snd_on):
                    snd_on_hover.draw(screen)
            if self.snd_state == 0:
                snd_off_button.draw(screen)
                if self.hover_check(snd_mute):
                    snd_off_hover.draw(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.MOUSEMOTION:
                    x = pg.mouse.get_pos()[0]
                    y = pg.mouse.get_pos()[1]
                    # print(x, y)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x = pg.mouse.get_pos()[0]
                    y = pg.mouse.get_pos()[1]

                    # close
                    if (x >= closeX and x <= closeX+closeW and y >= closeY and y <= closeY+closeH):
                        click_snd.play()
                        pg.time.wait(400)
                        self.options = False

                    # Minus
                    elif (x >= (WIDTH/2)-125 and x <= (WIDTH/2)-75 and y >= (HEIGHT/2) and y <= (HEIGHT/2)+50):
                        click_snd.play()
                        screen.blit(snd_minus_c, [(WIDTH/2)-125, (HEIGHT/2)])
                        pg.display.update()
                        pg.time.wait(200)
                        if self.vol > 0 and self.vol_msc > 0:
                            self.vol -= 0.1
                            self.vol_msc -= 0.01
                            click_snd.set_volume(self.vol)
                            pg.mixer.music.set_volume(self.vol_msc)
                            item_snd.set_volume(self.vol)
                            if self.vol <= 0.1 and self.vol_msc <= 0.01:
                                self.snd_state = 0
                                self.vol = 0
                                self.vol_msc = 0
                    
                    # Plus
                    elif (x >= (WIDTH/2)+75 and x <= (WIDTH/2)+125 and y >= (HEIGHT/2) and y <= (HEIGHT/2)+50):
                        click_snd.play()
                        screen.blit(snd_add_c, [(WIDTH/2)+75, (HEIGHT/2)])
                        pg.display.update()
                        pg.time.wait(200)
                        if self.vol < 0.9:
                            self.vol += 0.1
                            self.vol_msc += 0.01
                        click_snd.set_volume(self.vol)
                        pg.mixer.music.set_volume(self.vol_msc)
                        item_snd.set_volume(self.vol)
                        if self.vol > 0 and self.vol_msc > 0:
                            self.snd_state = 1
                        if self.vol >= 1 and self.vol_msc >= 1:
                            self.snd_state = 1
                            self.vol = 1
                            self.vol_msc = 1
                            

                    # On
                    elif self.snd_state == 1:
                        if (x >= (WIDTH/2)-25 and x <= (WIDTH/2)+25 and y >= (HEIGHT/2) and y <= (HEIGHT/2)+50):
                            click_snd.play()
                            screen.blit(snd_on_c, [(WIDTH/2)-25, (HEIGHT/2)])
                            pg.display.update()
                            pg.time.wait(200)
                            self.vol = 0
                            self.vol_msc = 0
                            click_snd.set_volume(self.vol)
                            pg.mixer.music.set_volume(self.vol_msc)
                            item_snd.set_volume(self.vol)
                            self.snd_state = 0

                    # Off
                    elif self.snd_state == 0:
                        if (x >= (WIDTH/2)-25 and x <= (WIDTH/2)+25 and y >= (HEIGHT/2) and y <= (HEIGHT/2)+50):
                            click_snd.play()
                            screen.blit(snd_mute_c, [(WIDTH/2)-25, (HEIGHT/2)])
                            pg.display.update()
                            pg.time.wait(200)
                            self.vol = 0.5
                            self.vol_msc = 0.05
                            click_snd.set_volume(self.vol)
                            pg.mixer.music.set_volume(self.vol_msc)
                            item_snd.set_volume(self.vol)
                            self.snd_state = 1
            screen.blit(text, textRect)
            pg.display.update()

    def show_go_screen(self):
        self.GO_screen = True

        while self.GO_screen:
            self.screen.fill(RED)
            pg.display.flip()
            self.GOevents()

# create the game object
g = Game()
# g.show_start_screen()
while True:
    g.main_menu()
    g.new()
    g.run()
    g.show_go_screen()