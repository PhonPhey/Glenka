import pygame as pg
import pyganim as pga
import os


def play_music(path_snd, snd_name):

    pg.mixer.init()
    pg.mixer.music.load(os.path.join(path_snd, snd_name + ".ogg"))
    pg.mixer.music.play(0)


def load_tex(path_tex, tex_name):

    return pg.image.load(os.path.join(path_tex, tex_name + ".png"))


def load_sprt(path_sprt, spec_path_sprt, sprt_name):
    return pg.image.load(os.path.join(path_sprt + spec_path_sprt, sprt_name + ".png"))


def sprt(path_sprt, sprt_name, widht, height):
    block_list = pg.sprite.Group()
