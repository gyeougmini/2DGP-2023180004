from pico2d import *

open_canvas()

background = load_image('TUK_GROUND.png')
grass = load_image('grass.png')
character = load_image('run_animation.png')

# fill here
frame = 0

for x in range(0, 800, 5):
    clear_canvas()
    background.draw(400, 300, 800, 600)

    
    character.clip_draw(
        frame * 100, 0, 
        100, 100,
        x, 90
    )

    update_canvas()

    
    frame = (frame + 1) % 8


    delay(0.05)

for x in range(800, 0, -5):
    clear_canvas()
    background.draw(400, 300, 800, 600)

    
    character.clip_composite_draw(
        frame * 100, 0, 
        100, 100,
        0, 'h',
        x, 90,
        100, 100
    )
    
    update_canvas()

    
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()

