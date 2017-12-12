# Работа с текстом

# Автор: Рязанов Максим

# endsymb - список символов, обозначающих конец предложения
# nlines - количество строк
# lines - cписок изходных строк текста
# text - список из слово изходного текста
# lilen - список длин строк
# mlen - длина максимальной строки
# nspace - список количества пробелов в строках
# cmd - номер команды
# flag - режим выравнивания
# start [i,j] - индекс первого элемента текущего предложения
# last [i,j] - индекс первого элемента, следующего за текущим предложением
# mstart [i,j] - индекс первого элемента искомого предложения
# mlast [i,j] - индекс первого элемента, следующего за искомым
# mv - максимальное вхождение искомого слова в предложение
# temp, temp, g, line, sp, nsp, res, word - рабочие переменные

from copy import deepcopy

# Удаление слова
def rmword(wd):
    g = False
    for j in range(len(text)):
        for i in range(len(text[j])):
            if text[j][i] == wd:
                text[j][i] = ''
                g = True
                if text[j][i-1]==' ':
                    text[j][i-1]=''
                    nspace[j] -=1
    if g:
        print('_'*7+'Измененный ТЕКСТ'+'_'*7)
        return text
    else:
        print('Данного слова нет в тексте')
        return []

# Замена слова
def chword(wd,wd1):
    g = False
    for line in text:
        for i in range(len(line)):
            if line[i] == wd:
                line[i] = wd1
                g = True
        
    if g:
        print('_'*7+'Измененный ТЕКСТ'+'_'*7)
        return text
    else:
        print('Данного cлова нет в тексте')
        return []

# Печать текста
def prtext(atext, flag):
    for j in range(len(atext)):
        lilen = sum(list(len(atext[j][i]) for i in range (len(atext[j]))))
        nsp = mlen-lilen
        if nspace[j] != 0:
            sp = nsp//nspace[j]
            nsp = nsp%nspace[j]
        else:
            sp = 0
            nsp = 0
            
        if flag == 'l':
            g = False
        else:
            g = True
            
        if flag == 'r':
            print(' '*(mlen-lilen),end = '')
        for i in range(len(atext[j])):
            if atext[j][i] and (g or atext[j][i]!= ' '):
                print(atext[j][i], end = '')
                g = True
            if (flag == 'c'or flag == 'с') and atext[j][i] == ' ':
                print(' '*sp,end = '')
                if nsp:
                    print(' ',end = '')
                    nsp -= 1
        print()
        
# Cимволы конца предложения            
endsymb = ".?!"

# Ввод
lines = []
print('TЕКСТ')
nlines = 0
while True:
    lines.append(input())
    nlines += 1
    if lines[nlines-1][-1] == '.':
        break
    
    

text = []
nspace = [0]*nlines
mlen = 0

for i in range(nlines):
    lilen = len(lines[i])
    mlen = max(mlen,lilen)
    temp = ""
    temp2 = []
    for j in lines[i]:
        if j.isalpha():
            temp += j
        else:
            if j == ' ':
                nspace[i] += 1
            if temp: temp2.append(temp)
            temp = ""
            temp2.append(j)
    if temp: temp2.append(temp)
    text.append(temp2)
    
    

# Основная часть программы
while True:
    
    print('МЕНЮ\n1. Удалить слово\n2. Заменить слово')
    print('3. Выравнить')
    print('4. Предложение с максимальным количеством вхождений слова')
    print('0. Выйти из программы\n\n')
    print('ТЕКСТ:\n')
    

    prtext(text,'s')
    print()
    cmd = (input('Введите номер команды: '))
    if cmd.isdigit():
        cmd = int(cmd)
        if cmd > 4 :
            print('Введена неверная команда')
    else:
        print('Введена неверная команда')
        cmd = -1
    
    if cmd == 0:
        print('Завершение программы.')
        break
    if cmd == 1:
        word = input('Введите слово которое нужно удалить: ')
        print('\n')
        prtext(rmword(word),'s')
        print('\n')
    if cmd == 2:
        word = input('Введите слово которое нужно заменить: ')
        word1 = input('Введите слово на которое нужно заменить: ')
        print('\n')
        
        prtext(chword(word,word1),'s')
        print('\n')
    if cmd == 3:
        print('Выравнивание по левому краю - l')
        print('Выравнивание по ширине - с')
        print('Выравнивание по правому краю - r')
        flag = input('Введите режим выравнивания: ').lower()
        if flag == 'l' or flag == 'c' or flag == 'с' or flag == 'r':
            print('ТЕКСТ')
            prtext(text,flag)
        else:
            print('Неверный режим выравнивания')
    if cmd == 4:
        word = input('Введите искомое слово: ')
        print()
        start = [0,0]
        last = [0,0]
        mstart = [0,0]
        mlast = [nlines-1,len(text[nlines-1])]
        mv = 0
        temp = 0
        for i in range(nlines):
            for j in range(len(text[i])):
                if text[i][j] == word:
                    temp += 1
                if text[i][j] in endsymb and text[i][j]!='':
                    start = last[:]
                    last = [i,j+1]
                    if temp>mv:
                        mv = temp
                        mstart = start[:]
                        mlast = last[:]
                    temp = 0
                    
        if  mv+temp == 0:
            print('Данное слово не встречается в тексте')
        else:
            if mstart[1]>=len(text[mstart[0]]):
                mstart[0] += 1
                mstart[1] = 0
            print('Максимальное количество вхождений - ',mv)
            print('Предложение с максимальный количеством вхождений слова:')
            g = True
            if mstart[0] == mlast[0]:
                for i in range(mstart[1],mlast[1]):
                    if not(g and text[mstart[0]][i]== ' '):
                        print(text[mstart[0]][i],end = '')
                        g = False
            else:
                for i in range(mstart[1],len(text[mstart[0]])):
                    if not(g and text[mstart[0]][i]== ' '):
                        print(text[mstart[0]][i],end = '')
                        g = False
                print(' ',end = '')
                for i in range(mstart[0]+1,mlast[0]):
                    for j in range(len(text[i])):
                        print(text[i][j],end = '')
                    print(' ',end = '')
                for i in range(mlast[1]):
                    print(text[mlast[0]][i],end = '')
        print('\n')
                          
                
    input('Нажмите ENTER, чтобы продолжить...\n')    
