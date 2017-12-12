# Подсчет среднего арифметического модулей отрицательных чисел
# Автор: Рязанов Максим

# arr - массив чисел
# lenarr - длина массива
# cnt - количество отрицательных на четных позициях
# s - сумма модулей отрицательных на четных позициях
# sr - среднее арифметическое отрицательных элементов на четных позициях
# g, num, temp1,temp2,pos - рабочие переменные

g = True

print('Введите элементы массива через пробел:')
arr = list(map(str,input().split()))
lenarr = len(arr)

for num in range(lenarr):
    temp1 = arr[num][1:] if arr[num][0] == '-' else arr[num]
    temp2 = '2'
    if '.' in temp1:
        pos = temp1.index('.')
        temp2 = temp1[pos+1:]
        temp1 = temp1[:pos]
    if temp1.isdigit() and temp2.isdigit():
        arr[num] = float(arr[num])
    else:
        print('Введены некорректные значения')
        g = False
        break
if g:
    s = 0
    cnt = 0
    for i in range (lenarr):
        if i%2 == 0 and arr[i]<0:
            cnt +=1
            s += abs(arr[i])
    if cnt>0:
        sr = s/cnt
        print('Среднее арифмитическое модулей отрицательных элементов ',end = '')
        print('{:.4f}'.format(sr))
    else:
        if lenarr == 0:
            print('Введен нулевой массив')
        print('В массиве нет отрицательных элементов на четных позициях')
    
