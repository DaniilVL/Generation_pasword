import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.resizable(width=False, height=False)
window.wm_attributes('-alpha', 0.8)
window.geometry('640x480')
bukva=tk.Label()
bukva.place(relx=0.7, rely=0.175)
gorod=tk.Label(text='Введите любую букву:')
gorod.place(relx=0.2, rely=0.15,relheight=0.1,relwidth=0.5)

c = list()
with open('Simbol.txt') as file:
    for i in file:
        c.append(i.strip())
        # print(c)



def on_key_press(event: tk.Event):
    if event.keysym == "BackSpace":
        return None  # Не блокируем BackSpace
    if event.char not in c:
        return "break"  # Блокируем ввод всего кроме букв считанных из файла
    if len(pole.get()) >= 1:
        return "break"  # Блокируем ввод, если уже что-то введено (текстовое поле не пустое)
    # Можно объединить в один if, но оставлю отдельно для наглядности


def two_key_press(event: tk.Event):
    if event.keysym == "BackSpace":
        return None  # Не блокируем BackSpace
    if event.char not in c:
        return "break"  # Блокируем ввод всего кроме букв считанных из файла

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
    print(VvodGoroda[0])
    print(lastBukva)
    if VvodGoroda[0]==lastBukva:
        k=1
    elif VvodGoroda[0]!=lastBukva:
        k=0
    return(k)

def oshibka():
    messagebox.showwarning('ошибка','Данного города не существует.')

def oshibka_2():
    messagebox.showwarning('ошибка', 'Данынй город уже был')
def oshibka_3():
    messagebox.showwarning('ошибка', 'Данный город начинается не на ту букву')



def btn_click():
    global b
    global lastBukva
    global ispGoroda
    global proverka
    if b==0:
        global pervayaBukva
        pervayaBukva = pole.get()
        pole.delete(0, tk.END)
        print(pervayaBukva)
        lastBukva=pervayaBukva
        ispGoroda=[pervayaBukva]
        b=1
        print('2',b)

    gorod.config(text='Введите назваение города начинающегося на букву:')
    bukva.config(text=str(lastBukva))
    VvodGoroda=pole.get()
    pole.bind("<KeyPress>", two_key_press)
    pole.delete(0, tk.END)
    print(VvodGoroda)
    provNaPovtor(ispGoroda, VvodGoroda)
    proverkaNaPravila(VvodGoroda, lastBukva)
    bukva.config(text=str(lastBukva))
    if k == 1:
        if Povtor == 0:
            proverka = 2
        elif Povtor == 1:
            provGorodov(vnutrSpisok, VvodGoroda)
        print('3',ispGoroda)
    elif k == 0:
        proverka = 3
    poslBukva = ispGoroda[-1]
    if poslBukva[-1] == 'ь' and 'ъ':
        lastBukva = poslBukva[-2]
    else:
        lastBukva = poslBukva[-1]
    if proverka == 1:
        print('Отлично!, введите город на букву:', lastBukva)
    elif proverka == 0:
        oshibka()
        print('Такого города нет, введите город на:', lastBukva)
    elif proverka == 2:
        oshibka_2()
        print('Данный город уже был, введите город на:', lastBukva)
    elif proverka == 3:
        oshibka_3()
        print('Данный город не начинается на:', lastBukva, 'Введите город на букву:', lastBukva)
    bukva.config(text=str(lastBukva))

def pdsk_click():
    for i in vnutrSpisok:
        if i[0]==lastBukva:
            Spis_Podsk.append(i)
            for i in Spis_Podsk:
                if i not in ispGoroda:
                    Gorod.append(i)
                    break
    print(Gorod)

    messagebox.showwarning('подсказка', Gorod[0])

Povtor=1
b=0
Spis_Podsk=[]
vnutrSpisok=[]
ispGoroda=str()
pervayaBukva=str()
lastBukva=str()
proverka=int()
Gorod=[]
pole=tk.Entry()
with open('SpisokGorodov.txt') as file:
    for i in file:
        vnutrSpisok.append(i.strip().lower())
print(vnutrSpisok)
pole.place(relx=0.35,rely=0.25,relheight=0.1,relwidth=0.3)
pole.bind("<KeyPress>", on_key_press)
knoka=tk.Button(text='Нажми сюда, что бы ввести город',command=btn_click)
knoka.place(relx=0.10,rely=0.4,relheight=0.1,relwidth=0.35)
podskazka=tk.Button(text='Подсказка',command=pdsk_click)
podskazka.place(relx=0.50,rely=0.4,relheight=0.1,relwidth=0.35)
window.mainloop()