'''Player module'''

from pygame import *
import header as hd
from header import *


class Player(sprite.Sprite):
    def __init__(self, x, y, player_sprt):
        sprite.Sprite.__init__(self)

        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.yvel = 0  # скорость вертикального перемещения

        self.onGround = False  # На земле ли я?

        # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startX = x
        self.startY = y

        self.sprt_cort = player_sprt
        self.image = player_sprt[1]
        # self.image.fill(Color(hd.COLOR))

        self.rect = Rect(x, y, hd.WIDTH, hd.HEIGHT)  # прямоугольный объект

    def update(self, left, right, up, platforms):

        if up and self.xvel != -MOVE_SPEED:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
                self.image = hd.SPRT_OSEL[2]

        if up and self.xvel != MOVE_SPEED:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
                self.image = hd.SPRT_OSEL[2]

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image = hd.SPRT_OSEL[1]

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image = hd.SPRT_OSEL[0]

        if not(left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            # если есть пересечение платформы с игроком
            if sprite.collide_rect(self, p):

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.image = hd.SPRT_OSEL[2]
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True          # и становится на что-то твердое
                    self.yvel = 0                 # и энергия падения пропадает
                    self.image = hd.SPRT_OSEL[0]

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадает
