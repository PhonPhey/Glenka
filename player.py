'''Player module'''

from pygame import *
import header as hd


class Player(sprite.Sprite):
    def __init__(self, x, y, player_sprt):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.sprt_cort = player_sprt
        self.image = player_sprt[0]
        #self.image.fill(Color(hd.COLOR))
        self.rect = Rect(x, y, hd.WIDTH, hd.HEIGHT)  # прямоугольный объект

    def update(self,  left, right):
        if left:
            self.xvel = -hd.MOVE_SPEED  # Лево = x- n

        elif right:
            self.xvel = hd.MOVE_SPEED  # Право = x + n

        elif not(left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        self.rect.x += self.xvel  # переносим свои положение на xvel

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))
    