import pygame as pg
from glob import glob
 
screen = pg.display.set_mode((200, 200))
pg.display.set_caption("Game")
clock = pg.time.Clock()
 
 
class Sprite(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.acount = 0
 
        # Coordinates for movement
        self.x = 0
        self.y = 0
        self.action = "idle"
 
        self.animation = [
            pg.image.load(f) for f in glob("..\\cat\\Idle *.png")]
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        print(self.image)
 
    def update(self):
        self.acount += 1
        if self.acount == len(self.animation):
            self.acount = 0
        self.image = self.animation[self.acount]
 
    def change_to(self, action):
        self.action = action
        self.animation = [
            pg.image.load(f) for f in glob(f"..\\cat\\{self.action} *.png")]
        return self.animation
 
 
g = pg.sprite.Group()
sprite = Sprite()
walk = sprite.change_to("walk")
jump = sprite.change_to("jump")
idle = sprite.change_to("idle")
 
g.add(sprite)
print(sprite)
 
loop = 1
jumpcount = 0
jumpstate = 0
walkstate = 0
while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                sprite.acount = 0
                sprite.animation = walk
                walkstate = 1
            if event.key == pg.K_LEFT:
                sprite.acount = 0
                sprite.animation = idle
                walkstate = 0
            if event.key == pg.K_UP:
                sprite.acount = 0
                sprite.animation = jump
                jumpstate = 1
    if jumpstate:
        jumpcount += 1
        if jumpcount < 4:
            sprite.rect.y -= 8
        else:
            sprite.rect.y += 4
        # print(jumpcount)
        if jumpcount > 8:
            jumpstate = 0
            jumpcount = 0
            if walkstate:
                sprite.change_to("walk")
            else:
                sprite.change_to("idle")
 
    screen.fill((0, 0, 0))
    g.draw(screen)
    g.update()
    pg.display.flip()
    clock.tick(30)
 
pg.quit()