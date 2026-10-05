from pico2d import *
import pico2d.pico2d as p2d

WIDTH, HEIGHT = 1200, 800


def clear_white():
    # pico2d 의 clear_canvas() 는 회색으로 지우므로 흰색으로 직접 지운다
    SDL_SetRenderDrawColor(p2d.renderer, 255, 255, 255, 255)
    SDL_RenderClear(p2d.renderer)


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

running = True
while running:
    handle_events()
    clear_white()
    # 대기 동작 첫 프레임: x=1, w=29, pico_y=447, h=39
    sheet.clip_draw_to_origin(1, 447, 29, 39, WIDTH // 2, HEIGHT // 2)
    update_canvas()
    delay(0.1)

close_canvas()
