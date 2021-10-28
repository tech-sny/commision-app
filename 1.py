from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os,sys


def ll_del():
      global s,p
      file=open("user.doc","r")
      lines= file.readlines()
      file.close
      w=open("user.doc","w")
      w.writelines([item for item in lines[:-1]])
      w.close()
      s=s-p
      p=0
      
      
      
      


def x_info():
      global c1,a,j
      file=open("user.doc","a")
      a=int(xr.get())
      j=int(xr1.get())
      c1=a*j
      file.write("--------------------------------------------\n")
      file.write("TOTAL X-RAY = "+str(a)+" *  "+str(j)+" = "+str(c1)+"\n")
      print("TOTAL X-RAY = "+str(a)+" *  "+str(j)+" = "+str(c1)+"\n")
      xr.set("X-RAY SUCCESSFULLY")
      xr1.set("CALCULATED")
      
      file.close()
     
def x_info1():
      button7.place_forget()
      xr_text.place(x=15,y=390)
      xr1_text.place(x=250,y=390)
      xr_entry.place(x=15,y=430)
      xr1_entry.place(x=250,y=430)
      file=open("user.doc","a")
      file.write("\ntotal pathology = "+str(s)+"\n")
      file.close()
      



     
def  add_amt(event=None):
     global c2
     c2=c2+1
     a1=int(amt.get())
     global r
     global s,p
     file=open("user.doc","a")
     firstname_info = firstname.get()
     if(c2==1):
           
           if(firstname_info<10):
                file.write("0" + str(firstname_info)+" - "+m+" - "+str(y))
           else:
                file.write(" " + str(firstname_info)+" - "+m+" - "+str(y))
           file.write("  -----------> ")
           file.write(str(a1))
     else:
            file.write(" + "+str(a1))
     s=s+a1
     r=r+a1
     p=r
     print(str(firstname_info)+" "+str(a1)+" "+str(s))
     amt.set('')
     file.close
    
     

def delete_info():
     file = open("user.doc","w")
     file.truncate(0)
     file.close
     button2.place_forget()


def calc_info():
    global r,c1,l
    r=0
    file = open("user.doc","a")
    global s
    if(c1!=1):
          l=s/2
          s1=l+c1
          file.write("--------------------------------------------\n")
          file.write(" 50%  of pathology=  "+str(l))
          file.write("\n")
          file.write("TOTAL =  "+str(l)+" + "+str(c1)+" = "+str(s1))
          file.write("\n")
          
    else:
            c1=0
            l=s
            s1=l/2
            file.write("--------------------------------------------\n")
            file.write("TOTAL =  "+str(s)+" + "+" = "+str(l))
            file.write("\n")
            file.write(" 50%  =  "+str(s1))
    
    print("TOTAL PATH = "+str(s))
    print("\n")
    print("TOT= "+str(s1))
    file.close
    firstname.set("FILE CREATED")
    amt.set("THANK YOU")
    
    
  
def next_info():
    global m,y
    docname_text.place_forget()
    mnt_text.place_forget()
    yr_text.place_forget()
    button3.place_forget()
    doc_name_entry.place_forget()
    mnt_entry.place_forget()
    yr_entry.place_forget()
    doc1=docname.get()
    m=mnt.get()
    y=yr.get()
    docname_text1= Label(text="Dr. "+doc1+"       "+m+"   "+str(y))
    docname_text1.place(x=100,y=75)
    file = open("user.doc","a")
    file.write("\n")
    file.write("\n")
    file.write("      LIFE PATHOLOGY AND X-RAY CENTRE\n")
    file.write("\n")
    file.write("         Dr.  " + doc1+"       "+m+"   "+str(y)+"\n")
    file.write("\n")
    

    

def save_info(event=None):
     global r
     global s
     global c2,p
     global c1,a
     
     firstname_info = int(firstname.get())
     amt_info = int(amt.get())
     s=s+amt_info
     print(firstname_info,amt_info,s)
     file = open("user.doc","a")
    
     if(c2==0):
          #file.write("\n")
          if(firstname_info<10):
                file.write("0" + str(firstname_info)+" - "+m+" - "+str(y))
          else:
                file.write(" " + str(firstname_info)+" - "+m+" - "+str(y))
          file.write("  -----------> ")
          file.write(" = " + str(amt_info))
     elif(c2>=1):
          #file.write("\n")
          file.write(" + "+str(amt_info))
          r=r+amt_info
          p=p+amt_info
          file.write(" = " + str(r))
          
         
          
          
          c2=0
     r=0
     file.write("\n")
     amt.set('')
     firstname.set(firstname_info+1)
     
     file.close()
          
          
          
    
#frame heading
s=0    #global variable for total calulation of month
r=0     #global variable for total calculation a day
c1=0
c2=0
c1=c1+1
m=""
y=0
j=0
p=0
app = tk.Tk()
app.geometry("600x600")
app.title(" LIFE PATHOLOGY AND X-RAY COMMISSION  FORM")
heading = Label(text="COMMISSION FORM",fg="black",bg="mistyrose",width="500",height="3",font="10")
heading.pack()
xray_part = Label(text="------------------------------------------------X-RAY------------------------------------------")
xray_part.place(x=3,y=360)
#doctor detail
docname_text = Label(text="DOCTOR NAME :")
docname_text.place(x=15,y=120)
docname = StringVar()
doc_name_entry = Entry(textvariable=docname,width="20")
doc_name_entry.place(x=15,y=150)

mnt_text = Label(text="ENTER  MONTH:")
mnt_text.place(x=155,y=120)
mnt = StringVar()
mnt_entry = Entry(textvariable=mnt,width="20")
mnt_entry.place(x=155,y=150)

yr_text = Label(text="ENTER YEAR :")
yr_text.place(x=295,y=120)
yr = IntVar()
yr_entry = Entry(textvariable=yr,width="20")
yr.set("")
yr_entry.place(x=295,y=150)

button3 = Button(app,text="NEXT",command=next_info,width="10",height="1",bg="PaleTurquoise")
button3.place(x=450,y=145)




#name
firstname_text = Label(text="DATE :")
firstname_text.place(x=15,y=180)
firstname = IntVar()
first_name_entry = Entry(textvariable=firstname,width="30")
first_name_entry.place(x=15,y=210)


#amount
amt_text = Label(app,text="AMOUNT :")
amt_text.place(x=15,y=240)
amt = IntVar()
amt.set("")
amt_entry = Entry(textvariable=amt,width="30")
amt_entry.place(x=15,y=270)

#sumit button
button = Button(app,text="SUBMIT DATA",command=save_info,width="20",height="2",bg="PaleTurquoise")
button.place(x=15,y=320)

#delete button
button2 = Button(app,text="DELETE",command=delete_info,width="20",height="2",bg="PaleTurquoise")
button2.place(x=15,y=70)

#add in amount button
button5= Button(app,text="+",command=add_amt,width="10",height="1",bg="PaleTurquoise")
button5.place(x=220,y=265)

#complete button
button4 = Button(app,text="COMPLETE",command=calc_info,width="60",height="2",bg="burlywood")
button4.place(x=15,y=500)
    
#x ray
button6= Button(app,text="X-RAY",command=x_info,width="10",height="1",bg="PaleTurquoise")
button6.place(x=450,y=430)

button7= Button(app,text="ENTER DETAILS OF X-RAY",command=x_info1,width="30",height="2",bg="PaleTurquoise")
button7.place(x=15,y=390)

button8= Button(app,text="DELETE LAST LINE",command=ll_del,width="20",height="1",bg="PaleTurquoise")
button8.place(x=400,y=265)

xr_text = Label(text="ENTER NUMBER OF X-RAY :")

xr = IntVar()
xr.set("")
xr_entry = Entry(textvariable=xr,width="30")

xr1_text = Label(text="ENTER THE COST OF 1 X-RAY :")
xr1 = IntVar()
xr1.set("")
xr1_entry = Entry(textvariable=xr1,width="30")


app.bind("<Shift_R>",add_amt)
app.bind("<Return>",save_info)
mainloop()

