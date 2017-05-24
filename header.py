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
PATH_SPRT = "res/sprt"
PATH_SND = "res/snd"

#Sprite const
SPRT_RDIO_LMN = pga.getImagesFromSpriteSheet(rows=1, cols=3)

#Texture const
TEX_STN = load_tex(PATH_TEX, "tex_stone")

#Sound const
SND_BGN = "begin_song"
