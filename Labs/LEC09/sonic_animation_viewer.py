from pico2d import *

WIDTH, HEIGHT = 1200, 800

open_canvas(WIDTH, HEIGHT)

while True:
    clear_canvas()
    update_canvas()
    delay(0.1)

close_canvas()
