import pygame as pg

pg.init()
pg.mixer.init()


TIMER = 5
SCORE = 0
MAPNUM = 2

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

PLAYER_SPEED = 350

screen = pg.display.set_mode([WIDTH, HEIGHT])

# function to create rect and scale image
def make_rect(group, path, l, t, w, h,scale=False, nW=0, nH=0):
    temp = pg.sprite.Sprite(group)
    temp.image = pg.image.load(path).convert_alpha()
    temp.rect = pg.Rect(l, t, w, h)
    if scale == True:
        temp.image = pg.transform.scale(temp.image, [nW, nH])

    return temp

# Draw groups
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

# Images
BGMENU = pg.image.load("img\\menu\\main_menu\\restaurante.jpg").convert()
BGMENU = pg.transform.scale(BGMENU, [WIDTH, HEIGHT])


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


# GO screen
retry_btn1 = make_rect(go_draw_group, "img\\menu\\game_over\\restart1.png", 80, 260, buttonW, buttonH)
retry_btn2 = make_rect(go_retry, "img\\menu\\game_over\\restart2.png", 80, 260, buttonW, buttonH)
retry_btn3 = pg.image.load("img\\menu\\game_over\\restart3.png")
quit_btn1 = make_rect(go_draw_group, "img\\menu\\main_menu\\sair1.png", 480, 260, buttonW, buttonH)
quit_btn2 = make_rect(go_quit, "img\\menu\\main_menu\\sair2.png", 480, 260, buttonW, buttonH)
quit_btn3 = pg.image.load("img\\menu\\main_menu\\sair3.png")


# Sound
vol = 0.5
vol_msc = 0.05
click_snd = pg.mixer.Sound("snd\\Effects\\btn_click.ogg")
click_snd.set_volume(vol)

# music = pg.mixer.music.load("snd\\BGM\\")
# pg.mixer.music.set_volume(vol_msc)

item_snd = pg.mixer.Sound("snd\\Effects\\item.ogg")
item_snd.set_volume(vol)