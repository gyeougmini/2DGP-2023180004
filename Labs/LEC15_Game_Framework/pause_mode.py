import game_framework
from pico2d import *
import game_world


def init():
    pass

def finish():
    pass

def update():
    pass  # 게임 월드를 업데이트하지 않으므로 모든 움직임이 멈춤

def render():
    clear_canvas()
    game_world.render()  # 멈춘 플레이 화면을 그대로 보여줌
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()

def pause():
    pass

def resume():
    pass
