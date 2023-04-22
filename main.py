import pgzrun
from pgzhelper import *

WIDTH = 800
HEIGHT = 600
BLUE = (163,232,254)
GREEN = (88,242,152)
velocity_y = 0
gravity = 1
runner = Actor('run__000', pos=[100, 400])
run_images = ['run__000','run__002','run__004']
runner.images = run_images
obstacles = []
obstacles_timeout = 0
def draw_sky():
    screen.draw.filled_rect(Rect(0,0,WIDTH,HEIGHT/2+100), BLUE)
def draw_ground():
    screen.draw.filled_rect(Rect(0, HEIGHT / 2 + 100, WIDTH, HEIGHT), GREEN)
def draw():
    draw_sky()
    draw_ground()
    runner.draw()
    for cactus in obstacles:
        cactus.draw()
def update():
    global velocity_y, obstacles_timeout
    runner.next_image()
    obstacles_timeout += 1
    if obstacles_timeout > 50:
        cactus = Actor('cactus', pos=[850, 430])
        obstacles.append(cactus)
        obstacles_timeout = 0
    for cactus in obstacles:
        cactus.x -= 8
    if keyboard.up:
        velocity_y = -15
    runner.y += velocity_y
    velocity_y += gravity
    if runner.y > 400:
        velocity_y = 0
        runner.y = 400
pgzrun.go()