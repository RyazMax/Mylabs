import pygame as pg
from pygame.locals import *
import  math

# TICKS - количество тиков в секунду
# BACKGROUND - цвет фона
# SIZE - размер поля
# LINE_W - толщина линии
# DIST_K - коэфициент расстояния до дуги шара

# ball_update(ball, time) - обновление координат шара
# ball_colide(ball, wall) - проверка столкновений шара
# draw_arc(ball, phase) - отрисовка дуги на шаре
# draw_line(ball, phase) - отрисовка линии на шаре
# draw_ball(ball) - отрисовка шара
# wall_update(wall, time) - обновление координат стены)
# wall_draw(wall) - отрисовка стены

TICKS = 60 
BACKGROUND = (220, 220, 220)
SIZE = (800, 600)
LINE_W = 2
DIST_K = 1.4

def ball_update(ball, time):
    # Обновление координат шара
    # ball - словарь свойств шара
    # time - время, прошедшое с последнего обновления

    ball['x'] += int(ball['speedX']*time)
    ball['y'] += int(ball['speedY']*time)
    ball['angle'] += ball['angleSpeed']*time # Обновление угла поворота

    # Взятие модуля угла для избежания переполнения
    ball['angle'] -= 2*math.pi*int(ball['angle']/(2*math.pi))

def ball_colide(ball, wall):
    # Обработка столкновения шара и стены
    # ball - словать со свойствами шара
    # wall - словарь со свойствами стены
    # Столкновение шара с границами поля
    if ball['x']-ball['rad'] < 0:
        ball['x'] = ball['rad']
        ball['speedX'] = -ball['speedX']
    elif ball['x'] + ball['rad'] > SIZE[0]:
        ball['x'] = SIZE[0]-ball['rad']
        ball['speedX'] = -ball['speedX']
    if ball['y'] - ball['rad'] < 0:
        ball['y'] = ball['rad']
        ball['speedY'] = -ball['speedY']
    elif ball['y'] + ball['rad'] > SIZE[1]:
        ball['y'] = SIZE[1]-ball['rad']
        ball['speedY'] = -ball['speedY']

    # Cтолкновение со стеной
    if ball['y'] - ball['rad'] < wall['y']+wall['height']/2:
        if abs(ball['speedY']-wall['speedY'])<1e-6:
            ball['speedY'] = -ball['speedY']
        else:
            ball['speedY'] = -ball['speedY'] #+wall['speedY']
        ball['y'] = int(wall['y']+wall['height']/2 + ball['rad'])


def draw_arc(ball, phase):
    # Отрисовка дуги на шаре
    # ball - словарь со свойствами шара
    # phase - начальный угол поворота дуги

    phase = ball['angle']+phase
    H = ball['rad'] * DIST_K # Расстояние до центра мнимого шара
    
    # fi - угол между линией соединяющей окружности и радиусом опущенным в точку их пересечения
    # csFi - косинус этого угла
    csFi = H/(2*ball['rad'])
    fi = math.acos(csFi)

    # Координаты центра мнимой окружности
    newX = ball['x']+math.cos(phase)*H
    newY = ball['y']+math.sin(phase)*H
    rect = pg.Rect((newX-ball['rad'], newY-ball['rad']), (ball['rad']*2, ball['rad']*2))
    pg.draw.arc(screen, (0, 0, 0), rect, math.pi - phase - fi, math.pi +
                        - phase + fi, LINE_W)

def draw_line(ball, phase):
    # Отрисовка линии на шаре
    # ball - словарь со свойствами шара
    # phase - начальный угол поворота дуги

    phase += ball['angle']

    # Концы линии
    start = (ball['x']+math.cos(phase)*ball['rad'],
                 ball['y']+math.sin(phase)*ball['rad'])
    end = (ball['x']+math.cos(phase+math.pi)*ball['rad'],
               ball['y']+math.sin(phase+math.pi)*ball['rad'])
    pg.draw.line(screen, (0, 0, 0), start, end, LINE_W)


def ball_draw(ball):
    # Отрисовка шара и линий на нем
    # ball - словарь со свойствами шара

    pg.draw.circle(screen, ball['color'], (ball['x'], ball['y']), ball['rad'])
    if (ball['angleSpeed'] != 0):
        draw_line(ball, 0)
        draw_line(ball, math.pi/2)
        draw_arc(ball, 0)
        draw_arc(ball, math.pi)

def wall_update(wall, time):
    # Обновление координат стены
    # wall - словарь со свойствами стены
    # time - время прошедшее с последнего обновления
    # border - граница опускания стены

    border = int(SIZE[1]/2)+100
    wall['y'] += wall['speedY']*time
     
    if wall['y']-wall['height']/2 < 0:
        wall['y'] = wall['height']/2
        wall['speedY'] = -wall['speedY']
    elif wall['y']+wall['height']/2 > border:
        wall['y'] = border - wall['height']/2
        wall['speedY'] = -wall['speedY']


def wall_draw(wall):
    # Отрисовка стены
    # wall - словарь со свойствами стены

    x, y, height, width = wall['x'], wall['y'], wall['height'], wall['width']
    rect = pg.Rect((x-width/2, y-height/2), (width, height)) 
    pg.draw.rect(screen, wall['color'], rect)

pg.init()
pg.display.set_caption('Animation by Ryazanov Maxim')
screen = pg.display.set_mode(SIZE)

ball = {'x': 500, # Координаты шара
        'y': 500,
        'rad': 50, # Радиус шара
        'color': (200, 150, 100), # Цвет шара
        'angleSpeed': 2*math.pi/3, # Угловая скорость шара
        'speedX': 300, # Cкорость в направлении координат
        'speedY': 300,
        'angle': 0, # Текущий угол поворота
        }

wall = {'x': SIZE[0]/2, # Координаты стены
        'y': 200,
        'height': 200, # Высота стены
        'width': SIZE[0], # Ширина стены
        'color': (100, 0, 0), # Цвет стены
        'speedY': 150, # Скорость стены
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
