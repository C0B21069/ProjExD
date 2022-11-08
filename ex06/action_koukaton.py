import pygame as pg
import sys
from random import randint
import tkinter as tk
import tkinter.messagebox as tkm


#キャラクターの動作の初期値の設定
class Player():
	def __init__(self, x, y):
		# self.image = pg.Surface((800,480))
		# self.rect = self.image.get_rect()
		# self.radius = int(tile_size / 2)
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jumped = False
		self.on_ground = True
		self.in_the_air = False
		self.dead = False

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