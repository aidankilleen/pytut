#pygame_helloworld.py
# By: Aidan
# Date: 24/11/2022


import pygame as pg

pg.init()

width = 640
height = 480

screen = pg.display.set_mode([width, height])

pg.display.set_caption("PyGame Hello World")

black = 20,20,20
screen.fill(black)

timer = pg.time.Clock()

# create the ball
ball = pg.image.load("intro_ball.gif")
ball_rect = ball.get_rect()

# game loop
finished = False

xdir = 1
ydir = 1

delay = 10

while not finished:

    for e in pg.event.get():

        print (e)

        if (e.type == pg.QUIT):
            finished = True
            break

        if (e.type == pg.KEYDOWN):
            if e.unicode == "+":
                delay = delay - 1
            elif e.unicode == "-":
                delay = delay + 1

    if ball_rect.left < 0 or ball_rect.right > width:
        xdir = -xdir

    if ball_rect.top < 0 or ball_rect.bottom > height:
        ydir = -ydir

    ball_rect = ball_rect.move([xdir,ydir])    

    screen.fill(black)
    screen.blit(ball, ball_rect)

    pg.display.flip()           # redisplay the screen

    #pg.time.delay(delay)
    timer.tick(300)

pg.quit()

