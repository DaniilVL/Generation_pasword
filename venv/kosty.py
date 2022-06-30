import random
import re
print('Для получения результата бросания костей напишите:Y, для выхода напишите:N')
igra=str()
one=int()
two=int()
result=str()
igra = str(input().strip())
while result != True:
    result=re.match(r'[y n]', igra) and len(igra)==1
    print(result)
    if result==None or False:
        igra = str(input().strip())
while igra!='n':
    if igra=='y':
        one=random.randint(1,6)
        two=random.randint(1,6)
        print("Результат броска первый кубик",one, "второй кубик",two)
        print('Хотите еще сыграть Y-да, N - нет')
        igra = str(input().strip())
        while result != True:
            result = re.match(r'[y n]', igra) and len(igra) == 1
            print(result)
            if result == None or False:
                igra = str(input().strip())


