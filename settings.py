import pygame as pg
from os import path

# from sprites import Spritesheet

pg.init()
pg.mixer.init()

GAMEFOLDER = path.dirname(__file__)

TIMER = 60
TIMEARR = [80, 70, 60]
SCORE = 0
TOTALSCORE = 0
RECORDS = 0
PHASESCORE = [5, 8, 12]
MAPNUM = 1
FONTE = pg.font.SysFont("Monospace", 60, True, True)


# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
VIOLET = (138,43,226)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Projeto"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_SPEED = 250
PLAYER_HEIGHT_MULTIPLIER = 1.2

screen = pg.display.set_mode([WIDTH, HEIGHT])

# function to create rect and scale image
def make_rect(group, path, l, t, w, h,scale=False, nW=0, nH=0):
    temp = pg.sprite.Sprite(group)
    temp.image = pg.image.load(path).convert_alpha()
    temp.rect = pg.Rect(l, t, w, h)
    if scale == True:
        temp.image = pg.transform.scale(temp.image, [nW, nH])

    return temp

# # Draw groups
# ## Menu
# mm_draw_group1 = pg.sprite.Group()
# mm_start = pg.sprite.Group()
# mm_option = pg.sprite.Group()
# mm_inst = pg.sprite.Group()
# mm_quit = pg.sprite.Group()
# ## option
# option_draw_group = pg.sprite.Group()
# snd_add_hover = pg.sprite.Group()
# snd_minus_hover = pg.sprite.Group()
# snd_on_button = pg.sprite.Group()
# snd_on_hover = pg.sprite.Group()
# snd_off_button = pg.sprite.Group()
# snd_off_hover = pg.sprite.Group()
# # Close Button
# close_draw_group = pg.sprite.Group()
# close_hover = pg.sprite.Group()
# start_draw_group = pg.sprite.Group()


# Loading images

## Menu
mm_draw_group1 = pg.sprite.Group()
mm_start = pg.sprite.Group()
mm_option = pg.sprite.Group()
mm_inst = pg.sprite.Group()
mm_quit = pg.sprite.Group()

## option
option_draw_group = pg.sprite.Group()
snd_add_hover = pg.sprite.Group()
snd_minus_hover = pg.sprite.Group()
snd_on_button = pg.sprite.Group()
snd_on_hover = pg.sprite.Group()
snd_off_button = pg.sprite.Group()
snd_off_hover = pg.sprite.Group()
# Close Button
close_draw_group = pg.sprite.Group()
close_hover = pg.sprite.Group()
start_draw_group = pg.sprite.Group()
## Game Over
go_draw_group = pg.sprite.Group()
go_quit = pg.sprite.Group()
go_retry = pg.sprite.Group()

## Continue game
continue_draw_group = pg.sprite.Group()
continue_start = pg.sprite.Group()

# Score
score_txt_draw_group = pg.sprite.Group()
score_draw_group = pg.sprite.Group()

# Images
BGMENU = pg.image.load("img\\menu\\main_menu\\restaurante.jpg").convert()
BGMENU = pg.transform.scale(BGMENU, [WIDTH, HEIGHT])
MAINMENUIMAGE = pg.image.load("img\\menu\\main_menu\\2012.jpg").convert()
MAINMENUIMAGE = pg.transform.scale(MAINMENUIMAGE, [WIDTH, HEIGHT])


# mm_draw_group
buttonW = 200
buttonH = 50
startX, startY = 60, 500
start_btn1 = make_rect(mm_draw_group1, "img\\menu\\main_menu\\start1.png", startX, startY, buttonW, buttonH)
start_btn2 = make_rect(mm_start, "img\\menu\\main_menu\\start2.png", startX, startY, buttonW, buttonH)
start_btn3 = pg.image.load("img\\menu\\main_menu\\start3.png")

optionX, optionY = startX, startY+60
option_btn1 = make_rect(mm_draw_group1, "img\\menu\\main_menu\\options1.png", optionX, optionY, buttonW, buttonH)
option_btn2 = make_rect(mm_option, "img\\menu\\main_menu\\options2.png", optionX, optionY, buttonW, buttonH)
option_btn3 = pg.image.load("img\\menu\\main_menu\\options3.png")

exitX, exitY = startX, optionY+60
exit_btn1 = make_rect(mm_draw_group1, "img\\menu\\main_menu\\sair1.png", exitX, exitY, buttonW, buttonH)
exit_btn2 = make_rect(mm_quit, "img\\menu\\main_menu\\sair2.png", exitX, exitY, buttonW, buttonH)
exit_btn3 = pg.image.load("img\\menu\\main_menu\\sair3.png")

closeW, closeH = 50, 50
closeX, closeY = WIDTH-80, 30
close_btn1 = make_rect(close_draw_group, "img\\menu\\botao_sair.png", closeX, closeY, closeW, closeH)
close_btn2 = make_rect(close_hover, "img\\menu\\botao_sair2.png", closeX, closeY, closeW, closeH)

# option_draw_group

option_pag1 = make_rect(option_draw_group, "img\\menu\\options\\options_pag1.jpg", 0, 0, 732, 400, True, WIDTH, HEIGHT)

snd_btn_H, snd_btn_W = 50, 50
snd_on = make_rect(snd_on_button, "img\\menu\\options\\botao_som_on_02.png", (WIDTH/2)-25, (HEIGHT/2), snd_btn_H, snd_btn_W)
snd_on_h = make_rect(snd_on_hover, "img\\menu\\options\\botao_som_on_03.png", (WIDTH/2)-25, (HEIGHT/2), snd_btn_H, snd_btn_W)
snd_on_c = pg.image.load("img\\menu\\options\\botao_som_on.png")

snd_minus = make_rect(option_draw_group, "img\\menu\\options\\botao_som_down_02.png", (WIDTH/2)-125, (HEIGHT/2), snd_btn_H, snd_btn_W)
snd_minus_h = make_rect(snd_minus_hover, "img\\menu\\options\\botao_som_down_03.png", (WIDTH/2)-125, (HEIGHT/2), snd_btn_H, snd_btn_W)
snd_minus_c = pg.image.load("img\\menu\\options\\botao_som_down.png")

snd_add = make_rect(option_draw_group, "img\\menu\\options\\botao_som_up_02.png", (WIDTH/2)+75, (HEIGHT/2), snd_btn_H, snd_btn_W)
snd_add_h = make_rect(snd_add_hover, "img\\menu\\options\\botao_som_up_03.png", (WIDTH/2)+75, (HEIGHT/2), snd_btn_H, snd_btn_W)
snd_add_c = pg.image.load("img\\menu\\options\\botao_som_up.png")

snd_mute = make_rect(snd_off_button, "img\\menu\\options\\botao_som_off_02.png", (WIDTH/2)-25, (HEIGHT/2), snd_btn_H, snd_btn_W)
snd_mute_h = make_rect(snd_off_hover, "img\\menu\\options\\botao_som_off_03.png", (WIDTH/2)-25, (HEIGHT/2), snd_btn_H, snd_btn_W)
snd_mute_c = pg.image.load("img\\menu\\options\\botao_som_off.png")

# Continue draw group
continueX, continueY = (WIDTH//2)-(buttonW//2), (HEIGHT//2)-(buttonH//2)
continue_btn1 = make_rect(continue_draw_group, "img\\menu\\main_menu\\start1.png", continueX, continueY, buttonW, buttonH)
continue_btn2 = make_rect(continue_start, "img\\menu\\main_menu\\start2.png", continueX, continueY, buttonW, buttonH)
continue_btn3 = pg.image.load("img\\menu\\main_menu\\start3.png")

font = pg.font.Font('freesansbold.ttf', 32)
text = font.render('Proxima fase?', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (WIDTH//2, (HEIGHT//2)-100)

# End game
endText = font.render('Parabéns, você chegou ao fim do jogo!', True, BLACK, WHITE)
endTextRect = text.get_rect()
endTextRect.center = ((WIDTH//2)-160, (HEIGHT//2)-100)

# GO screen
retryX, retryY = (WIDTH//2)-(1.5*buttonW), (HEIGHT//2)+150
retry_btn1 = make_rect(go_draw_group, "img\\menu\\game_over\\restart1.png", retryX, retryY, buttonW, buttonH)
retry_btn2 = make_rect(go_retry, "img\\menu\\game_over\\restart2.png", retryX, retryY, buttonW, buttonH)
retry_btn3 = pg.image.load("img\\menu\\game_over\\restart3.png")
quit_btn1 = make_rect(go_draw_group, "img\\menu\\main_menu\\sair1.png", retryX+2*buttonW, retryY, buttonW, buttonH)
quit_btn2 = make_rect(go_quit, "img\\menu\\main_menu\\sair2.png", retryX+2*buttonW, retryY, buttonW, buttonH)
quit_btn3 = pg.image.load("img\\menu\\main_menu\\sair3.png")

# Spritesheet

class Spritesheet():
    def __init__(self, filename):
        self.sheet = pg.image.load(filename).convert()

    def image_at(self, rectangle, colorkey = (0, 0, 0)):
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pg.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = (0, 0, 0)):
        return [self.image_at(rect, colorkey) for rect in rects]
    
    def inver_images_at(self, rects, colorkey = (0, 0, 0)):
        return [pg.transform.flip(self.image_at(rect, colorkey), True, False) for rect in rects]


# spritesheet_image = pg.image.load("img\\game\\map\\map_spritesheet.png").convert_alpha()

# spritesheet = SpriteSheet(spritesheet_image)
# wall_border_down_right = spritesheet.get_image(32, 32, 1, BLACK)
# wall_border_bottom = spritesheet.get_image(32, 32, 1, BLACK)
mapSS = Spritesheet('img\\game\\map\\map_spritesheet.png')


wall_corner_left = mapSS.image_at((160, 0, 32, 32))
wall_top = mapSS.image_at((192, 0, 32, 32))
wall_corner_right = mapSS.image_at((224, 0, 32, 32))
wall_left = mapSS.image_at((160, 32, 32, 32))
wall_middle = mapSS.image_at((192, 32, 32, 32))
wall_right = mapSS.image_at((224, 32, 32, 32))
wall_bottom_left = mapSS.image_at((160, 64, 32, 32))
wall_bottom = mapSS.image_at((192, 64, 32, 32))
wall_bottom_right = mapSS.image_at((224, 64, 32, 32))

top_left_corner = mapSS.image_at((256, 0, 32, 32))
top_corner = mapSS.image_at((288, 0, 32, 32))
top_right_corner = mapSS.image_at((320, 0, 32, 32))
left_corner = mapSS.image_at((256, 32, 32, 32))
right_corner = mapSS.image_at((320, 32, 32, 32))
bottom_left_corner = mapSS.image_at((256, 64, 32, 32))
bottom_corner = mapSS.image_at((288, 64, 32, 32))
bottom_right_corner = mapSS.image_at((320, 64, 32, 32))


bed1 = mapSS.image_at((448, 0, 32, 32))
bed2 = mapSS.image_at((448, 32, 32, 32))
bed3 = mapSS.image_at((448, 64, 32, 32))

wooden_floor = mapSS.image_at((0, 96, 32, 32))
cracked_wooden_floor = mapSS.image_at((32, 96, 32, 32))
tile_floor = mapSS.image_at((0, 128, 32, 32))
cracked_tile_floor = mapSS.image_at((0, 160, 32, 32))
stone_floor = mapSS.image_at((32, 128, 32 ,32))
cracked_stone_floor = mapSS.image_at((32, 160, 32, 32))

wardrobe_1 = mapSS.image_at((0, 192, 32, 32))
wardrobe_2 = mapSS.image_at((0, 224, 32, 32))

bookshelf_1 = mapSS.image_at((32, 192, 32, 32))
bookshelf_2 = mapSS.image_at((32, 224, 32, 32))

drawer_1 = mapSS.image_at((128, 192, 32, 32))
drawer_2 = mapSS.image_at((128, 224, 32, 32))

sink_top = mapSS.image_at((64, 96, 32, 32))
cabinet_top = mapSS.image_at((96, 96, 32, 32))
cooktop = mapSS.image_at((128, 96, 32, 32))
cabinet_door = mapSS.image_at((64, 128, 32, 32))
cabinet = mapSS.image_at((96, 128, 32, 32))
oven = mapSS.image_at((128, 128, 32, 32))

obs_top = mapSS.image_at((192, 96, 32, 32))
obs_bottom = mapSS.image_at((192, 128, 32, 32))

# Items
backpack = pg.image.load('img\\game\\itens\\backpack.png')
backpack = pg.transform.scale(backpack,(TILESIZE, TILESIZE))
bandage = pg.image.load('img\\game\\itens\\bandage.png')
bandage = pg.transform.scale(bandage, (TILESIZE, TILESIZE))
food1 = pg.image.load('img\\game\\itens\\canned_food_1.png')
food1 = pg.transform.scale(food1 ,(TILESIZE, TILESIZE))
food2 = pg.image.load('img\\game\\itens\\canned_food_2.png')
food2 = pg.transform.scale(food2 ,(TILESIZE, TILESIZE))
food3 = pg.image.load('img\\game\\itens\\canned_food_3.png')
food3 = pg.transform.scale(food3 ,(TILESIZE, TILESIZE))
food4 = pg.image.load('img\\game\\itens\\canned_food_4.png')
food4 = pg.transform.scale(food4 ,(TILESIZE, TILESIZE))
flashlight = pg.image.load('img\\game\\itens\\flashlight_1.png')
flashlight = pg.transform.scale(flashlight ,(TILESIZE, TILESIZE))
hammer = pg.image.load('img\\game\\itens\\hammer.png')
hammer = pg.transform.scale(hammer ,(TILESIZE, TILESIZE))
pills1 = pg.image.load('img\\game\\itens\\pill_1.png')
pills1 = pg.transform.scale(pills1 ,(TILESIZE//2, TILESIZE))
pills2 = pg.image.load('img\\game\\itens\\pills_2.png')
pills2 = pg.transform.scale(pills2 ,(TILESIZE//2, TILESIZE))
rope = pg.image.load('img\\game\\itens\\rope.png')
rope = pg.transform.scale(rope ,(TILESIZE, TILESIZE))
water = pg.image.load('img\\game\\itens\\water.png')
water = pg.transform.scale(water ,(TILESIZE//2, TILESIZE))





# Characters
jackSS = Spritesheet('img\\PLAYER\\Males\\M_08.png')
jack_front = jackSS.images_at([(2, 2, 12, 15), (2, 19, 12, 15), (2, 36, 12, 15)])
jack_front[0] = pg.transform.scale(jack_front[0],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])
jack_front[1] = pg.transform.scale(jack_front[1],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])
jack_front[2] = pg.transform.scale(jack_front[2],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])

jack_back = jackSS.images_at([(34, 2, 12, 15), (34, 19, 12, 15), (34, 36, 12, 15)])
jack_back[0] = pg.transform.scale(jack_back[0],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])
jack_back[1] = pg.transform.scale(jack_back[1],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])
jack_back[2] = pg.transform.scale(jack_back[2],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])

jack_right = jackSS.images_at([(19, 2, 10, 15), (19, 19, 10, 15), (19, 36, 10, 15)])
jack_right[0] = pg.transform.scale(jack_right[0],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])
jack_right[1] = pg.transform.scale(jack_right[1],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])
jack_right[2] = pg.transform.scale(jack_right[2],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])

jack_left = jackSS.inver_images_at([(19, 2, 10, 15), (19, 19, 10, 15), (19, 36, 10, 15)])
jack_left[0] = pg.transform.scale(jack_left[0],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])
jack_left[1] = pg.transform.scale(jack_left[1],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])
jack_left[2] = pg.transform.scale(jack_left[2],[TILESIZE, TILESIZE*PLAYER_HEIGHT_MULTIPLIER])

# HUD
textSS = Spritesheet('img\\game\\hud\\words.png')
textTime = textSS.image_at([1, 1, 100, 21])
textItem = textSS.image_at([108, 1, 94, 21])
textScore = textSS.image_at([2, 25, 115, 21])


# Score
scoreArr = [str(SCORE)]
nums = [pg.image.load('img\\game\\hud\\num_0.png'), pg.image.load('img\\game\\hud\\num_1.png'), pg.image.load('img\\game\\hud\\num_2.png'), pg.image.load('img\\game\\hud\\num_3.png'), pg.image.load('img\\game\\hud\\num_4.png'), pg.image.load('img\\game\\hud\\num_5.png'), pg.image.load('img\\game\\hud\\num_6.png'), pg.image.load('img\\game\\hud\\num_7.png'), pg.image.load('img\\game\\hud\\num_8.png'), pg.image.load('img\\game\\hud\\num_9.png')]
# for i in len(nums):
    # nums[i] = pg.transform.scale(nums[i], [])
numsCount = []

countW = 90
countH = 150
for i in range(4):
    numsCount.append(pg.transform.scale(nums[i], [countW, countH]))

for i in range(len(nums)):
    nums[i] = pg.transform.scale(nums[i], [15, 25])
# score_text = make_rect(score_txt_draw_group, "img\\pontuacao.png", 786, 20, 256, 76, True, 256, 76)

# Sound
vol = 0.5
vol_msc = 0.05
click_snd = pg.mixer.Sound("snd\\Effects\\btn_click.ogg")
click_snd.set_volume(vol)

music = pg.mixer.music.load("snd\\BGM\\musicaMenu.mp3")
pg.mixer.music.set_volume(vol_msc)

item_snd = pg.mixer.Sound("snd\\Effects\\scoreSound.ogg")
item_snd.set_volume(vol)