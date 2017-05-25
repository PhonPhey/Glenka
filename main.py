import pygame as pg
from pygame import *
import pyganim as pga
import header as hd
import simpleaudio as sa
import os
from util import *
from player import *


def main():
    pg.init()
    pg.mixer.init()

    win = pg.display.set_mode(hd.DISPLAY)
    pg.display.set_caption(hd.WIN_TITLE)
    bg = pg.Surface((hd.WIN_WIDTH, hd.WIN_HEIGHT))

    bg.fill(pg.Color(hd.BACKGROUND_COLOR))

    hero = Player(55, 55, hd.SPRT_OSEL)  # создаем героя по (x,y) координатам
    left = right = False    # по умолчанию — стоим

    play_music(hd.PATH_SND, hd.SND_BGN)

    while 1:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                raise SystemExit("QUIT")

            elif e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            elif e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            elif e.type == KEYUP and e.key == K_RIGHT:
                right = False
            elif e.type == KEYUP and e.key == K_LEFT:
                left = False
            if hero.rect.x >= 800:
                hero.rect.x = -36
            elif hero.rect.x <= -40:
                hero.rect.x = 750

        win.blit(bg, (0, 0))
        win.blit(hd.TEX_STN, (23, 17))
        print(hero.rect.x)

        hero.update(left, right)  # передвижение
        hero.draw(win)  # отображение

        pg.display.update()


if __name__ == "__main__":
    main()
