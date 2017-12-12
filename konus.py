fin = open('data.txt','r')
fout = open('output.txt','w')

#n = int(input())
s_list = []
key_list = []
d = {}
i = 0

#for i in range (n):
for line in fin:

    if line[len(line)-1] == '\n':
        s_list.append(line[:-1])
    else:
        s_list.append(line)
    #s_list[i] = input()

    ln = len(s_list[i])
    key = ''
    for j in  range (26):
       key += str(s_list[i].count(chr(ord('a')+j)))
       key +=' '
    if not key in d.keys():
        d[key] = []
        key_list.append(key)
        d[key].append(i)
    else:
        d[key].append(i)

    i+=1
    
ln = len(key_list)
for i in range(ln):
    fout.write('THE '+str(i+1)+' GROUP\n')
    for j in range(len(d[key_list[i]])):
        fout.write(s_list[d[key_list[i]][j]]+' ')
    fout.write('\n')
    

fin.close()
fout.close()
       


