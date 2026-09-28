# 원운동 -> 사각운동 -> 삼각운동을 끊김 없이 무한 반복
import math
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')

STEP = 5  # 한 프레임에 이동하는 거리(픽셀)

# 세 운동이 모두 지나가는 공통 시작점: (400, 550)
CENTER_X, CENTER_Y, RADIUS = 400, 300, 250
LEFT, RIGHT, BOTTOM, TOP = 50, 750, 50, 550


def draw_character(x, y):
    # 창 닫기 버튼을 누르면 종료
    for event in get_events():
        if event.type == SDL_QUIT:
            close_canvas()
            exit()

    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def move_line(x1, y1, x2, y2):
    # (x1, y1)에서 (x2, y2)까지 STEP 간격으로 직선 이동
    steps = max(1, int(math.hypot(x2 - x1, y2 - y1) / STEP))
    for i in range(steps):
        t = i / steps
        draw_character(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)


def move_circle():
    print('CIRCLE')
    # 맨 위(90도)에서 시작해 반시계 방향으로 한 바퀴
    steps = int(2 * math.pi * RADIUS / STEP)
    for i in range(steps):
        theta = math.radians(90) + 2 * math.pi * i / steps
        x = CENTER_X + RADIUS * math.cos(theta)
        y = CENTER_Y + RADIUS * math.sin(theta)
        draw_character(x, y)


def move_rectangle():
    print('RECTANGLE')
    # 윗변 가운데에서 시작해 시계 방향으로 한 바퀴
    move_line(CENTER_X, TOP, RIGHT, TOP)
    move_line(RIGHT, TOP, RIGHT, BOTTOM)
    move_line(RIGHT, BOTTOM, LEFT, BOTTOM)
    move_line(LEFT, BOTTOM, LEFT, TOP)
    move_line(LEFT, TOP, CENTER_X, TOP)


def move_triangle():
    print('TRIANGLE')
    # 꼭짓점 (400, 550) -> 왼쪽 아래 -> 오른쪽 아래 -> 꼭짓점
    move_line(CENTER_X, TOP, LEFT, BOTTOM)
    move_line(LEFT, BOTTOM, RIGHT, BOTTOM)
    move_line(RIGHT, BOTTOM, CENTER_X, TOP)


while True:
    move_circle()
    move_rectangle()
    move_triangle()
