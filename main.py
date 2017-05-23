import pygame as pg
import header as hd


def play_music(path):
  
    pg.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pg.mixer.music.load(path)
    pg.mixer.music.play(0)
        #for m in pg.event.get():
            #if m.type == QUIT:
                #exit (0)

def main():
    pg.init()
    win = pg.display.set_mode(hd.DISPLAY)
    pg.display.set_caption(hd.WIN_TITLE)
    bg = pg.Surface((hd.WIN_WIDTH, hd.WIN_HEIGHT))

    bg.fill(pg.Color(hd.BACKGROUND_COLOR))
    fon = pg.sprite.Sprite('')
    fon.draw()
    pg.sprite.Sprite.update()

    """while 1:
        for e in pg.event.get():
            if e.type == QUIT:
                raise()SystemExit, "QUIT"
        screen.blit(bg, (0,0))
        pg.display.update()"""

if __name__ == "__main__":
    play_music()
    #main()
