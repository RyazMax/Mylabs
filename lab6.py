# Определение суммы ряда и построение таблицы значений
# Автор: Рязанов Максим

# x - значение x
# eps - точность
# nmax - максимальное количество итераций
# step - шаг
# s - сумма элементов
# t - текущий член ряда
# n - номер текущей итерации
# hor, ver, crosa - коды символов Unicode

x = float(input('Введите x:'))
eps = float(input('Введите точность:'))
nmax = int(input('Введите максимальное количество итераций:'))
step = int(input('Введите шаг:'))

hor = '\u2500'
ver = '\u2502'
crosa = '\u253c'

s = 1
t = 1
n = 1

# Построение таблицы
print('\u250c'+6*hor+'\u252c'+10*hor+'\u252c'+17*hor+'\u252c'+15*hor+'\u2510')
print(ver+'{:^6s}'.format('N')+ver+'{:^10s}'.format('X')+ver, end = '')
print('{:^17s}'.format('Текущий член ряда')+ver, end = '')
print('{:^15s}'.format('Cумма ряда')+ver)
print('\u251c'+6*hor+crosa+10*hor+crosa+17*hor+crosa+15*hor+'\u2524')
print(ver+'{:^6d}'.format(n)+ver+'{:^10.4f}'.format(x)+ver, end = '')
print('{:>17.7f}'.format(t)+ver+'{:>15.7f}'.format(s)+ver)


while abs(t)>eps and n<nmax:
    t = -t*x*x/(2*n*(2*n-1))
    s += t

    if n%step == 0:
        print(ver+'{:^6d}'.format(n+1)+ver+'{:^10.4f}'.format(x)+ver, end = '')
        if abs(t)>1e+8 or abs(t)<1e-7:
            print('{:>17.7e}'.format(t)+ver, end = '')
        else:
            print('{:>17.7f}'.format(t)+ver, end = '')
        if abs(s)>1e+8 or abs(t)<1e-7:
            print('{:>15.7e}'.format(s)+ver)
        else:
            print('{:>15.7f}'.format(s)+ver)


    n += 1 
print('\u2514'+hor*6+'\u2534'+hor*10+'\u2534'+hor*17+'\u2534'+15*hor+'\u2518')

if abs(t)>eps:
    print('Ряд не сошелся за',nmax,end = ' ')
    if 5<=nmax%10<=9 or nmax%10 == 0 or 10<=nmax%100<20:
        print('итераций ', end ='')
    elif nmax%10 == 1:
        print('итерацию ', end ='')
    else:
        print('итерации ', end ='')
else:
    print('Ряд сошелся за',n,end = ' ')
    if 5<=n%10<=9 or n%10 == 0 or 10<=n%100<20:
        print('итераций ', end = '')
    elif n%10 == 1:
        print('итерацию ', end = '')
    else:
        print('итерации ',end = '')
print('с заданной точностью.')
if s>1e+8:
    print('Cумма ряда равна {:13.7e}'.format(s))
else:    
    print('Сумма ряда равна {:13.7f}'.format(s))
