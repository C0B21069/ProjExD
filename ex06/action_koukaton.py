import pygame as pg
import sys
from random import randint
import tkinter as tk
import tkinter.messagebox as tkm


#ゲームクリア時に表示する
class Crea:
    def draw_text(self, text, size, x, y, color):
            font = pg.font.Font(None, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            self.screen.blit(text_surface,text_rect)


#キャラクターの動作の初期値の設定
class Player:
	def __init__(self, x, y):
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.on_ground = True
		self.in_the_air = False
		self.dead = False


#移動に関する関数
def update(self,screen,data):
    dx = 0
    dy = 0							
    key = pg.key.get_pressed()
    if key[pg.K_SPACE] and self.jumped == False and self.on_ground == True and self.in_the_air == False:
        self.jumped = True
        self.vel_y = -15
        self.on_ground = False
    if key[pg.K_SPACE] == False:
        self.jumped = False
    if key[pg.K_LEFT]:
        dx -= 5
    if key[pg.K_RIGHT]:
        dx += 5
    self.vel_y += 1
    if self.vel_y > 10:
        self.vel_y = 10
    dy += self.vel_y
    if self.vel_y != 0:
        self.in_the_air = True
    for tile in data:
        if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
            dx = 0
        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
            if self.vel_y < 0:
                dy = tile[1].bottom - self.rect.top
                self.vel_y = 0
            elif self.vel_y >= 0:
                dy = tile[1].top - self.rect.bottom
                self.vel_y = 0
                self.on_ground = True
                self.in_the_air = False		
    self.rect.x += dx
    self.rect.y += dy
    if self.rect.top >= 480:
        self.dead = True
    pg.draw.circle(screen, (0, 200, 50), self.rect.center,self.radius)


def main():
    #画面の表示
    root = tk.Tk()
    root.withdraw()
    pg.display.set_caption("こうかとん")
    scrn_sfc = pg.display.set_mode((800,480))
    scrn_rct = scrn_sfc.get_rect()

    #背景画像の設定
    bg_sfc = pg.image.load("fig/back.png")
    bg_rect = bg_sfc.get_rect()

    #キャラクター画像の設定
    tori_sfc = pg.image.load("fig/2.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 49, 347

    #キャラクターが動くように
    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc,bg_rect)
        key_states=pg.key.get_pressed()
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if tori_rct.center <= (49, 347):
            tori_rct.center = (49, 347)

        scrn_sfc.blit(tori_sfc,tori_rct)
        pg.display.update()
        clock.tick(1000)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return


if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit() #プログラム終了