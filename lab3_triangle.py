# Определение свойств треугольника
# Автор: Рязанов Максим

# x1 - координата x 1-й вершины треугольника
# y1 - координата y 1-й вершины треугольника
# x2 - координата x 2-й вершины треугольника
# y2 - координата у 2-й вершины треугольника
# x3 - координата х 3-й вершины треугольника
# y3 - координата y 3-й вершины треугольника
# a - длина 1-й стороны треугольника
# b - длина 2-й стороны треугольника
# c - длина 3-й стороный треугольника
# x0 - координата x произвольной точки
# y0 - координата y произвольной точки
# med - длина медианы проведенной из наименьшего угла треугольника
# mdist - расстояние от точки до близжайщей стороны или её продолжения
# adist - расстояние от точки до 1-й стороны
# bdist - расстояние от точки до 2-й стороны
# cdist - расстояние от точки до 3-й стороны
# exist, point, t_a, t_b, t_c, s_a, s_b, s_c - рабочие переменные
# rs_a, rs_b, rs_c, part_a, part_b, part_c - рабочие переменные 

from math import sqrt

exist = True
point = False

# Ввод координат
x1 = float(input('Введите координату x 1-й вершины треугольника'))
y1 = float(input('Введите координату y 1-й вершины треугольника'))
x2 = float(input('Введите координату x 2-й вершины треугольника'))
y2 = float(input('Введите координату y 2-й вершины треугольника'))
x3 = float(input('Введите координату x 3-й вершины треугольника'))
y3 = float(input('Введите координату y 3-й вершины треугольника'))
    
# Определение длин сторон
a = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
b = sqrt((x3-x2)*(x3-x2) + (y3-y2)*(y3-y2))
c = sqrt((x3-x1)*(x3-x1) + (y3-y1)*(y3-y1))

if a==0 and b==0:
    exist = False
    point = True
    print('Все точки совпадают. Треугольник не существует.')
elif a == 0:
    exist = False
    print('Точки 1 и 2 совпадают. Точки образуют отрезок.')
elif b == 0:
    exist = False
    print('Точки 2 и 3 совпадают. Точки образуют отрезок.')
elif c == 0:
    exist = False
    print('Точки 1 и 3 совпадают. Точки образуют отрезок.')
    
if exist:
    if a+b == c or a+c == b or b+c == a:
        exist = False
        print ('3 точки лежат на одной прямой. Треугольник вырожденный')

if exist:
    print ('1-я сторона треугольника = {:4.3f}'.format(a))
    print ('2-я сторона треугольника = {:4.3f}'.format(b))
    print ('3-я сторона треугольника = {:4.3f}'.format(c))
    if a == b == c:
        print('Треугольник равносторонний')
    else:
        print('Треугольник не равносторонний')
        
# Определение медианы
if exist:
    if a<=b and a<=c:
        xm = (x2+x1)/2
        ym = (y2+y1)/2
        med = sqrt((xm-x3)*(xm-x3) + (ym-y3)*(ym-y3))
    elif b<=a and b<=c:
        xm = (x3+x2)/2
        ym = (y3+y2)/2
        med = sqrt((xm-x1)*(xm-x1) + (ym-y1)*(ym-y1))
    else:
        xm = (x3+x1)/2
        ym = (y3+y1)/2
        med = sqrt((xm-x2)*(xm-x2) + (ym-y2)*(ym-y2))
    print('Длина медианы опущенной из меньшего угла: {:4.3f}'.format(med))

# Определение принадлежности точки треугольнику
x0 = float(input('Введите координату x произвольной точки'))
y0 = float(input('Введите координату y произвольной точки'))

if point:
    if x1 == x0 and y1 == y0:
        print('Точка (',x0,',',y0,') совпадает с всеми 3 точками')
else:
    t_a = (x2-x1)*(y0-y1) - (y2-y1)*(x0-x1)
    t_b = (x3-x2)*(y0-y2) - (y3-y2)*(x0-x2)
    t_c = (x1-x3)*(y0-y3) - (y1-y3)*(x0-x3)

    s_a = (x2-x1)*(x0-x1) + (y2-y1)*(y0-y1)
    s_b = (x3-x2)*(x0-x2) + (y3-y2)*(y0-y2)
    s_c = (x1-x3)*(x0-x3) + (y1-y3)*(y0-y3)

    rs_a = (x1-x2)*(x0-x2) + (y1-y2)*(y0-y2)
    rs_b = (x2-x3)*(x0-x3) + (y2-y3)*(y0-y3)
    rs_c = (x3-x1)*(x0-x1) + (y3-y1)*(y0-y1)

    part_a = t_a == 0 and s_a>=0 and rs_a>=0 and a
    part_b = t_b == 0 and s_b>=0 and rs_b>=0 and b
    part_c = t_c == 0 and s_c>=0 and rs_c>=0 and c
    
    if exist:
        if part_a or part_b or part_c:
            print('Точка лежит на стороне треугольника')
        elif (t_a>0 and t_b>0 and t_c>0)or(t_a<0 and t_b<0 and t_c<0):
            print('Точка лежит внутри треугольника')
        else:
            print('Точка лежит вне треугольника')
    elif (part_a or part_b or part_c):
        print('Точка лежит на отрезке c точками',x1,y1,'|',x2,y2,'|',x3,y3)
    else:
        print('Точка не лежит на отрезке с точками',x1,y1,'|',x2,y2,'|',x3,y3)
            
# Нахождение расстояния от точки до близжайшей прямой
if point:
    mdist = sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0))
    print('Расстояние от точки до 3 совпадающих точек {:4.3f}'.format(mdist))
else:
    if a == 0:
        bdist = abs(t_b/b)
        cdist = abs(t_c/c)
        mdist = min(bdist,cdist)
    elif b == 0:
        cdist = abs(t_c/c)
        adist = abs(t_a/a)
        mdist = min(adist,cdist)
    elif c == 0:
        adist = abs(t_a/a)
        bdist = abs(t_b/b)
        mdist = min(bdist,adist)
    else:
        adist = abs(t_a/a)
        bdist = abs(t_b/b)
        cdist = abs(t_c/c)
        mdist = min(min(adist,bdist),cdist)
    print('Растояние до прямой содержащей близжайшую сторону {:4.3f}'.format(mdist))
        
