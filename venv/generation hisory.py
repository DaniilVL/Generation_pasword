# Name=[]
# a=str()
# age=[]
# b=int()
# i=0
# print('до 3 имен')
# while i!=3:
#     a=str(input())
#     if a=='все':
#         i=3
#     else:
#         Name.append(a)
#         i+=1
# i=0
# print(f'Введите {len(Name)} разных возрастов')
# while i!=len(Name):
#     b=int(input())
#     age.append(b)
#     i+=1
# print(f'И пошел {Name[0]} в лес глухой и увидел он там {Name[1]}. и спросил {Name[0]}  у {Name[1]}, а где {Name[2]}? На что ответил ему {Name[1]} \n - откуда мне знать? \n Тогда спросил {Name[0]} Асколько лет тебе уже ? {Name[1]} сказал:\n уже {age[1]}\n А тебе сколько  мне, ответил {Name[0]} уже {age[0]}, а сколько тогда {Name[2]}, ему уже {age[2]}')




from tkinter import *
import time


def update_clock():
    timer_label.config(text=time.strftime('%H:%M:%S',time.localtime()),
                  font='Times 25')  # change the text of the time_label according to the current time
    root.after(100, update_clock)  # reschedule update_clock function to update time_label every 100 ms

root = Tk()  # create the root window
timer_label = Label(root, justify='center')  # create the label for timer
timer_label.pack()  # show the timer_label using pack geometry manager
root.after(0, update_clock)  # schedule update_clock function first call
root.mainloop()  # start the root window mainloop
















# # a='lol'
# # print(f'и тогда сказала мышка {a}')
# # 827
# # набережная реки сестры д 17, паспорт, 11 утра,
# # import random
# # slovo=str()
# # I=0
# # while I!=100:
# #     bukva=0
# #     print()
# #     if bukva==0:
# #         slovo=slovo +'а'
# #     elif bukva==1:
# #         slovo=slovo+'б'
# #     elif bukva==2:
# #         slovo=slovo +'в'
# #     elif bukva==3:
# #         slovo=slovo +'г'
# #     elif bukva==4:
# #         slovo=slovo +'д'
# #     elif bukva==5:
# #         slovo=slovo +'е'
# #     elif bukva==6:
# #         slovo=slovo +'ё'
# #     elif bukva==7:
# #         'ж'
# #     elif bukva==8:
# #         slovo.append('з')
# #     elif bukva==9:
# #         slovo.append('и')
# #     elif bukva==10:
# #         slovo.append('й')
# #     elif bukva==11:
# #         slovo.append('к')
# #     elif bukva==12:
# #         slovo.append('л')
# #     elif bukva==13:
# #         slovo.append('м')
# #     elif bukva==14:
# #         slovo.append('н')
# #     elif bukva==15:
# #         slovo.append('о')
# #     elif bukva==16:
# #         slovo.append('п')
# #     elif bukva==17:
# #         slovo.append('р')
# #     elif bukva==18:
# #         slovo.append('с')
# #     elif bukva==19:
# #         slovo.append('т')
# #     elif bukva==20:
# #         slovo.append('у')
# #     elif bukva==21:
# #         slovo.append('ф')
# #     elif bukva==22:
# #         slovo.append('х')
# #     elif bukva==23:
# #         slovo.append('ц')
# #     elif bukva==24:
# #         slovo.append('ч')
# #     elif bukva==25:
# #         slovo.append('ш')
# #     elif bukva==26:
# #         slovo.append('щ')
# #     elif bukva==27:
# #         slovo.append('ъ')
# #     elif bukva==28:
# #         slovo.append('ы')
# #     elif bukva==29:
# #         slovo.append('ь')
# #     elif bukva==30:
# #         slovo.append('э')
# #     elif bukva==31:
# #         slovo.append('ю')
# #     elif bukva==32:
# #         slovo.append('я')
# #     elif bukva==33:
# #         slovo.append(' ')
# #     I+=1
# # print(slovo)
#
#
#
#
#
#
#
# import random
# slovo=str()
# I=0
# B=0
# c=0
# z=0
# while c!=1:
#     while I!=999999:
#         bukva=random.randint(0,32)
#         if bukva==0:
#             slovo=slovo + 'а'
#         elif bukva==1:
#             slovo=slovo + 'б'
#         elif bukva==2:
#             slovo=slovo + 'в'
#         elif bukva==3:
#             slovo=slovo + 'г'
#         elif bukva==4:
#             slovo=slovo + 'д'
#         elif bukva==5:
#             slovo=slovo + 'е'
#         elif bukva==6:
#             slovo=slovo + 'ё'
#         elif bukva==7:
#             slovo=slovo + 'ж'
#         elif bukva==8:
#             slovo=slovo + 'з'
#         elif bukva==9:
#             slovo=slovo + 'и'
#         elif bukva==10:
#             slovo=slovo + 'й'
#         elif bukva==11:
#             slovo=slovo + 'к'
#         elif bukva==12:
#             slovo=slovo + 'л'
#         elif bukva==13:
#             slovo=slovo + 'м'
#         elif bukva==14:
#             slovo=slovo + 'н'
#         elif bukva==15:
#             slovo=slovo + 'о'
#         elif bukva==16:
#             slovo=slovo + 'п'
#         elif bukva==17:
#             slovo=slovo + 'р'
#         elif bukva==18:
#             slovo=slovo + 'с'
#         elif bukva==19:
#             slovo=slovo + 'т'
#         elif bukva==20:
#             slovo=slovo + 'у'
#         elif bukva==21:
#             slovo=slovo + 'ф'
#         elif bukva==22:
#             slovo=slovo + 'х'
#         elif bukva==23:
#             slovo=slovo + 'ц'
#         elif bukva==24:
#             slovo=slovo + 'ч'
#         elif bukva==25:
#             slovo=slovo + 'ш'
#         elif bukva==26:
#             slovo=slovo + 'щ'
#         elif bukva==27:
#             slovo=slovo + 'ъ'
#         elif bukva==28:
#             slovo=slovo + 'ы'
#         elif bukva==29:
#             slovo=slovo + 'ь'
#         elif bukva==30:
#             slovo=slovo + 'э'
#         elif bukva==31:
#             slovo=slovo + 'ю'
#         elif bukva==32:
#             slovo=slovo + 'я'
#         # elif bukva==33:
#         #     slovo=slovo + ' '
#         I+=1
#         # print(I)
#     # print(slovo)
#     B='данил'
#     if B in slovo:
#         print('(((')
#         c+=1
#     else:
#         print('((')
#     I=0
#     z+=1
# print(z)