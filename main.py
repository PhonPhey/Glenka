import arcade
import header
import simpleaudio as sa
def music():
    wave_obj = sa.WaveObject.from_wave_file("/home/oksovskii/Downloads/Joakim_Karud_Something_New.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def draw_background():
    
    
    arcade.draw_rectangle_filled(header.SCREEN_WIDTH / 2, header.SCREEN_HEIGHT * 2 / 3,
                                 header.SCREEN_WIDTH - 1, header.SCREEN_HEIGHT * 2 / 3,
                                 arcade.color.SKY_BLUE)

    arcade.draw_rectangle_filled(header.SCREEN_WIDTH / 2, header.SCREEN_HEIGHT / 6,
                                 header.SCREEN_WIDTH - 1, header.SCREEN_HEIGHT / 3,
                                 arcade.color.DARK_SPRING_GREEN)


def main():
   
    arcade.open_window(header.SCREEN_WIDTH, header.SCREEN_HEIGHT, header.WIN_TITLE) 
    arcade.start_render()
    empty_sprite = arcade.Sprite()
    filename = "/home/oksovskii/Downloads/tex_stonee.png"
    ship_sprite = arcade.Sprite(filename, header.SCALE)
    arcade.set_background_color(arcade.color.GREEN)
    arcade.start_render()
    ship_sprite.draw()
    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    music()
    main()
    
    
    