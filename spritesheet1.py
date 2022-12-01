import pygame as pg



class Spritesheet:
    def __init__(self, file):
        self.sheet = pg.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pg.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey((0,0,0))
        return sprite

pg.init()

character_spritesheet = Spritesheet('img/character.png')

width = 640
height = 480

screen = pg.display.set_mode([width, height])

pg.display.set_caption("PyGame Hello World")

black = 20,20,20
screen.fill(black)

timer = pg.time.Clock()

image = character_spritesheet.get_sprite(0, 0, 32, 32)


finished = False

while not finished:

    for e in pg.event.get():

        print (e)

        if (e.type == pg.QUIT):
            finished = True
            break

    screen.fill((0,0,0))
    screen.blit(image, (0,0,32,32))

    pg.display.flip()           # redisplay the screen

    timer.tick(300)

pg.quit()




