import pygame as pg
from pygame.locals import *
import random, math

TICKS = 30
BACKGROUND = (220, 220, 220)
SIZE = (800, 600)

class Ball(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, radius=50):
        super(Ball, self).__init__()
        self.x = x
        self.y = y
        self.speedX = 300
        self.speedY = 300
        self.radius = radius
        self.color = (200, 150, 100)

    def update(self, pressed_keys, time):
        #if pressed_keys[K_UP]:
         #   self.rect.move_ip(0, -self.speedY*time)
        #if pressed_keys[K_DOWN]:
         #   self.rect.move_ip(0, self.speedY*time)
        #if pressed_keys[K_LEFT]:
         #   self.rect.move_ip(-self.speedX*time, 0)
        #if pressed_keys[K_RIGHT]:
         #   self.rect.move_ip(self.speedX*time, 0)

        self.x += int(self.speedX*time)
        self.y += int(self.speedY*time)

        if self.x-self.radius < 0:
            self.x = self.radius
            self.speedX = -self.speedX
        elif self.x+self.radius > 800:
            self.x = 800-self.radius
            self.speedX = -self.speedX
        if self.y-self.radius < 0:
            self.y = self.radius
            self.speedY = -self.speedY
        elif self.y+self.radius > 600:
            self.y = 600-self.radius
            self.speedY = -self.speedY

        if self.y-self.radius<wall.rect.bottom+wall.speed*time:
            self.speedY = -self.speedY
            self.y = int(wall.rect.bottom+self.radius-wall.speed*time)

    def draw(self):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Wall(pg.sprite.Sprite):
    def __init__(self):
        super(Wall, self).__init__()
        self.surf = pg.Surface((SIZE[0], 200))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.speed = 300

    def update(self, time):
        self.rect.move_ip(0, -self.speed*time)

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = -self.speed
        elif self.rect.bottom > 400:
            self.rect.bottom = 400
            self.speed = -self.speed
        

pg.init()
pg.display.set_caption('Animation by Ryazanov Maxim')
screen = pg.display.set_mode(SIZE)
ball = Ball(400, 500)
wall = Wall()
running = True
clock = pg.time.Clock()
objects = pg.sprite.Group()
objects.add(wall)

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    secs = clock.tick(TICKS)/1000
    #if pg.sprite.spritecollideany(ball, pg.sprite.Group(wall)):
       # ball.speedY = -ball.speedY
        
    pressed_keys = pg.key.get_pressed()
    ball.update(pressed_keys, time=secs)
    wall.update(time=secs)

    screen.fill(BACKGROUND)
    for obj in objects:
        screen.blit(obj.surf, obj.rect)
    ball.draw()
    pg.display.flip()

pg.quit()
