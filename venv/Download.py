import tkinter as tk
from tkinter import messagebox

calck=tk.Tk()
calck.geometry('320x400')
calck.resizable(width=False, height=False)
polosa=tk.Label(text='KALKULYATOR')
polosa.pack()
c=[]
o=1
z=1


def two_key_press(event: tk.Event):
    if event.keysym == "BackSpace":
        return None  # Не блокируем BackSpace
    elif event.char.isdigit():
        return None
    elif event.char in '\r':
        Travno()
    elif event.char in'+-)(*^!%':
        return None
    else:
        return 'break'


def bacsp(arg):
    pole.delete(pole.index(tk.END) - 1)

def clear(arg):
    pole.delete(0,tk.END)

def btn_clck(arg):
    a=pole.get()
    pole.delete(0, tk.END)
    a=a+arg
    pole.insert(0,a)

def Travno():
    try:
        rezult=pole.get()
        rezult =rezult
        print(type(rezult))
        print(rezult)
        pole.delete(0, tk.END)
        print(eval(rezult))
        pole.insert(0,eval((rezult)))
    except ZeroDivisionError:
        pole.insert(0,'На ноль делить нельзя!')

def facktorial(arg):
    global o
    global z
    o = pole.get()
    o=int(o)
    while o!=0:
        z=z*o
        o-=1
    pole.insert(0,z)

def Copyr():
    a=pole.get()
    pole.delete(0,tk.END)
    calck.clipboard_append(a)


copy=tk.Button(text='Copy', command=Copyr)
copy.place(relx=0.75,rely=0.15,relheight=0.1,relwidth=0.2)

pole=tk.Entry(calck,justify=tk.RIGHT)
pole.place(relx=0.05,rely=0.15,relheight=0.1,relwidth=0.65)
pole.bind("<KeyPress>", two_key_press)
one=tk.Button(text='%', command=lambda arg='%':btn_clck(arg))
one.place(relx=0.02,rely=0.30,relheight=0.1,relwidth=0.22)
two=tk.Button(text='^', command=lambda arg='^':btn_clck(arg))
two.place(relx=0.26,rely=0.30,relheight=0.1,relwidth=0.22)
tree=tk.Button(text='!', command=lambda arg='!':facktorial(arg))
tree.place(relx=0.50,rely=0.30,relheight=0.1,relwidth=0.22)
four=tk.Button(text='**0.5', command=lambda arg='**0.5':btn_clck(arg))
four.place(relx=0.74,rely=0.30,relheight=0.1,relwidth=0.22)

five=tk.Button(text='(', command=lambda arg='(':btn_clck(arg))
five.place(relx=0.02,rely=0.41,relheight=0.1,relwidth=0.22)
six=tk.Button(text=')', command=lambda arg=')':btn_clck(arg))
six.place(relx=0.26,rely=0.41,relheight=0.1,relwidth=0.22)
seven=tk.Button(text='/', command=lambda arg='/':btn_clck(arg))
seven.place(relx=0.50,rely=0.41,relheight=0.1,relwidth=0.22)
eigth=tk.Button(text='-', command=lambda arg='-':btn_clck(arg))
eigth.place(relx=0.74,rely=0.41,relheight=0.1,relwidth=0.22)

nain=tk.Button(text='7', command=lambda arg='7':btn_clck(arg))
nain.place(relx=0.02,rely=0.52,relheight=0.1,relwidth=0.22)
ten=tk.Button(text='8', command=lambda arg='8':btn_clck(arg))
ten.place(relx=0.26,rely=0.52,relheight=0.1,relwidth=0.22)
elven=tk.Button(text='9', command=lambda arg='9':btn_clck(arg))
elven.place(relx=0.50,rely=0.52,relheight=0.1,relwidth=0.22)
twelv=tk.Button(text='*', command=lambda arg='*':btn_clck(arg))
twelv.place(relx=0.74,rely=0.52,relheight=0.1,relwidth=0.22)

thirteen=tk.Button(text='4', command=lambda arg='4':btn_clck(arg))
thirteen.place(relx=0.02,rely=0.63,relheight=0.1,relwidth=0.22)
fourteen=tk.Button(text='5', command=lambda arg='5':btn_clck(arg))
fourteen.place(relx=0.26,rely=0.63,relheight=0.1,relwidth=0.22)
faiveteen=tk.Button(text='6', command=lambda arg='6':btn_clck(arg))
faiveteen.place(relx=0.50,rely=0.63,relheight=0.1,relwidth=0.22)
sixteen=tk.Button(text='+', command=lambda arg='+':btn_clck(arg))
sixteen.place(relx=0.74,rely=0.63,relheight=0.1,relwidth=0.22)

seventeen=tk.Button(text='1', command=lambda arg='1':btn_clck(arg))
seventeen.place(relx=0.02,rely=0.74,relheight=0.1,relwidth=0.22)
eghtteen=tk.Button(text='2', command=lambda arg='2':btn_clck(arg))
eghtteen.place(relx=0.26,rely=0.74,relheight=0.1,relwidth=0.22)
nainghtteen=tk.Button(text='3',command=lambda arg='3':btn_clck(arg))
nainghtteen.place(relx=0.50,rely=0.74,relheight=0.1,relwidth=0.22)
twenty=tk.Button(text='=', command=Travno)
twenty.place(relx=0.74,rely=0.74,relheight=0.1,relwidth=0.22)

tewntyOne=tk.Button(text='0', command=lambda arg='0':btn_clck(arg))
tewntyOne.place(relx=0.02,rely=0.85,relheight=0.1,relwidth=0.22)
tewntyTwo=tk.Button(text='.', command=lambda arg='.':btn_clck(arg))
tewntyTwo.place(relx=0.26,rely=0.85,relheight=0.1,relwidth=0.22)
nainghtteen=tk.Button(text='Backspace', command=lambda arg='Backspace': bacsp(arg))
nainghtteen.place(relx=0.50,rely=0.85,relheight=0.1,relwidth=0.22)
twenty=tk.Button(text='C', command=lambda arg='TC':clear(arg))
twenty.place(relx=0.74,rely=0.85,relheight=0.1,relwidth=0.22)



calck.mainloop()









