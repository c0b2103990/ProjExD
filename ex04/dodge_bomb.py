import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    bg_sfc  = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    scrn_sfc.blit(bg_sfc, bg_rct)
    # tori_sfc = pg.image.load("fig/8.png")
    # tori_rct = tori_sfc.get_rect()
    # tori_rct.center = 700, 400
    # scrn_sfc.blit(tori_sfc, tori_rct)

    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(0.5)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()