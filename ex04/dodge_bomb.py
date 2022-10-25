import pygame as pg
import sys
from random import randint
import time
import tkinter as tk
import tkinter.messagebox as tkm

#練習7
def check_bound(obj_rct, scr_rct):
    """
    obj_rct:こうかとんrct,または,爆弾
    scr_rct:スクリーンrct
    領域内:+1/領域外:-1
    """
    
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    start_time = time.time()
    #時間経過の表示
    # elapsed_time = int(time.time() - start_time)
    # elapsed_hour = elapsed_time // 3600
    # elapsed_minute = (elapsed_time % 3600) // 60
    # elapsed_second = (elapsed_time % 3600 % 60)
    # root = tk.Tk()
    # root.title("経過時間")
    # root.geometry("100x100")
    # label = tk.Label(root, text = str(elapsed_hour).zfill(2) + ":" + str(elapsed_minute).zfill(2) +
    #                               ":" + str(elapsed_second).zfill(2),
    #                               font = ("Ricty Diminished", 20)
    #                  )               

    root = tk.Tk()
    root.withdraw()
    #練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #練習3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #練習5
    bomb_sfc = pg.Surface((20,20)) #空のSurface
    bomb_sfc.set_colorkey((0, 0, 0)) #爆弾の四隅の黒い部分を透過させる
    pg.draw.circle(bomb_sfc, (255, 40, 40), (10, 10), 10) #円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    #爆弾2個目
    bomb_sfc2 = pg.Surface((20,20))
    bomb_sfc2.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc2, (0, 255, 40), (10, 10), 10)
    bomb_rct2 = bomb_sfc2.get_rect()
    bomb_rct2.centerx = randint(0, 1500)
    bomb_rct2.centery = randint(0, 800)

    #練習6
    vx, vy = +1, +1
    vx2, vy2 = +1, +1

    clock = pg.time.Clock() 

    #練習2
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) 
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return

        #練習4
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += 1
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]:
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1

        scrn_sfc.blit(tori_sfc, tori_rct) #練習3

        #練習7
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        if vx < 0:  #爆弾の加速
            vx -= 0.0005
        elif vx > 0:
            vx += 0.0005
        if vy < 0:
            vy -= 0.0005
        elif vy > 0:
            vy += 0.0005
        vx *= yoko
        vy *= tate

        yoko2, tate2 = check_bound(bomb_rct2, scrn_rct)
        if vx2 < 0: #爆弾の加速
            vx2 -= 0.0005
        elif vx2 > 0:
            vx2 += 0.0005
        if vy2 < 0:
            vy2 -= 0.0005
        elif vy2 > 0:
            vy2 += 0.0005
        vx2 *= yoko2
        vy2 *= tate2

        bomb_rct.move_ip(vx, vy) #練習6 
        scrn_sfc.blit(bomb_sfc, bomb_rct) #練習5

        #爆弾2個目
        bomb_rct2.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc2, bomb_rct2)

        #練習8
        if tori_rct.colliderect(bomb_rct): #こうかとんrctが爆弾rctと重なったら
            end = time.time()
            tkm.showinfo("GAME OVER",f"{end - start_time:.3g}秒でGAVE OVER")
            return
        
        if tori_rct.colliderect(bomb_rct2): #こうかとんrctが爆弾rctと重なったら
            end = time.time()
            tkm.showinfo("GAME OVER",f"{end - start_time:.3g}秒でGAME OVER")
            return
        
        #成功した時の表示
        if pg.time.get_ticks() >= 30000:
            tkm.showinfo("GAME CLEAR","GAME CLEAR おめでとう！")
            return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() #初期化
    main() 
    pg.quit() #初期化の解除
    sys.exit() #プログラムの終了