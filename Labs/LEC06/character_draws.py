# 실습 과제 진행
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')


def move_circle():
    print("CIRCLE")

    character.draw(400, 300)
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        clear_canvas()

        character.draw(x, y)
        update_canvas()
        delay(0.01)


    update_canvas()
    pass

def move_rectangle():
    print("RECTANGLE") 
    pass

def move_triangle():
    print("TRIANGLE")
    pass



while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass


close_canvas()