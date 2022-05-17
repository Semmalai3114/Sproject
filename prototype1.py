from tkinter import*
root=Tk()
global number,n
n=0
global num1
num1=0




def say_hi(number):
    global temp
    temp=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(temp)+str(number))
    
def clear():
    e1.delete(0,END)
def add():
    global num1
    num1+=int(e1.get())
    
    global n
    global r
    r="add"
    
    e1.delete(0,END)
    return r,num1

def multiply():
    global num1
    global r
    r="mul"
    num1=int(e1.get())
    e1.delete(0,END)

def sub():
    global s1
    s1=int(e1.get())
    global r
    r="sub"
    e1.delete(0,END)

def div():
    global d1
    d1=int(e1.get())
    global r
    r="div"
    e1.delete(0,END)

def floor():
    global f1
    f1=int(e1.get())
    global r
    r="floor"
    e1.delete(0,END)
def mod():
    global m1
    m1=int(e1.get())
    global r
    r="mod"
    e1.delete(0,END)
def exponential():
    global p1
    p1=int(e1.get())
    global r
    r="exp"
    e1.delete(0,END)
    
   
def equal():
    global num1
    second_number=e1.get()
    e1.delete(0,END)
    if r=="add":
        e1.insert(0,int(num1)+int(second_number))
        
    elif r=="sub":
        e1.insert(0,s1-int(second_number))
    elif r=="mul":
        e1.insert(0,num1*int(second_number))
    elif r=="div":
        e1.insert(0,d1/int(second_number))
    elif r=="floor":
        e1.insert(0,f1//int(second_number))
    elif r=="mod":
        e1.insert(0,m1%int(second_number))
    elif r=="exp":
        e1.insert(0,p1**int(second_number))
   
    
l1=Label(root,text="AKASH CALCULATOR",width=90)
l1.grid(row=0,column=0,columnspan=10,padx=10,pady=10)
e1=Entry(root,width=90,borderwidth=20,bg="white")
e1.grid(row=1,column=0,columnspan=9,padx=10,pady=10)
b1=Button(root,text="1",padx=40,pady=20,command=lambda:say_hi(1),bg="grey")
b2=Button(root,text="2",padx=40,pady=20,command=lambda:say_hi(2),bg="grey")
b3=Button(root,text="3",padx=40,pady=20,command=lambda:say_hi(3),bg="grey")
b4=Button(root,text="4",padx=40,pady=20,command=lambda:say_hi(4),bg="grey")
b5=Button(root,text="5",padx=40,pady=20,command=lambda:say_hi(5),bg="grey")
b6=Button(root,text="6",padx=40,pady=20,command=lambda:say_hi(6),bg="grey")
b7=Button(root,text="7",padx=40,pady=20,command=lambda:say_hi(7),bg="grey")
b8=Button(root,text="8",padx=40,pady=20,command=lambda:say_hi(8),bg="grey")
b9=Button(root,text="9",padx=40,pady=20,command=lambda:say_hi(9),bg="grey")
b10=Button(root,text="0",padx=40,pady=20,command=lambda:say_hi(0),bg="grey")
b11=Button(root,text="/",padx=40,pady=20,command=div,bg="grey")
b12=Button(root,text="*",padx=40,pady=20,command=multiply,bg="grey")
b13=Button(root,text="-",padx=40,pady=20,command=sub,bg="grey")
b14=Button(root,text="+",padx=40,pady=20,command=add,bg="green")
b15=Button(root,text="**",padx=40,pady=20,command=exponential,bg="grey")
b16=Button(root,text="clear",padx=40,pady=20,command=clear,bg="red")
b17=Button(root,text="//",padx=40,pady=20,command=floor,bg="grey")
b18=Button(root,text="=",padx=40,pady=20,command=equal,bg="grey")
b19=Button(root,text="%",padx=40,pady=20,command=mod,bg="grey")
b1.grid(row=5,column=0)
b2.grid(row=5,column=1)
b3.grid(row=5,column=2)
b4.grid(row=6,column=0)
b5.grid(row=6,column=1)
b6.grid(row=6,column=2)
b7.grid(row=7,column=0)
b8.grid(row=7,column=1)
b9.grid(row=7,column=2)
b10.grid(row=8,column=1)
b11.grid(row=5,column=3)
b12.grid(row=6,column=3)
b13.grid(row=7,column=3)
b14.grid(row=8,column=3)
b15.grid(row=8,column=2)
b16.grid(row=8,column=4)
b17.grid(row=7,column=4)
b18.grid(row=8,column=0)
b19.grid(row=6,column=4)
root.mainloop()
