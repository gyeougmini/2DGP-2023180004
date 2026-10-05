from pico2d import *
import pico2d.pico2d as p2d

WIDTH, HEIGHT = 1200, 800
SCALE = 4
CENTER_X = 600
GROUND_Y = 300
FRAME_TIME = 0.1

# 동작 하나 = (pico_y, h, [(x, w), ...])
# 1 대기
IDLE = (447, 39, [(1, 29), (31, 26), (58, 28), (86, 30), (118, 30), (150, 30),
                  (182, 29), (211, 29), (240, 29), (270, 24), (302, 29)])
# 2 달리기
RUN = (407, 39, [(8, 26), (37, 27), (65, 31), (97, 37), (135, 32), (170, 32), (206, 26),
                 (238, 24), (263, 30), (295, 36), (334, 32), (370, 29)])
# 3 전력 질주
DASH = (361, 43, [(1, 33), (39, 35), (89, 35), (130, 34), (181, 34), (228, 33)])
# 4 스핀
SPIN = (325, 33, [(1, 29), (35, 29), (67, 30), (98, 31), (131, 29), (162, 29),
                  (193, 30), (230, 31), (268, 30)])


def clear_white():
    # pico2d 의 clear_canvas() 는 회색으로 지우므로 흰색으로 직접 지운다
    SDL_SetRenderDrawColor(p2d.renderer, 255, 255, 255, 255)
    SDL_RenderClear(p2d.renderer)


def draw_frame(x, y, w, h):
    # 바닥선 GROUND_Y 에 발을 맞추고, 가로는 화면 가운데에 맞춰 SCALE 배로 그린다
    sheet.clip_draw_to_origin(x, y, w, h,
                              CENTER_X - w * SCALE // 2, GROUND_Y,
                              w * SCALE, h * SCALE)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(WIDTH, HEIGHT)
sheet = load_image('sonic-sprite.png')

current = SPIN
frame = 0

running = True
while running:
    handle_events()
    clear_white()
    y, h, frames = current
    x, w = frames[frame]
    draw_frame(x, y, w, h)
    update_canvas()
    frame = (frame + 1) % len(frames)
    delay(FRAME_TIME)

close_canvas()
