from pico2d import *
import game_framework
import game_world
import title_mode
import pause_mode
from boy import Boy
from grass import Grass


def handle_events():
    global boy

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
        else:
            boy.handle_event(event)



def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()  # 다시 들어올 때 소년/볼이 중복되지 않도록 월드를 비움

def pause():
    pass

def resume():
    # 정지 중에 뗀 방향키는 소년에게 전달되지 않으므로, 눌린 키를 초기화해서 계속 달리지 않게 함
    boy.pressed_keys.clear()
    if boy.state == 'RUN':
        boy.dir = 0
        boy.stop_run()
