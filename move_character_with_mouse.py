from pico2d import *
from random import randint

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def get_xy(t):
    global x, y, origin_x, origin_y

    if t >= 1:
        origin_x = x
        origin_y = y
        t = 1
    x = (1 - t) * origin_x + t * mx
    y = (1 - t) * origin_y + t * my

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = 0

running = 1
mx, my = x, y = origin_x, origin_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if mx == x:
        mx, my = randint(30, TUK_WIDTH - 30), randint(80, TUK_HEIGHT - 80)
        t = 0.0

    if mx < x:
        running = 1
    else:
        running = 2

    get_xy(t)
    t += 0.05
    hand_arrow.draw(mx, my)
    if running == 1:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif running == 2:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.1)
    handle_events()

close_canvas()