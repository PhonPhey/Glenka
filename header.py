''' Header file '''

from util import *
import pyganim as pga

WIN_WIDTH = 800
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
WIN_TITLE = "GLENKA"

BACKGROUND_COLOR = "#bef7e9"

SCALE = 1

PATH_TEX = "res/tex"
PATH_SPRT = "res/sprt/"
PATH_SND = "res/snd"

# Sprite const
SPRT_RDIO_LMN = [load_sprt(PATH_SPRT, "sprt_radio_limon", "sprt_radio_limon_0"), load_sprt(PATH_SPRT, "sprt_radio_limon", "sprt_radio_limon_1"), load_sprt(
    PATH_SPRT, "sprt_radio_limon", "sprt_radio_limon_2"), load_sprt(PATH_SPRT, "sprt_radio_limon", "sprt_radio_limon_3")]

SPRT_OSEL = [load_sprt(PATH_SPRT, "sprt_osel", "sprt_osel_0"), load_sprt(PATH_SPRT, "sprt_osel", "sprt_osel_1"), load_sprt(
    PATH_SPRT, "sprt_osel", "sprt_osel_2"), load_sprt(PATH_SPRT, "sprt_osel", "sprt_osel_3")]


# Texture const
TEX_STN = load_tex(PATH_TEX, "tex_stone")

# Sound const
SND_BGN = "begin_song"

# player const

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
