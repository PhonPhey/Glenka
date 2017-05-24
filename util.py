import pygame as pg
import os


def play_music(path_snd, snd_name):

    pg.mixer.init()
    pg.mixer.music.load(os.path.join(path_snd, snd_name + ".ogg"))
    pg.mixer.music.play(0)


def tex(path_tex, tex_name):

    return pg.image.load(os.path.join(path_tex, tex_name + ".png"))