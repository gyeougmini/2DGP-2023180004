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

for count in range(5):
    for x in range(0, 800, 20):
        clear_canvas()
        background.draw(400, 300, 800, 600)


        character.clip_draw(
            frame * 100, 0,
            100, 100,
            x, 90,
            200, 200
        )

        ball.draw(x + 40, 60)

        update_canvas()


        frame = (frame + 1) % 8


        delay(0.05)

    for x in range(800, 0, -20):
        clear_canvas()
        background.draw(400, 300, 800, 600)


        character.clip_composite_draw(
            frame * 100, 0,
            100, 100,
            0, 'h',
            x, 90,
            200, 200
        )

        ball.draw(x - 40, 60)

        update_canvas()


        frame = (frame + 1) % 8
        delay(0.05)

# 마지막 화면을 그대로 둔 채 1초 정지한 뒤 samurai로 전환
delay(1)

frame = 0

# 오른쪽 → 왼쪽을 3번 반복하면 방향 전환이 총 5번
for count in range(3):
    for x in range(300, 700, 10):
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

    for x in range(700, 300, -10):
        clear_canvas()
        grass.draw(400, 30)

        samurai.clip_composite_draw(
            frame * 128, 1280 - 128 * 5,
            128, 128,
            0, 'h',
            x, 125,
            128, 128
        )

        update_canvas()

        frame = (frame + 1) % 6

        delay(0.05)

# 마지막 화면을 그대로 둔 채 1초 정지한 뒤 sonic으로 전환
delay(1)


sonic_frames = [
    (1, 29), (35, 29), (67, 30), (98, 31), (131, 29),
    (162, 29), (193, 30), (230, 31), (268, 30)
]

frame = 0

# 오른쪽 → 왼쪽을 3번 반복하면 방향 전환이 총 5번
for count in range(3):
    for x in range(100, 700, 15):
        clear_canvas()
        grass.draw(400, 30)

        # 화면 가운데(x=400)에서 가장 크고(5배), 양 끝(x=100, 700)에서 가장 작게(1배)
        scale = 1 + 4 * (1 - abs(x - 400) / 300)

        left, width = sonic_frames[frame]
        sonic.clip_draw(
            left, 325,
            width, 33,
            x, 61 + 33 * scale / 2,
            width * scale, 33 * scale
        )

        update_canvas()

        frame = (frame + 1) % 9

        delay(0.05)

    for x in range(700, 100, -15):
        clear_canvas()
        grass.draw(400, 30)

        scale = 1 + 4 * (1 - abs(x - 400) / 300)

        left, width = sonic_frames[frame]
        sonic.clip_composite_draw(
            left, 325,
            width, 33,
            0, 'h',
            x, 61 + 33 * scale / 2,
            width * scale, 33 * scale
        )

        update_canvas()

        frame = (frame + 1) % 9

        delay(0.05)

# 마지막 화면을 그대로 둔 채 1초 정지한 뒤 점프하는 sonic으로 전환
delay(1)


sonic_jump_frames = [
    (1, 24), (31, 29), (65, 20), (90, 25), (119, 25), (149, 20)
]

frame = 0

for count in range(3):
    for i in range(0, 61):
        clear_canvas()
        grass.draw(400, 30)


        t = i / 60
        jump = 300 * 4 * t * (1 - t)

        left, width = sonic_jump_frames[frame]
        sonic.clip_draw(
            left, 155,
            width, 44,
            400, 61 + 44 + jump,
            width * 2, 44 * 2
        )

        update_canvas()

        frame = (frame + 1) % 6

        delay(0.05)



close_canvas()

