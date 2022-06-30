def provGorodov(vnutrSpisok,VvodGoroda):
    global proverka
    for z in vnutrSpisok:
        if z == VvodGoroda:
            proverka = 1
            ispGoroda.append(z)
            break
        elif VvodGoroda != z:
            proverka = 0
            continue
        else:
            break
    return(ispGoroda,proverka)

def provNaPovtor(ispGoroda,VvodGoroda):
    global Povtor
    for i in ispGoroda:
        if i == VvodGoroda:
            Povtor = 0
            break
        elif i!=VvodGoroda:
            Povtor = 1
            continue
    return(Povtor)

def proverkaNaPravila(VvodGoroda,lastBukva):
    global k
    if VvodGoroda[0]==lastBukva:
        k=1
    elif VvodGoroda[0]!=lastBukva:
        k=0
    return(k)

def proverkaNaEnter():
    global VvodGoroda
    while len(VvodGoroda)==0:
        if len(VvodGoroda)==0:
            print('Введите название города:')
            VvodGoroda = str(input().lower())
        elif len(VvodGoroda)>=1:
            continue
    return(VvodGoroda)

def proverkaNaZnakiIprobel():
    global pervayaBukva
    global c
    global C
    with open('Simbol.txt') as file:
        for i in file:
            c.append(i.strip())
        while C != 1:
            if pervayaBukva in c:
                C += 1
            if pervayaBukva not in c:
                print('Введите одну букву, без:', pervayaBukva)
                pervayaBukva = str(input().lower())
    return(pervayaBukva)




print('Введите букву для первого города:')
pervayaBukva=str(input().lower())
VvodGoroda=str()
proverka=int()
ispGoroda=list()
lastBukva=str()
Povtor=1
K=0
z=0
c=list()
C=0
proverkaNaZnakiIprobel()
while len(pervayaBukva)==1:
    if len(pervayaBukva)==1:
        vnutrSpisok=[pervayaBukva*2]
        lastBukva=pervayaBukva
        ispGoroda=[pervayaBukva]

        break
    else:
        print('введите одну букву')
        pervayaBukva=str(input().lower())
        vnutrSpisok = [pervayaBukva * 2]
with open('SpisokGorodov.txt') as file:
    for i in file:
        vnutrSpisok.append(i.strip().lower())
print('Введите название города на:',pervayaBukva)
while VvodGoroda!='завершить':
    VvodGoroda=str(input().lower())
    proverkaNaEnter()
    provNaPovtor(ispGoroda,VvodGoroda)
    proverkaNaPravila(VvodGoroda,lastBukva)
    if k==1:
        if Povtor==0:
            proverka=2
        elif Povtor == 1:
            provGorodov(vnutrSpisok,VvodGoroda)
    elif k==0:
        proverka=3
    poslBukva=ispGoroda[-1]
    if poslBukva[-1]== 'ь' and 'ъ':
        lastBukva = poslBukva[-2]
    else:
        lastBukva=poslBukva[-1]
    if proverka == 1:
        print('Отлично!, введите город на букву:', lastBukva)
    elif proverka==0:
        print('Такого города нет, введите город на:', lastBukva)
    elif proverka==2:
        print('Данный город уже был, введите город на:', lastBukva)
    elif proverka==3:
        print('Данный город не начинается на:',lastBukva,'Введите город на букву:',lastBukva)
    proverka=1
    Povtor=1






    # global pervayaBukva
    # while True:
    #     with open('список символов.txt') as file:
    #         for i in file:
    #             if pervayaBukva == i.strip():
    #                 break
    #             else:
    #                 print('Введите одну букву, без:', pervayaBukva)
    #                 pervayaBukva = str(input().lower())
    # return(pervayaBukva)





# def proverkaNaZnakiIprobel():
#     global VvodGoroda
#     while True:
#         for i in VvodGoroda:
#             if i!='а' or 'б' or'в'or'г' or'д' or 'е' or'ё'or'ж' or'з' or'и' or 'й' or 'к' or 'л' or'м' or'н'or'о'or'п'or'р'or'с'or'т'or'у'or'ф'or'х'or'ц'or'ч'or'ш'or'щ'or'ъ'or'ы'or'ь'or'э'or'ю'or'я'or'-':
#                 print(i)
#                 print('Введите название города без символа:',i)
#                 VvodGoroda = str(input().lower())
#             else:
#                 continue
#     return(VvodGoroda)







# VvodGoroda=str()
# b=0
# c=list()
# a=[]
# lastBukva=str()
# with open('SpisokGorodov.txt') as file:
#     for i in file:
#         a.append(i.strip().lower())
# while VvodGoroda!='Все':
#     print('Введите название города')
#     VvodGoroda=str(input().lower())
#     for z in a:
#         if z == VvodGoroda:
#             b+=1
#             c.append(z)
#             break
#         elif VvodGoroda!=i:
#             b==0
#             continue
#         else:
#             break
#     #         Добавить проверку на энтер и пробел..
#     lastBukva=VvodGoroda[-1]
#     if b==1:
#         print('Отлично!, введите город на букву:', lastBukva)
#     elif b==0:
#         print('Такого слова нет')
#     b=0
#     print(c)




































# print(c)
# for i in range(len(goroda)):
#     if goroda[i-1]==goroda[i]:
#         c.append(goroda[b])
#         b+=1
#     else:
#         b+=1
#         continue
# print(c)
