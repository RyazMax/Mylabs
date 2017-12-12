# Интегрирование функции

# Автор: Рязанов Максим

# dig - проверка на корректность числа
# mfunc - функция для интегрирования
# a - начало диапозона интегрирования
# b - конец дипозона интегрирования
# n1, n2 - количество разбиений
# step - длина 1 диапозона
# s1, s3 - значения интеграла по методу срединных прямоугольников
# s2, s4 - значения интеграла по методу "3/8"
# x - текущее значение аргумента
# t, t1, t2, t3, t4, f1, f2, f3, f4 - рабочие переменные


from math import sin, cos

def dig(x):
    if x[0] == '-': x = x[1:]
    t2 = '1'
    if '.' in x:
        t1 = x[:x.index('.')]
        t2 += x[x.index('.')+1:]
    else:
        t1 = x
    if t1.isdigit() and t2.isdigit():
        return True
    else:
        return False
    
def mfunc (x):
    return (sin(x)*sin(x)+cos(x)*cos(x))

a = input('Введите начало диапозона интегрирования: ')
if dig(a):
    a = float(a)
else:
    print('Введено неверное значение')
    exit()
    
b = input('Введите конец диапозона интегрирования : ')
if dig(b):
    b = float(b)
else:
    print('Введено неверное значение')
    exit()

if not b>=a:
    print('Введен неверный диапозон')
    exit()
    
n1 = input('Введите 1-е количество разбиений(натуральное число): ')
if n1.isdigit() and n1!='0':
    n1 = int(n1)
else:
    print('Введено не натуральное число')
    exit()

n2 = input('Введите 2-е количество разбиений(натуральное число): ')
if n2.isdigit() and n2!='0':
    n2 = int(n2)
else:
    print('Введено не натуральное число')
    exit()
    


# Интегрирование
s1 = s3 = 0
s2 = s4 = mfunc(a)+mfunc(b)

step = (b-a)/n1
for i in range (n1):
    x = a+step*i
    s1 += (mfunc((x+x+step)/2))
    if i:
        if i%3:
            s2 += 3*mfunc(x)
        else:
            s2 += 2*mfunc(x)

s1 *= step
s2 *= step*(3/8)

step = (b-a)/n2
for i in range (n2):
    x = a+step*i
    s3 += (mfunc((x+x+step)/2))
    if i:
        if i%3:
            s4 += 3*mfunc(x)
        else:
            s4 += 2*mfunc(x)
s3 *= step
s4 *= step*3/8

# Вывод
f1 = f2 = f3 = f4 = 'f'
if abs(s1)>1e+7 or(abs(s1)<1e-7): f1 = 'e'
if abs(s2)>1e+7 or(abs(s2)<1e-7): f2 = 'e'
if abs(s3)>1e+7 or(abs(s3)<1e-7): f3 = 'e'
if abs(s4)>1e+7 or(abs(s4)<1e-7): f4 = 'e'

print()
if n1%3 or n2%3:
    print('Для метода "3/8" необходимо число разбиенией кратное 3')
    if n1%3: s2 = '-'
    if n2%3: s4 = '-'
   
t = "ср. прямоугольников"
t1 = "Метод"
t2 = "N\u2081"
t3 = "N\u2082"
t4 = '"3/8"'

print('\u250c'+'\u2500'*20+'\u252c'+'\u2500'*16+'\u252c'+'\u2500'*16+'\u2510')
print('\u2502{:^20s}\u2502{:^16s}\u2502{:^16s}\u2502'.format(t1,t2,t3))
print('\u251c'+'\u2500'*20+'\u253c'+'\u2500'*16+'\u253c'+'\u2500'*16+'\u2524')
print('\u2502{0:^20s}\u2502{1:>16.6{3}}\u2502{2:>16.6{4}}'
                                               '\u2502'.format(t,s1,s3,f1,f3))
print('\u251c'+'\u2500'*20+'\u253c'+'\u2500'*16+'\u253c'+'\u2500'*16+'\u2524')
print('\u2502{:^20s}\u2502'.format(t4), end ='')
if s2 != '-': print('{0:>16.6{1}}\u2502'.format(s2,f2),end = '')
else: print('{:^16s}\u2502'.format(s2), end = '')
if s4 != '-': print('{0:>16.6{1}}\u2502'.format(s4,f4))
else : print('{:^16s}\u2502'.format(s4))
print('\u2514'+'\u2500'*20+'\u2534'+'\u2500'*16+'\u2534'+'\u2500'*16+'\u2518')
                            

    
