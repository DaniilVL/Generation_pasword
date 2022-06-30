import random

import random
def rando(r):
    while r<=200:
        rand=random.randint(1,25)
        r=random.randrange(chisla[-1],chisla[-1]+rand)
        if r in chisla:
            continue
        else:
            chisla.append(r)
    return chisla

chisla=[1]
r=1
rando(r)
print(len(chisla))
print(chisla)
print('Введите число, номер которого вы хотите узнать:')
Nuj_Chislo = int(input())

mid = len(chisla)//2
low = 0
high = len(chisla) - 1

while chisla[mid] != Nuj_Chislo and low <= high:
    if Nuj_Chislo > chisla[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Нет числа")
else:
    print("номер:", mid+1)




































#
# import random
# def rando(r):
#     while r<=200:
#         rand=random.randint(1,25)
#         r=random.randrange(chisla[-1],chisla[-1]+rand)
#         if r in chisla:
#             continue
#         else:
#             chisla.append(r)
#     return chisla
#
# chisla=[0,1]
# r=1
# rando(r)
# print(len(chisla))
# print(chisla)
# print('Введите число, номер которого вы хотите узнать:')
# Nuj_Chislo=int(input())
# i=int()
# a=1
# if len(chisla) / 2 != 0:
#     a=int((len(chisla)+a)/2)
# if Nuj_Chislo>chisla[a]:
#     c=len(chisla)
#     a=int(c/2)
#     while chisla[a]!=Nuj_Chislo:
#         if Nuj_Chislo>chisla[a]:
#             i=a
#             a=int((len(chisla)+i)/2)
#         elif Nuj_Chislo<chisla[a]:
#             a=int((i+1)/2)
#             i=a
# elif Nuj_Chislo<chisla[a]:
#     a=int((a+1)/2)
#     while chisla[a]!=Nuj_Chislo:
#         if Nuj_Chislo>chisla[a]:
#             a=int((len(chisla)+i)/2)
#             i=a
#         elif Nuj_Chislo<chisla[a]:
#             i=a
#             a=int((i+1)/2)
# print(a)