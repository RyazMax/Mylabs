def change(s):
    s = s.upper()
    s = s.replace('I','1')
    s = s.replace('L','1')
    s = s.replace('O','0')
    return s

login = change(input())

g = True
n = int(input())
for i in range(n):
    x = change(input())
    if x == login: g = False

if g:
    print('Yes')
else:
    print('No')
    
