# Определение прямой пересекающией наибольшее число треугольников
# Автор: Рязанов Максим

# points - список точек
# idpoints - id точек в Canvas
# tring - список треугольников
# idtring - id треугольников в Canvas
# Com_text - стандартный текст
# set_text(text,col) - установить текст в цвет сol
# warn(text) - выдать предупреждение text
# dig(number) - проверка на число
# draw_iline(points,lwd) - построение бесконечной линии шириной lwd
# clean() - очистка канваса и всех фигур
# istring(tmp) - проверка точек tmp на треугольник
# add() - добавление фигуры
# ret() - скрытие построений
# calculate() - вычисление максимального количества пересечений
# delete(ls) - удаление выделеной фигуры из списка ls
# root - основное окно
# can - Холст
# entry - поле ввода координат
# label - сообщение
# ls - список точек
# lstitle - заголовок ls
# ls2 - список треугольников
# ls2title - заголовок ls2
# new_but - кнопка очистить
# do_but - кнопка выполнения
# ret_but - кнопка скрытия построений
# but - кнопка добавления фигуры

from tkinter import*
import math as m

points = []
idpoints = []
tring = []
idtring = []
Com_text = 'Введите координаты точки или 3-х точек треугольника'


def set_text(text,col):
    label['text'] = text
    label['foreground'] = col

def warn(text):
    set_text(text,'red')
    label.after(2000,lambda: set_text(Com_text,'black'))

def dig(number):
    if type(number) == int: return True
    if number[0] == '-': number = number[1:]

    ind = number.index('.') if '.' in number else len(number)
    tmp1 = number[:ind]
    tmp2 = '2'+number[ind+1:]

    return tmp1.isdigit() and tmp2.isdigit()

def draw_iline(points,lwd):
    p1 = [points[0],points[1]]
    p2 = [points[2],points[3]]

    deltax = p2[0]-p1[0] 
    deltay = p2[1]-p1[1]

    if deltax == 0 and deltay == 0:
        k = 0
    elif deltax == 0:
        k = 500/deltay
    elif deltay == 0:
        k = 500/deltax
    else:
        k = min(500/deltay,500,deltax)

    can.create_line(p1[0]-k*deltax,p1[1]-k*deltay,
                    p2[0]+k*deltax,p2[1]+k*deltay,width = lwd, fill = 'red',tags = 'line')

def clean():
    can.delete(*(can.find_all()))
    ls.delete(0,ls.size())
    ls2.delete(0,ls2.size())
    points.clear()
    tring.clear()
    idpoints.clear()
    tring.clear()

def istring(tmp):
    
    a = m.sqrt((tmp[0]-tmp[2])**2+(tmp[1]-tmp[3])**2)
    b = m.sqrt((tmp[2]-tmp[4])**2+(tmp[3]-tmp[5])**2)
    c = m.sqrt((tmp[0]-tmp[4])**2+(tmp[1]-tmp[5])**2)

    if abs(a+b-c<1e-6): return False
    if abs(a+c-b<1e-6): return False
    if abs(b+c-a<1e-6): return False
    return True
    
    
def add(event = None):
    set_text(Com_text,'black')
    tmp = entry.get().split()
    
    if event:
        tmp = [event.x,event.y]
        
    if not len(tmp) in [2,6]:
        warn('Введены неверные значения')
        return
    else:
        cor = list(map(dig,tmp))
        g = True
        for i in cor:
            g &= i
        if  not g:
            warn('Введены неверные значения')
            return
        tmp = list(map(float,tmp))
        lwd = 2
        if len(tmp) == 2:
            idpoints.append(can.create_oval(tmp[0]-1,
                    tmp[1]-1,tmp[0]+1,tmp[1]+1,width = 3,outline = 'green'))
            points.append(tmp)
            ls.insert(0,tmp)
        if len(tmp) == 4:
            draw_iline(tmp,lwd)
        if len(tmp) == 6:
            if istring(tmp):
                tring.append(tmp)
                idtring.append([
                can.create_line(tmp[0],tmp[1],tmp[2],
                                tmp[3],width = lwd,fill = 'blue'),
                can.create_line(tmp[0],tmp[1],tmp[4],
                                tmp[5],width = lwd,fill = 'blue'),
                can.create_line(tmp[2],tmp[3],tmp[4],
                                tmp[5],width = lwd,fill = 'blue')])
                ls2.insert(0,tmp)
            else:
                warn('Вырожденный треугольник')
                return
        entry.delete(0,len(entry.get()))

def ret():
    can.delete('line')
    can.itemconfigure('h', width = 3,outline = 'green',tags = '')
    can.itemconfigure('h', width = 3,outline = 'green',tags = '')
    
def calculate():
    ret()
    if len(points)<2: return warn('Недостаточно точек')
    mx = 0
    id1 = -1
    id2 = -1
    for i in range(len(points)-1):
        for j in range(i+1,len(points)):
            x0 = points[i][0]
            y0 = points[i][1]
            dx = x0-points[j][0]
            dy = y0-points[j][1]
            cur = 0
            for k in range(len(tring)):
                tmp = []
                for q in range(3):
                    dxt = x0-tring[k][q*2]
                    dyt = y0-tring[k][q*2+1]
                    vec = (dx*dyt-dy*dxt)
                    tmp.append(vec)
                g = True
                if tmp[0]<0 and tmp[1]<0 and tmp[2]<0: g = False
                if tmp[0]>0 and tmp[1]>0 and tmp[2]>0: g = False
                if g: cur+=1
            if cur>mx:
                id1 = i
                id2 = j
                mx = cur
    if mx:
        draw_iline(points[id1]+points[id2],3)
        can.create_text(305,270,text = str(mx)+' пересечений',tags = 'line')
        can.itemconfigure(idpoints[id1], width = 5,outline = 'black',tags='h')
        can.itemconfigure(idpoints[id2], width = 5,outline = 'black',tags='h')
    else:
        can.create_text(305,270,text = 'Нет пересечений',fill = 'red',
                        tags = 'line')
                
    
def delete(ls):
    if not ls.curselection():
        return 1
    sel = ls.size()-1-list(ls.curselection())[0]
    if len(ls.selection_get().split()) == 2:
        can.delete(idpoints[sel])
        idpoints.pop(sel)
        points.pop(sel)
    else:
        for i in range(3):
            can.delete(idtring[sel][i])
        idtring.pop(sel)
        tring.pop(sel)
            
    ls.delete(ls.size()-1-sel)
    
    

root  = Tk()
root.title('Точки и треугольники')
root.geometry('800x350')
root.bind(sequence = '<Control-r>', func = lambda x: calculate())
root.bind(sequence = '<Control-z>', func = lambda x: ret())
root.bind(sequence = '<Control-n>', func = lambda x: clean())

can = Canvas(root,bg = 'white',height = 280, width = 350)
can.grid(row = 1,rowspan = 4, column = 0, columnspan = 3, padx = 10)
can.bind(sequence = '<Button-1>',func = add)
can.bind(sequence = '<Button-3>',
         func = lambda x: entry.insert(0,str(x.x)+' '+str(x.y)+' '))

entry = Entry(root,width = 25)
entry.bind(sequence = '<Return>', func = lambda x: add())
entry.grid(row = 2, column = 3, columnspan = 2)
entry.focus_set()

label = Label(root,text = 'Введите координаты точки или 3-х точек треугольника')
label.grid(row = 1, column = 3, columnspan = 2)

new_but = Button(root,text = 'Очистить',command = clean)
new_but.grid(row = 0, column = 0,sticky = 'w',padx = 10)

but = Button(root, text = 'Добавить', command = add)
but.grid(row = 2, column = 4,sticky = 'e')

lstitle = Label(root,text = 'Точки')
lstitle.grid (row = 3,column = 3)

ls2title = Label(root,text = 'Треугольники')
ls2title.grid (row = 3,column = 4)

ls = Listbox(root, width = 25)
ls.grid(row = 4, column = 3,rowspan = 2,padx = 10)
ls.bind(sequence = '<Delete>',func = lambda x: delete(ls))

ls2 = Listbox(root, width = 25)
ls2.grid(row = 4, column = 4, rowspan = 2)
ls2.bind(sequence = '<Delete>',func = lambda x: delete(ls2))

do_but = Button(root, text = 'Выполнить!',command = calculate,width = 10)
do_but.grid(row = 6, column = 3,sticky = 'e')

ret_but = Button(root, text = 'Продолжить', command = ret, width = 10)
ret_but.grid(row = 6,column = 4,sticky = 'w')

root.mainloop()
