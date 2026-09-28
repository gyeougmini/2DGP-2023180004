# 실습 과제 진행
import math
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.05)


def move_circle():

    character.draw(400, 300)
    for degree in range(0, 360, 5):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)

    update_canvas()

def move_top():
    for x in range(50, 750, 10):
        draw_character(x, 550)

def move_right():
    for y in range(550, 50, -10):
        draw_character(750, y)

def move_bottom():
    for x in range(750, 50, -10):
        draw_character(x, 50)

def move_left():
    for y in range(50, 550, 10):
        draw_character(50, y)


def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_leftdown():
    for i in range(0, 70):
        x = 400 - 350 * i / 70
        y = 300 - 250 * i / 70
        draw_character(x, y)

def move_tri_right():
    for x in range(50, 750, 10):
        draw_character(x, 50)

def move_leftup():
    for i in range(0, 70):
        x = 750 - 350 * i / 70
        y = 50 + 250 * i / 70
        draw_character(x, y)


def move_triangle():
    move_leftdown()
    move_tri_right()
    move_leftup()



while True:
    move_circle()
    move_rectangle()
    move_triangle()


close_canvas()