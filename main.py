import pygame as pg
from pygame import *
import pyganim as pga
import header as hd
import simpleaudio as sa
import os
from util import *
from player import *
import platform as plt
import res.levels as lvl


def main():
    pg.init()
    pg.mixer.init()

    win = pg.display.set_mode(hd.DISPLAY)
    pg.display.set_caption(hd.WIN_TITLE)
    bg = pg.Surface((hd.WIN_WIDTH, hd.WIN_HEIGHT))

    bg.fill(pg.Color(hd.BACKGROUND_COLOR))

    # создаем героя по (x,y) координатам
    hero = Player(55, 55, hd.SPRT_OSEL)

    left = right = False    # по умолчанию — стоим
    up = False

    timer = pg.time.Clock()

    entities = pg.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    entities.add(hero)

    play_music(hd.PATH_SND, hd.SND_BGN)

    while 1:
        # Максимальное кол-во FPS
        timer.tick(60)

        for e in pg.event.get():
            if e.type == pg.QUIT:
                raise SystemExit("QUIT")

            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False

            if hero.rect.x >= 800:
                hero.rect.x = -36
            elif hero.rect.x <= -40:
                hero.rect.x = 750

        win.blit(bg, (0, 0))

        x = y = 0  # координаты
        for row in lvl.LEVEL_0:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = plt.Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)

                x += hd.PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += hd.PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

        # print(hero.rect.x)

        hero.update(left, right, up, platforms)  # передвижение
        entities.draw(win)  # отображение

        pg.display.update()


if __name__ == "__main__":
    main()
