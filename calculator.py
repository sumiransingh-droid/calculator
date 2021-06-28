import auto_py_to_exe
from tkinter import *
from tkinter import messagebox
import math
screen = Tk()
screen.title("My Calculator")
screen.configure(bg='purple')
screen.maxsize(width=470,height=490)
screen.minsize(width=470,height=490)
screen.iconbitmap('calculator.ico')

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification','Try again something is wrong',parent=screen)

def cmsin():
   global operator
   try:
       result = math.sin(eval(tex.get()))
       operator = str(result)
       tex.set(operator)
   except:
       messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)


def cmcos():
   global operator
   try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
   except:
        messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)


def cmtan():
    global operator
    try:
       result = math.tan(eval(tex.get()))
       operator = str(result)
       tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)


def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
          messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)

def cmlog():
   global operator
   try:
       result = math.log(eval(tex.get()))
       operator = str(result)
       tex.set(operator)
   except:
       messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)

tex = StringVar()
operator = ''

entry1 = Entry(screen,bg='orange',font=('arial',20,'italic bold'),bd='30',justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,text='7',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(7),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btn7.grid(row=1,column=0)

btn8 = Button(screen,text='8',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(8),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btn8.grid(row=1,column=1)

btn9 = Button(screen,text='9',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(9),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btn9.grid(row=1,column=2)

btnadd = Button(screen,text='+',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('+'),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text="4",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(4),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btn4.grid(row=2,column=0)

btn5 = Button(screen,text="5",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(5),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btn5.grid(row=2,column=1)

btn6 = Button(screen,text="6",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(6),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btn6.grid(row=2,column=2)

btnsub = Button(screen,text="-",font=('arial',20,'italic bold'),bd=8,padx=18,pady=16,command=lambda:click('-'),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btnsub.grid(row=2,column=3)

btn1 = Button(screen,text="1",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(1),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btn1.grid(row=3,column=0)

btn2 = Button(screen,text="2",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(2),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btn2.grid(row=3,column=1)

btn3 = Button(screen,text="3",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(3),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btn3.grid(row=3,column=2)

btnmul = Button(screen,text="*",font=('arial',20,'italic bold'),bd=8,padx=18,pady=16,command=lambda:click('*'),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btnmul.grid(row=3,column=3)

btn0 = Button(screen,text="0",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(0),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btn0.grid(row=4,column=0)

btnc = Button(screen,text="C",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=clear,
              activebackground='dark grey',activeforeground='white',bg='light grey')
btnc.grid(row=4,column=1)

btneql = Button(screen,text="=",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=equal,
              activebackground='dark grey',activeforeground='white',bg='light grey')
btneql.grid(row=4,column=2)

btndiv = Button(screen,text="/",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('/'),
              activebackground='dark grey',activeforeground='white',bg='light grey')
btndiv.grid(row=4,column=3)

##############################################advance calculation


btnsin = Button(screen,text="sin",font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=cmsin,
              activebackground='dark grey',activeforeground='white',bg='light grey')
btnsin.grid(row=0,column=5)

btncos = Button(screen,text="cos",font=('arial',20,'italic bold'),bd=8,padx=13,pady=16,command=cmcos,
              activebackground='dark grey',activeforeground='white',bg='light grey')
btncos.grid(row=1,column=5)

btntan = Button(screen,text="tan",font=('arial',20,'italic bold'),bd=8,padx=15,pady=16,command=cmtan,
              activebackground='dark grey',activeforeground='white',bg='light grey')
btntan.grid(row=2,column=5)

btnsqrt = Button(screen,text="sqrt",font=('arial',20,'italic bold'),bd=8,padx=10,pady=16,command=cmsqrt,
              activebackground='dark grey',activeforeground='white',bg='light grey')
btnsqrt.grid(row=3,column=5)

btnlog = Button(screen,text="log",font=('arial',20,'italic bold'),bd=8,padx=15,pady=16,command=cmlog,
              activebackground='dark grey',activeforeground='white',bg='light grey')
btnlog.grid(row=4,column=5)

screen.mainloop()








