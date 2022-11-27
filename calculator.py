from logging import root
import math
from tkinter import *
from math import *
def sin():
   get= math.sin(math.radians(float(expression.get())))
   strvar.set(get)
   expression.update()

def cos():
   get= math.cos(math.radians(float(expression.get())))
   strvar.set(get)
   expression.update()

def tan():
   get= math.tan(math.radians(float(expression.get())))
   strvar.set(get)
   expression.update()

def sqrt():
   get= math.sqrt(float(expression.get()))
   strvar.set(get)
   expression.update()

def backspace():
    exlen=len(expression.get())
    expression.delete(exlen-1)

def click(event):
    global strvar
    gettext=event.widget.cget("text")  #to get the value of button text we use event ke widget mai c get 
    
    if gettext=="C":
        strvar.set("")
        expression.update()
    elif gettext=="=":
        if strvar.get().isdigit():
            int(strvar.get())
        else:
            try:
               strvar.set(eval(expression.get()))
               expression.update()
                
            except:
                strvar.set("Error")
                expression.update()
    
    else:

        strvar.set(strvar.get()+gettext)  #to show the expression on the screen
        expression.update()

root=Tk()


root.title("Calculator")
root.configure(background="grey",bd=5,relief=SUNKEN)
root.resizable(0,0)
#root.wm_iconbitmap("bb.png")
strvar=StringVar()
strvar.set("")
expression=Entry(root,font=("helvetica",15,"bold"),relief=RAISED,textvariable=strvar,bd=6,background="white",width=23)
expression.grid(columnspan=10)



#---------------------------creating number buttons of calculator--------------------------------------------------
numberpad='789456123'
i=0
btn=[]
for j in range(1,4):
    for k in range(3):
        btn.append(Button(root,text=numberpad[i],background="black",bd=5,foreground="white",font=("helvetica",14,"bold"),width=2))
        btn[i].grid(row=j,column=k)
        btn[i].bind("<Button-1>",click)
        i+=1

#0 button
b0=Button(root,text="0",background="black",bd=5,foreground="white",font=("helvetica",16,"bold"),width=2)
b0.grid(row=4,column=1,padx=3)

#---------------------------creating arithmetic buttons----------------------------------------------------------
#Multiply button
multiply=Button(root,text="*",background="black",bd=5,foreground="white",font=("helvetica",15,"bold"),width=2)
multiply.grid(row=1,column=3,padx=3)
#Addition button
add=Button(root,text="+",background="black",bd=5,
foreground="white",font=("helvetica",15,"bold"),height=3,width=2)
add.grid(row=3,column=3,rowspan=2) 
#Divide button
div=Button(root,text="/",background="black",bd=5,foreground="white",font=("helvetica",16,"bold"),width=2)
div.grid(row=1,column=4,padx=3)
#subtraction button
sub=Button(root,text="-",background="black",bd=5,foreground="white",font=("helvetica",16,"bold"),width=2)
sub.grid(row=2,column=4)
#equals button
equal=Button(root,text="=",background="black",bd=5,foreground="white",font=("helvetica",14,"bold"),width=2)
equal.grid(row=3,column=4)
#Clear button
clear=Button(root,text="C",background="orange",bd=5,foreground="black",font=("helvetica",14,"bold"),width=2)
clear.grid(row=4,column=0)
#Decimal button5
point=Button(root,text=".",background="black",bd=5,foreground="white",font=("helvetica",14,"bold"),width=2)
point.grid(row=4,column=2)
#percentage button
per=Button(root,text="%",background="black",bd=5,foreground="white",font=("helvetica",14,"bold"),width=2)
per.grid(row=2,column=3)

back=Button(root,text="←",background="black",bd=5,foreground="white",font=("arial black",13),width=2,command=backspace)
back.grid(row=4,column=4)

#-------------------------------------scientific  operators-------------------------------------------------------

sin=Button(root,text="sin",background="black",bd=5,foreground="white",font=("arial black",13,'bold'),width=2,command=sin)
sin.grid(row=1,column=5)

cos=Button(root,text="cos",background="black",bd=5,foreground="white",font=("arial black",13,'bold'),width=2,command=cos)
cos.grid(row=2,column=5)

tan=Button(root,text="tan",background="black",bd=5,foreground="white",font=("arial black",13,'bold'),width=2,command=tan)
tan.grid(row=3,column=5)

sqr=Button(root,text="√",background="black",bd=5,foreground="white",font=("arial black",13,'bold'),width=2,command=sqrt)
sqr.grid(row=4,column=5)

l1=[add,sub,div,multiply,clear,point,equal,per,b0]
for i in l1:
    i.bind("<Button-1>",click)

root.mainloop()
