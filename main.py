import pygame as pg
import pyganim as pga
import header as hd
import simpleaudio as sa
import os
from util import *


def main():
    pg.init()
    pg.mixer.init()

    win = pg.display.set_mode(hd.DISPLAY)
    pg.display.set_caption(hd.WIN_TITLE)
    bg = pg.Surface((hd.WIN_WIDTH, hd.WIN_HEIGHT))

    bg.fill(pg.Color(hd.BACKGROUND_COLOR))
    play_music(hd.PATH_SND, hd.SND_BGN)


    while 1:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                raise Exception(SystemExit, "QUIT")
        win.blit(bg, (0, 0))
        win.blit(hd.TEX_STN, (23, 17))



        pg.display.update()

if __name__ == "__main__":
    main()
