import pygame as pg
import header as hd
import simpleaudio as sa
import os

def play_music(path_snd, snd_name):

    pg.mixer.init()
    pg.mixer.music.load(os.path.join(path_snd, snd_name))
    pg.mixer.music.play(0)

def main():
    pg.init()
    pg.mixer.init()

    win = pg.display.set_mode(hd.DISPLAY)
    pg.display.set_caption(hd.WIN_TITLE)
    bg = pg.Surface((hd.WIN_WIDTH, hd.WIN_HEIGHT))

    bg.fill(pg.Color(hd.BACKGROUND_COLOR))
    play_music(hd.PATH_SND, "begin_song.ogg")

    while 1:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                raise Exception(SystemExit, "QUIT")
        win.blit(bg, (0, 0))
        pg.display.update()

if __name__ == "__main__":
    main()
