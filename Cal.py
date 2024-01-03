from tkinter import *

win=Tk()
win.geometry("500x500")
win.title('Calculator V')
win.configure(background='cyan')


l=Label(win,text="Welcome to Cal V",font=10,bg='cyan',height=3)
l.place(x=180,y=0)

e=Label(win,text='0',bd='10',font=5)
e.place(x=180,y=100)
o=Label(win,text='',bd='6',font=5)
o.place(x=250,y=100)
p=Label(win,text='0',bd='10',font=5)
p.place(x=300,y=100)

def sign(a):
    o.configure(text=str(a))

def ans(a,b):
    if o.cget('text')=="+":
        l.configure(text=str(int(a)+int(b)))
    elif o.cget('text')=="-":
        l.configure(text=str(int(a)-int(b)))
    elif o.cget('text')=="/":
        l.configure(text=str(int(a)/int(b)))
    elif o.cget('text')=="x":
        l.configure(text=str(int(a)*int(b)))
    l.place(x=240,y=0)
        

def num1():
    if o.cget("text")=="":
        c=e.cget('text')
        e.configure(text=c+"1")
    else:
        c=p.cget('text')
        p.configure(text=c+"1")
def num2():
    if o.cget("text")=="":
        c=e.cget('text')
        e.configure(text=c+"2")
    else:
        c=p.cget('text')
        p.configure(text=c+"2")
def num3():
    if o.cget("text")=="":
        c=e.cget('text')
        e.configure(text=c+"3")
    else:
        c=p.cget('text')
        p.configure(text=c+"3")
def num4():
    if o.cget("text")=="":
        c=e.cget('text')
        e.configure(text=c+"4")
    else:
        c=p.cget('text')
        p.configure(text=c+"4")
def num5():
    if o.cget("text")=="":
        c=e.cget('text')
        e.configure(text=c+"5")
    else:
        c=p.cget('text')
        p.configure(text=c+"5")
def num6():
    if o.cget("text")=="":
        c=e.cget('text')
        e.configure(text=c+"6")
    else:
        c=p.cget('text')
        p.configure(text=c+"6")
def num7():
    if o.cget("text")=="":
        c=e.cget('text')
        e.configure(text=c+"7")
    else:
        c=p.cget('text')
        p.configure(text=c+"7")
def num8():
    if o.cget("text")=="":
        c=e.cget('text')
        e.configure(text=c+"8")
    else:
        c=p.cget('text')
        p.configure(text=c+"8")
def num9():
    if o.cget("text")=="":
        c=e.cget('text')
        e.configure(text=c+"9")
    else:
        c=p.cget('text')
        p.configure(text=c+"9")
def num0():
    if o.cget("text")=="":
        c=e.cget('text')
        e.configure(text=c+"0")
    else:
        c=p.cget('text')
        p.configure(text=c+"0")


N1=Button(win,text='1',bd=10,command=num1)
N1.place(x=200,y=250)
N2=Button(win,text='2',bd=10,command=num2)
N2.place(x=240,y=250)
N3=Button(win,text='3',bd=10,command=num3)
N3.place(x=280,y=250)
N4=Button(win,text='4',bd=10,command=num4)
N4.place(x=200,y=300)
N5=Button(win,text='5',bd=10,command=num5)
N5.place(x=240,y=300)
N6=Button(win,text='6',bd=10,command=num6)
N6.place(x=280,y=300)
N7=Button(win,text='7',bd=10,command=num7)
N7.place(x=200,y=350)
N8=Button(win,text='8',bd=10,command=num8)
N8.place(x=240,y=350)
N9=Button(win,text='9',bd=10,command=num9)
N9.place(x=280,y=350)
N0=Button(win,text='0',bd=10,command=num0)
N0.place(x=320,y=350)


s=Button(win,text='+',fg='white',bg='black',bd=10,command=lambda:sign('+'))
s.place(x=160,y=400)

n=Button(win,text='-',fg='white',bg='black',bd=10,command=lambda:sign('-'))
n.place(x=210,y=400)

d=Button(win,text='/',fg='white',bg='black',bd=10,command=lambda:sign('/'))
d.place(x=260,y=400)

m=Button(win,text='X',fg='white',bg='black',bd=10,command=lambda:sign('x'))
m.place(x=310,y=400)

equal=Button(win,text='=',fg='white',bg='grey',bd=20,command=lambda:ans(e.cget('text'),p.cget('text')))
equal.place(x=380,y=300)

win.mainloop()