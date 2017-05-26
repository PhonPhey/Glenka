""" Module for Platform class """

import pygame as pg
from header import *


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.blit(TEX_STN, (x, y))
        self.rect = pg.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
