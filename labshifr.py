# Шифрование
# Автор: Рязанов Максим

# word - исходное сообщение
# key - ключ
# alph - алфавит
# lenw - длина сообщения
# lenk - длина ключа
# lenal - длина алфавита
# shf - массив сдвигов
# g - регистр исходного сообщения
# resword - промежуточный результат
# ans - зашифрованное сообщение
# cor, t1, t2 - рабочие переменные

# Ввод
word = input('Введите сообщение: ')
key = input('Введите ключ: ')
key = key.upper()

# Cоставление алфавита
alph = [chr(i) for i in range(ord('А'),ord('Е')+1)]
alph.append('Ё')
alph += [chr(i) for i in range(ord('Ж'),ord('Я')+1)]
lenal = len(alph)

# Проверка данных
cor = True
for i in key:
    if not i in alph:
        cor = False
        
if not cor:
    print('Введен некорректный ключ')
    exit()
    

lenw = len(word)
lenk = len(key)
g = [word[i].islower() for i in range (lenw)]
word = word.upper()
resword = []


# Массив сдвигов
shf = [alph.index(key[i]) for i in range (lenk)]

# Шифровка
for i in range(lenw):
    if word[i] in alph:
        t1 = alph.index(word[i])
        t2 = (t1+shf[i%lenk])%lenal
        resword.append(alph[t2])
    else:
        resword.append(word[i])
    if g[i]:
        resword[i] = resword[i].lower()

ans = ""
for i in range(lenw):
    ans += resword[i]
    
print(ans)
        
        



