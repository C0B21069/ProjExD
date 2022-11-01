import pygame as pg
import sys
from random import randint
import time
import tkinter as tk
import tkinter.messagebox as tkm


MAX_SHOTS = 100 #こうかとんが撃てる弾の最大数
SCORE = 0 #スコアの表示


class MySprite(pg.sprite.Sprite): #画像アニメーション
    def __init__(self):
        super(MySprite, self).__init__()
        self.images = list()
        self.images.append(pg.image.load('fig/pg_bg.png'))
        self.images.append(pg.image.load('fig/pg_ng2.png'))
        self.images.append(pg.image.load('fig/pg_bg3.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect() 

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1

class MUsic: #音楽
    def music():
        pg.mixer.init(frequency = 44100)   
        pg.mixer.music.load("music.wav")     
        pg.mixer.music.play(1)              
        while(1):
            a = input("Finish? --->")
            if(a is 'y'): break
        pg.mixer.music.stop()             
        return 0


class Screen: #画面生成
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird: #こうかとん生成
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Bomb: #爆弾生成
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    start_time = time.time()
    root = tk.Tk()
    root.withdraw()
    # 練習1
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習3
    kkt = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    bkd2 = Bomb((0, 0, 255), 10, (+4, +4), scr)

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        # 練習4
        kkt.update(scr)

        # 練習7
        bkd.update(scr)
        bkd2.update(scr)

        # 練習8
        if kkt.rct.colliderect(bkd.rct):
            end = time.time()
            tkm.showinfo("GAME OVER",f"{end - start_time:.3g}秒でGAVE OVER") # こうかとんrctが爆弾rctと重なったら
            return
        if kkt.rct.colliderect(bkd2.rct):
            end = time.time()
            tkm.showinfo("GAME OVER",f"{end - start_time:.3g}秒でGAVE OVER") # こうかとんrctが爆弾rctと重なったら
            return
        if pg.time.get_ticks() >= 30000: #30秒逃げ切った場合にメッセージ表示
            tkm.showinfo("GAME CLEAR","GAME CLEAR おめでとう！")
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    MUsic() #音楽再生
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()