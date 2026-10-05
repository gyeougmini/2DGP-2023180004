from pico2d import *
import pico2d.pico2d as p2d

WIDTH, HEIGHT = 1200, 800
SCALE = 4
CENTER_X = 600
GROUND_Y = 300
FRAME_TIME = 0.1
REPEAT_COUNT = 5
PAUSE_TIME = 1.0

# 동작 목록: y, h 는 그 줄 전체가 같고(pico2d 좌표), 프레임마다 (x, w) 만 다르다
ANIMATIONS = [
    # 대기
    {'name': 'idle', 'y': 447, 'h': 39, 'frames': [(1, 29), (31, 26), (58, 28), (86, 30),
                                                   (118, 30), (150, 30), (182, 29), (211, 29),
                                                   (240, 29), (270, 24), (302, 29)]},
    # 걷기 → 달리기
    {'name': 'run', 'y': 407, 'h': 39, 'frames': [(8, 26), (37, 27), (65, 31), (97, 37),
                                                  (135, 32), (170, 32), (206, 26), (238, 24),
                                                  (263, 30), (295, 36), (334, 32), (370, 29)]},
    # 전력 질주
    {'name': 'dash', 'y': 361, 'h': 43, 'frames': [(1, 33), (39, 35), (89, 35), (130, 34),
                                                   (181, 34), (228, 33)]},
    # 스핀
    {'name': 'spin', 'y': 325, 'h': 33, 'frames': [(1, 29), (35, 29), (67, 30), (98, 31),
                                                   (131, 29), (162, 29), (193, 30), (230, 31),
                                                   (268, 30)]},
    # 구르기
    {'name': 'ball', 'y': 292, 'h': 27, 'frames': [(1, 30), (36, 29), (70, 29), (105, 29),
                                                   (139, 29), (174, 29)]},
    # 고속 달리기
    {'name': 'super_run', 'y': 251, 'h': 36, 'frames': [(1, 29), (36, 30), (74, 31), (111, 31),
                                                        (149, 30), (186, 31)]},
    # 필아웃
    {'name': 'peel_out', 'y': 207, 'h': 35, 'frames': [(1, 29), (36, 30), (72, 39), (123, 39),
                                                       (172, 39), (218, 38)]},
    # 여러 자세 / 넘어짐
    {'name': 'misc', 'y': 154, 'h': 45, 'frames': [(1, 24), (31, 29), (65, 20), (90, 25),
                                                   (119, 25), (149, 20), (184, 40), (232, 39)]},
    # 밀기 / 브레이크
    {'name': 'push', 'y': 108, 'h': 40, 'frames': [(1, 27), (31, 31), (64, 31), (99, 33),
                                                   (136, 32), (176, 33), (217, 33), (254, 33)]},
    # 놀람 / 피격
    {'name': 'hurt', 'y': 56, 'h': 43, 'frames': [(6, 34), (49, 34), (96, 23), (125, 23)]},
]


def clear_white():
    # pico2d 의 clear_canvas() 는 회색으로 지우므로 흰색으로 직접 지운다
    SDL_SetRenderDrawColor(p2d.renderer, 255, 255, 255, 255)
    SDL_RenderClear(p2d.renderer)


def draw_frame(x, y, w, h):
    # 바닥선 GROUND_Y 에 발을 맞추고, 가로는 화면 가운데에 맞춰 SCALE 배로 그린다
    sheet.clip_draw_to_origin(x, y, w, h,
                              CENTER_X - w * SCALE // 2, GROUND_Y,
                              w * SCALE, h * SCALE)


def draw():
    anim = ANIMATIONS[anim_index]
    x, w = anim['frames'][frame]
    draw_frame(x, anim['y'], w, anim['h'])


def update():
    global anim_index, frame, repeat, paused, pause_start
    if paused:
        # 1초가 지나면 다음 동작으로 넘어간다 (마지막 동작이면 그대로 멈춘다)
        if get_time() - pause_start >= PAUSE_TIME and anim_index < len(ANIMATIONS) - 1:
            anim_index += 1
            frame = 0
            repeat = 0
            paused = False
        return
    frame += 1
    if frame == len(ANIMATIONS[anim_index]['frames']):
        repeat += 1
        if repeat == REPEAT_COUNT:
            frame -= 1  # 정지하는 동안 마지막 프레임 유지
            paused = True
            pause_start = get_time()
        else:
            frame = 0


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

anim_index = 0
frame = 0
repeat = 0
paused = False
pause_start = 0.0

running = True
while running:
    handle_events()
    clear_white()
    draw()
    update_canvas()
    update()
    delay(FRAME_TIME)

close_canvas()
