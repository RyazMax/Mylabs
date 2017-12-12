# Построение массива чисел, определение совпадающих чисел
# Автор: Рязанов Максим

# n - количество элементов в массиве
# a - начало диапозона
# b - конец диапозона
# maxs - максимальное количество совпадающих чисел
# snum - значение самого частого элемента
# temp, nd, ad, bd,g - рабочие переменные

from random import randint

g = False
n = input('Введите количество элементов массива: ')
a = input('Введите начало диапозона: ')
b = input('Введите конец диапозона: ')

nd = n.isdigit()
ad = a.isdigit() or (a[0] == '-' and a[1:].isdigit())
bd = b.isdigit() or (b[0] == '-' and b[1:].isdigit())

if nd and bd and ad:
    n = int(n)
    a = int(a)
    b = int(b)
    g = True
    
else:
    print('Введены некорректные значения!')
    
if g:
    arr = [randint(a,b) for i in range(n)]
    print('Cформированный массив:')
    print(arr)

    maxs = 0
    for i in range (n):
        temp = arr.count(arr[i])
        if temp>maxs:
            maxs = temp
            snum = arr[i]
    if n>0:
        print('Максимальное количество совпадающих чисел: ',maxs)
        print('Максимально совпадающее число:',snum)
    else:
        print('Был сформирован нулевой массив')
    
