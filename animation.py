import pygame as pg
from pygame.locals import *
import  math

TICKS = 60 
BACKGROUND = (220, 220, 220)
SIZE = (800, 600)

def ball_update(ball, time):
        ball['x'] += int(ball['speedX']*time)
        ball['y'] += int(ball['speedY']*time)
        ball['angle'] += ball['angleSpeed']*time
       # ball['angle'] -= 2*math.pi*int(ball['angle']/2*math.pi)

def ball_colide(ball, wall):
        if ball['x']-ball['rad'] < 0:
            ball['x'] = ball['rad']
            ball['speedX'] = -ball['speedX']
        elif ball['x'] + ball['rad'] > 800:
            ball['x'] = 800-ball['rad']
            ball['speedX'] = -ball['speedX']
        if ball['y'] - ball['rad'] < 0:
            ball['y'] = ball['rad']
            ball['speedY'] = -ball['speedY']
        elif ball['y'] + ball['rad'] > 600:
            ball['y'] = 600-ball['rad']
            ball['speedY'] = -ball['speedY']

        if ball['y'] - ball['rad'] < wall['y']+wall['height']/2:
            if abs(ball['speedY']-wall['speedY'])<1e-6:
                ball['speedY'] = -ball['speedY']
            else:
                ball['speedY'] = -ball['speedY'] #+wall['speedY']
            ball['y'] = int(wall['y']+wall['height']/2 + ball['rad'])

def ball_draw(ball):
    pg.draw.circle(screen, ball['color'], (ball['x'], ball['y']), ball['rad'])
    if (ball['angleSpeed'] != 0):
        start = (ball['x']+math.cos(ball['angle'])*ball['rad'],
                 ball['y']+math.sin(ball['angle'])*ball['rad'])
        end = (ball['x']+math.cos(ball['angle']+math.pi)*ball['rad'],
               ball['y']+math.sin(ball['angle']+math.pi)*ball['rad'])
        pg.draw.line(screen, (0, 0, 0), start, end)

def wall_update(wall, time):
        wall['y'] += wall['speedY']*time
        
        if wall['y']-wall['height']/2 < 0:
            wall['y'] = wall['height']/2
            wall['speedY'] = -wall['speedY']
        elif wall['y']+wall['height']/2 > 400:
            wall['y'] = 400 - wall['height']/2
            wall['speedY'] = -wall['speedY']


def wall_draw(wall):
    x, y, height, width = wall['x'], wall['y'], wall['height'], wall['width']
    rect = pg.Rect((x-width/2, y-height/2), (width, height))
    pg.draw.rect(screen, wall['color'], rect)

pg.init()
pg.display.set_caption('Animation by Ryazanov Maxim')
screen = pg.display.set_mode(SIZE)

ball = {'x': 500,
        'y': 500,
        'rad': 50,
        'color': (200, 150, 100),
        'angleSpeed': math.pi,
        'speedX': 300,
        'speedY': 300,
        'angle': 0,
        }

wall = {'x': SIZE[0]/2,
        'y': 200,
        'height': 200,
        'width': SIZE[0],
        'color': (100, 0, 0),
        'speedY': 150,
        }

running = True
clock = pg.time.Clock()
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    secs = clock.tick(TICKS)/1000
        
    ball_update(ball, secs)
    wall_update(wall, secs)

    ball_colide(ball, wall)

    screen.fill(BACKGROUND)
    wall_draw(wall)
    ball_draw(ball)
    pg.display.update()

pg.quit()
