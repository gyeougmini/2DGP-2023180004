from pico2d import *

WIDTH, HEIGHT = 1200, 800


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(WIDTH, HEIGHT)

running = True
while running:
    handle_events()
    clear_canvas()
    update_canvas()
    delay(0.1)

close_canvas()
