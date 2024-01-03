from tkinter import *

win=Tk()
win.geometry("500x500")
win.title('Calculator V')
win.configure(background='cyan')


l=Label(win,text="Welcome to Cal V",font=10,bg='cyan',height=3)
l.place(x=180,y=0)

e=Entry(win,text='',bd='10',font=5)
e.place(x=10,y=100)
p=Entry(win,text='',bd='10',font=5)
p.place(x=250,y=100)

def sum(a,b):
    ans=int(a)+int(b)
    l.configure(text=('Sum:'+str(ans)))
    l.configure(anchor='center')

def div(a,b):
    ans=int(a)/int(b)
    l.configure(text=('Divided:'+ str(ans)))
    l.configure(anchor='center')

def sub(a,b):
    ans=int(a)-int(b)
    l.configure(text=('Subtracted:'+ str(ans)))
    l.configure(anchor='center')

def mult(a,b):
    ans=int(a)*int(b)
    l.configure(text=('Multiplied:'+ str(ans)))
    l.configure(anchor='center')


s=Button(win,text='+',fg='black',bd=10,command=lambda:sum(e.get(),p.get()))
s.place(x=160,y=200)

n=Button(win,text='-',fg='black',bd=10,command=lambda:sub(e.get(),p.get()))
n.place(x=210,y=200)

d=Button(win,text='/',fg='black',bd=10,command=lambda:div(e.get(),p.get()))
d.place(x=260,y=200)

m=Button(win,text='X',fg='black',bd=10,command=lambda:mult(e.get(),p.get()))
m.place(x=310,y=200)


win.mainloop()
