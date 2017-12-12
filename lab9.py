# Сортировка массива

# Автор: Рязанов Максим

# qsort - функция быстрой сортировки
#   mas - массив подающийся в функцию
#   lenmas - длина массива
#   med - опорный элемент
#   t1, t2, t3 - служебные переменные
#   res - результирующий массив
# arr - исходный массив

from random import randint

def qsort (mas):
    lenmas = len(mas)
    if lenmas<=1:
        return mas
    if lenmas>1:
        med = randint(0,lenmas-1)
        t1 = list(filter((lambda x: x<mas[med]),mas))
        t3 = list(filter((lambda x: x == mas[med]),mas))
        t2 = list(filter((lambda x: x>mas[med]),mas))
        res = qsort(t1)+t3+qsort(t2)
    return res
 
arr = list(map(int,input().split()))
arr = qsort(arr)
print (arr)
