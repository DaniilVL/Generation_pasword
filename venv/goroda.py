print('vvedite nazvanie goroda dlya dobavleniya v spisok, dlya zaversheniya vvedite:$')
a = [(i) for i in input().split()]
goroda=[]
i=str
while i!='$':
    for i in a:
        if i=='$':
            break
        elif i=='\n':
            goroda.append(', ')
            print(goroda)
        elif i!='\n':
            goroda.append(i)
    if i=='$':
        break
    a=[(i) for i in input().split()]
print(goroda)
Zapis=open('SpisokGorodov.txt','w')
for eliment in goroda:
    Zapis.write(eliment)
    Zapis.write('\n')
Zapis.close()
