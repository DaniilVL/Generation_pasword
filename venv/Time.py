import time
import tkinter as tk
from tkinter import messagebox



window=tk.Tk()
window.geometry('320x320')
window.resizable(width=False, height=False)

def oshibka():
    messagebox.showwarning('ошибка','.')

def one_key_press(event: tk.Event):
    if event.keysym == "BackSpace":
        return None  # Не блокируем BackSpace
    if len(pole_o.get()) >= 2:
        return 'break'
    elif event.char.isdigit():
        return None
    else:
        return 'break'


def two_key_press(event: tk.Event):
    if event.keysym == "BackSpace":
        return None  # Не блокируем BackSpace
    if len(pole_t.get()) >= 2:
        return 'break'
    elif event.char.isdigit():
        return None
    else:
        return 'break'

def tre_key_press(event: tk.Event):
    if event.keysym == "BackSpace":
        return None  # Не блокируем BackSpace
    if len(pole_tr.get()) >= 2:
        return 'break'
    elif event.char.isdigit():
        return None
    else:
        return 'break'

def oshibka_sec():
    messagebox.showwarning('ошибка',"Числовое значения для секундного поля должно находиться в пределах от 0 до 59")

def oshibka_min():
    messagebox.showwarning('ошибка',"Числовое значения для минутного поля должно находиться в пределах от 0 до 59")

def times():
    global i
    chas=pole_o.get()
    min=pole_t.get()
    sec=pole_tr.get()
    print(chas,min,sec)
    while i != 2:
        print(1)
        if int(min) >=60:
            print('a')
            pole_t.delete(0,tk.END)
            oshibka_min()
            min = pole_t.get()
        elif int(sec) >=60:
            print('b')
            pole_tr.delete(0, tk.END)
            oshibka_sec()
            sec=pole_tr.get()
        else:
            print('fsdfsdf')
            i=2
    vsego=int(chas)*3600+int(min)*60+int(sec)
    print(type(vsego))
    # pole_tr.insert(0, 2)
    time.sleep(1)
    chas=int(chas)
    min=int(min)
    sec=int(sec)
    while min and sec and chas ==0:
        MIN=min
        while MIN!=0:
            SEC=sec
            while SEC!=0:
                SEC-=1
                time.sleep(1)
                print(SEC)
            min-=1
            sec=59
            print(chas,min,sec)

    print(chas,min,sec)

i=0
#лабел оставегося времени
ost=tk.Label(text='осталось времни')
ost.pack()


sto=tk.Label(text='чч')
sto.place(relx=0.01,rely=0.11,relheight=0.1,relwidth=0.1)
sto=tk.Label(text='мм')
sto.place(relx=0.3,rely=0.11,relheight=0.1,relwidth=0.1)
sto=tk.Label(text='cc')
sto.place(relx=0.6,rely=0.11,relheight=0.1,relwidth=0.1)

#поля
pole_o=tk.Entry()
pole_o.place(relx=0.1,rely=0.11,relheight=0.1,relwidth=0.2)
pole_o.bind("<KeyPress>", one_key_press)


pole_t=tk.Entry()
pole_t.place(relx=0.4,rely=0.11,relheight=0.1,relwidth=0.2)
pole_t.bind("<KeyPress>", two_key_press)

pole_tr=tk.Entry()
pole_tr.place(relx=0.7,rely=0.11,relheight=0.1,relwidth=0.2)
pole_tr.bind("<KeyPress>", tre_key_press)

but=tk.Button(text='Запустить таймер',command=times)
but.place(relx=0.3,rely=0.3,relheight=0.1,relwidth=0.4)


window.mainloop()









# for j in range(vsego):
#     time.sleep(1)
#     print(vsego)
#     pole_tr.insert(0, vsego - 3660)
#     if vsego % 360 == 0:
#         fdfs



# def oshibka():
#     messagebox.showwarning('ошибка',"Числовое значения для секундного и минутного поля должн находиться в пределах от 0 до 59")
#
# def time():
#     chas=pole_o.get()
#     min=pole_t.get()
#     sec=pole_tr.get()
#     if min or sec >=60:
#         oshibka()
#         print('ji,brf')
#     print(chas,min,sec)






# def oshibka_sec():
#     messagebox.showwarning('ошибка',"Числовое значения для секундного поля должно находиться в пределах от 0 до 59")
#
# def oshibka_min():
#     messagebox.showwarning('ошибка',"Числовое значения для минутного поля должно находиться в пределах от 0 до 59")
#
# def time():
#     chas=pole_o.get()
#     min=pole_t.get()
#     sec=pole_tr.get()
#     if min >=60:
#         oshibka_min()
#     elif sec >=60:
#         oshibka_sec()