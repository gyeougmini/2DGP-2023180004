from pico2d import *

open_canvas()

ball = load_image('ball21x21.png')
background = load_image('TUK_GROUND.png')
grass = load_image('grass.png')
character = load_image('run_animation.png')
samurai = load_image('SamuraiSheet.png')
sonic = load_image('sonic-sprite.png')

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

    ball.draw(x + 40, 60)

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
    
    ball.draw(x - 40, 60)
    
    update_canvas()

    
    frame = (frame + 1) % 8
    delay(0.05)

frame = 0

for x in range(300, 700, 5):
    clear_canvas()
    grass.draw(400, 30)

    samurai.clip_draw(
        frame * 128, 1280 - 128 * 5,
        128, 128,
        x, 125
    )

    update_canvas()

    frame = (frame + 1) % 6

    delay(0.05)


sonic_frames = [
    (1, 29), (35, 29), (67, 30), (98, 31), (131, 29),
    (162, 29), (193, 30), (230, 31), (268, 30)
]

frame = 0

for x in range(100, 700, 5):
    clear_canvas()
    grass.draw(400, 30)

    left, width = sonic_frames[frame]
    sonic.clip_draw(
        left, 325,
        width, 33,
        x, 111,
        width * 3, 33 * 3
    )

    update_canvas()

    frame = (frame + 1) % 9

    delay(0.05)



close_canvas()

