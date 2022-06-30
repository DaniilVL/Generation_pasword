import tkinter as tk
import random

window=tk.Tk()
window.geometry('400x320')
window.resizable(width=False, height=False)
a=1
i=0
bukv=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
simbol=['`','#','$','%','^','&','*','_','(',')','!','/']

def two_key_press(event: tk.Event):
    if event.keysym == "BackSpace":
        return None  # Не блокируем BackSpace
    elif event.char.isdigit():
        return None
    elif event.char in '\r':
        gener()
    else:
        return 'break'


def one_key_press(event: tk.Event):
        return 'break'

def gener():
    pole.delete(0,tk.END)
    l=Len.get()
    l=int(l)
    global i
    i=0
    while i!=l:
        a=random.randint(1,4)
        # print('vibor',a)
        if a==1:
            z = random.randint(0, 25)
            # print('mal',z)
            pole.insert(0,bukv[z])
            i+=1
        elif a==2:
            z = random.randint(0,25)
            # print('bol',z)
            pole.insert(0, bukv[z].upper())
            i += 1
        elif a==3:
            z = random.randint(0, 12)
            # print('simb',z)
            pole.insert(0, simbol[z])
            i += 1
        elif a==4:
            z = random.randint(0, 9)
            # print('chis',z)
            pole.insert(0, z)
            i += 1
        # print('i=',i)


def copy():
    Z = pole.get()
    window.clipboard_append(Z)

def copySave():
    save=open('paroly.txt','a+')
    Z=pole.get()
    z=servis.get()
    save.write(z+'\n')
    save.write(Z +'\n')
    save.close()
    print('sdasdas')

opis=tk.Label(text='For which social network you need generate a password?')
opis.place(relx=0.05,rely=0.01,relheight=0.1,relwidth=0.9)
servis=tk.Entry() #Для чего пароль
servis.place(relx=0.05,rely=0.11,relheight=0.1,relwidth=0.6)

opis=tk.Label(text='your password')
opis.place(relx=0.05,rely=0.2,relheight=0.1,relwidth=0.9)
pole=tk.Entry() #Поле, где будет сгенерирован пароль
pole.place(relx=0.05,rely=0.3,relheight=0.1,relwidth=0.6)
pole.bind("<KeyPress>", one_key_press)

LenPas=tk.Label(text='how many characters should be in your password')
LenPas.place(relx=0.05,rely=0.4,relheight=0.1,relwidth=0.9)
Len=tk.Entry() #Поле для ввода длины пароля
Len.place(relx=0.05,rely=0.5,relheight=0.1,relwidth=0.2)
Len.bind("<KeyPress>", two_key_press)

generation=tk.Button(text='generation', command=gener) #Кнопка для генерации пароля
generation.place(relx=0.05,rely=0.65,relheight=0.1,relwidth=0.3)

copy=tk.Button(text='Copy',command=copy)
copy.place(relx=0.7,rely=0.3,relheight=0.1,relwidth=0.25)

copySave=tk.Button(text='Copy and Save',command=copySave)
copySave.place(relx=0.7,rely=0.11,relheight=0.1,relwidth=0.25)

window.mainloop()

