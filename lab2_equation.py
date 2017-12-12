# Решение квадратных уравнений 
# Автор: Рязанов Максим	

#       a - старший коэффициент
#       b - средний коэффициент
#       c - свободный член уравнения
#       D - дискриминант 
#       x1, x2 - корни уравнения
#       sqD, a2 - рабочие переменные

from math import sqrt

a = int(input('Введите старший коэффициент уравнения '))
b = int(input('Введите средний коэффициент уравнения '))
c = int(input('Введите свободный член уравнения '))

if a == 0:
    if b == 0:
        if c == 0:
            print ('Корень уравнения - любое число')
        else:
            print ('Решений нет')
    else:
        x1=-c/b
        print ('Корень линейного уравнения: {:4.3f}'.format(x1))
else:
    D = b*b - 4*a*c
    a2 = a*2
    if D>0:
        sqD = sqrt(D)
        x1 = (-b + sqD)/a2
        x2 = (-b - sqD)/a2
        print ('Первый корень уравнения: {:4.3f}'.format(x1))
        print ('Второй корень уравнения: {:4.3f}'.format(x2))
    elif D == 0:
        x1 = -b/a2
        print('Корень кратности 2: {:4.3f}'.format(x1))
    else:
        print ('Действительных решений нет')