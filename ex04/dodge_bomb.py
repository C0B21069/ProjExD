import pygame as pg
import sys
from random import randint

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

    #練習6
    vx, vy = +1, +1

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
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy) #練習6 
        scrn_sfc.blit(bomb_sfc, bomb_rct) #練習5

        #練習8
        if tori_rct.colliderect(bomb_rct): #こうかとんrctが爆弾rctと重なったら
            return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() #初期化
    main() 
    pg.quit() #初期化の解除
    sys.exit() #プログラムの終了