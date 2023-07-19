import tkinter.messagebox 
from tkinter import * 
import random 
import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root") 
mycursor=mydb.cursor() 

mycursor.execute("create database if not exists bank") 
mycursor.execute("use bank") 
#creating required tables  
mycursor.execute("create table if not exists bank_master(acno int(4) primary key,name varchar(30),city  varchar(20),mobileno int(10),balance int(6))") 
mycursor.execute("create table if not exists banktrans(acno int(4),amount int(6),dot date,ttype  char(1),foreign key (acno) references bank_master(acno))") 
mydb.commit() 
def createaccentry(): 
 global e1,e2,e3,e4 
 name=e2.get() 
 city=e3.get() 
 mn=e4.get() 
 balance=0 
 acno=random.randint(999,10000) 
 mycursor.execute("insert into bank_master  
 values('"+str(acno)+"','"+name+"','"+city+"','"+str(mn)+"','"+str(balance)+"')") 
 mydb.commit() 
 k="Your account has been created"
 s="ACC NO." 
 tkinter.messagebox.showinfo("Result",k) 
 tkinter.messagebox.showinfo(s,acno) 
  
def createacc(): 
 global e1,e2,e3,e4 
 root1=Tk() 
 label=Label(root1,text="CREATE ACCOUNT",font='arial 25 bold')  label.pack() 
 frame=Frame(root1,height=500,width=200) 
 frame.pack() 
 l2=Label(root1,text="NAME") 
 l2.place(x=10,y=170) 
 e2=tkinter.Entry(root1) 
 e2.place(x=120,y=170) 
 l3=Label(root1,text="CITY") 
 l3.place(x=10,y=210) 
 e3=tkinter.Entry(root1) 
 e3.place(x=120,y=210) 
 l4=Label(root1,text="PHONE") 
 l4.place(x=10,y=250) 
 e4=tkinter.Entry(root1) 
 e4.place(x=120,y=250) 
 b1=Button(root1,text="SUBMIT",command=createaccentry)  b1.place(x=150,y=370)
  
 root.resizable(False,False) 
 root1.mainloop() 
def depentry(): 
 global y1,y2,y3,y4 
 acno=y1.get() 
 name=y2.get() 
 dp=y3.get() 
 dot=y4.get() 
 ttype="d" 
 mycursor.execute("insert into banktrans values('"+str(acno)+"','"+str(dp)+"','"+dot+"','"+ttype+"')") 
 mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where  acno='"+str(acno)+"' and name='"+name+"'") 
 mydb.commit() 
 k="Your money has been deposited" 
 tkinter.messagebox.showinfo("Result",k) 
  
def deposit(): 
 global y1,y2,y3,y4 
 root2=Tk() 
 label=Label(root2,text="DEPOSIT MONEY",font='arial 25 bold') 
 label.pack() 
 frame=Frame(root2,height=500,width=250) 
 frame.pack() 
 l1=Label(root2,text="ACC.NO(4 Digit)") 
 l1.place(x=10,y=130) 
 y1=tkinter.Entry(root2) 
 y1.place(x=170,y=130) 
 l2=Label(root2,text="NAME") 
 l2.place(x=10,y=170) 
 y2=tkinter.Entry(root2) 
 y2.place(x=170,y=170) 
 l3=Label(root2,text="AMOUNT TO DEPOSIT")  l3.place(x=10,y=210) 
 y3=tkinter.Entry(root2) 
 y3.place(x=170,y=210) 
 l4=Label(root2,text="DATE(YYYY-MM-DD)")  l4.place(x=10,y=250) 
 y4=tkinter.Entry(root2) 
 y4.place(x=170,y=250) 
 b1=Button(root2,text="SUBMIT",command=depentry)  b1.place(x=150,y=370) 
  
 root.resizable(False,False) 
 root2.mainloop() 
def widentry(): 
 global K1,K2,K3,K4 
 acno=K1.get() 
 name=K2.get() 
 wd=K3.get() 
 dot=K4.get() 
 ttype="w" 
 mycursor.execute("insert into banktrans values('"+str(acno)+"','"+str(wd)+"','"+dot+"','"+ttype+"')") 
 mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where  acno='"+str(acno)+"' and name='"+name+"'") 
 mydb.commit() 
 k="Your money has been withdrawn" 
 tkinter.messagebox.showinfo("Result",k) 
  
def withdraw(): 
 global K1,K2,K3,K4 
 root3=Tk() 
 label=Label(root3,text="WITHDRAW MONEY",font='arial 25 bold') 
 label.pack() 
 frame=Frame(root3,height=500,width=200) 
 frame.pack() 
 l1=Label(root3,text="ACC.NO(4 Digit)") 
 l1.place(x=10,y=130) 
 K1=tkinter.Entry(root3) 
 K1.place(x=170,y=130) 
 l2=Label(root3,text="NAME") 
 l2.place(x=10,y=170) 
 K2=tkinter.Entry(root3) 
 K2.place(x=170,y=170) 
 l3=Label(root3,text="AMOUNT TO WITHDRAW")
 l3.place(x=10,y=210) 
 K3=tkinter.Entry(root3) 
 K3.place(x=170,y=210) 
 l4=Label(root3,text="DATE(YYYY-MM-DD)") 
 l4.place(x=10,y=250) 
 K4=tkinter.Entry(root3) 
 K4.place(x=170,y=250) 
 b1=Button(root3,text="SUBMIT",command=widentry) 
 b1.place(x=150,y=370) 
  
 root.resizable(False,False) 
 root3.mainloop() 
def disp(): 
 global i1,i2 
 acno=i1.get() 
 name=i2.get() 
 mycursor.execute("select * from bank_master where acno='"+str(acno)+"' and name='"+name+"'")  for i in mycursor: 
 tkinter.messagebox.showinfo("ACCOUNT DETAILS",i)  
  
def display(): 
 global i1,i2 
 root4=Tk() 
 label=Label(root4,text="DISPLAY ACCOUNT",font='arial 25 bold') 
 label.pack() 
 frame=Frame(root4,height=500,width=200) 
 frame.pack() 
 l1=Label(root4,text="ACC. NO") 
 l1.place(x=10,y=130) 
 i1=tkinter.Entry(root4) 
 i1.place(x=100,y=130) 
 l2=Label(root4,text="NAME") 
 l2.place(x=10,y=170) 
 i2=tkinter.Entry(root4) 
 i2.place(x=100,y=170) 
 b1=Button(root4,text="SUBMIT",command=disp) 
 b1.place(x=150,y=370) 
  
 root.resizable(False,False) 
 root4.mainloop()

 #transferring
def transent(): 
 global L1,L2,L6 
 acno=L1.get() 
 name=L2.get() 
 dp=L6.get() 
 mycursor.execute("select balance from bank_master where acno='"+str(acno)+"' and  name='"+name+"'") 
 for i in mycursor: 
 tkinter.messagebox.showinfo("ACCOUNT BALANCE",i) 
def transfinal(): 
 global L1,L2,L4,L5,L6,L7 
 acno=L1.get() 
 acno1=L4.get() 
 dp=L6.get() 
 dot=L7.get() 
 name=L2.get() 
 name1=L5.get() 
 ttype="w" 
 ttype1="d" 
 mycursor.execute("insert into banktrans values('"+str(acno)+"','"+str(dp)+"','"+dot+"','"+ttype+"')")  mycursor.execute("insert into banktrans values('"+str(acno1)+"','"+str(dp)+"','"+dot+"','"+ttype1+"')") 
 mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where  acno='"+str(acno1)+"' and name='"+name1+"'") 
 mycursor.execute("update bank_master set balance=balance-'"+str(dp)+"' where acno='"+str(acno)+"'  and name='"+name+"'") 
 mydb.commit() 
 k="Your money has been transferred" 
 tkinter.messagebox.showinfo("Result",k) 
  
  
def transfer(): 
 global L1,L2,L4,L5,L6,L7 
 root5=Tk()
 label=Label(root5,text="TRANSFER MONEY",font='arial 25 bold')  label.pack() 
 frame=Frame(root5,height=500,width=200) 
 frame.pack() 
 l1=Label(root5,text="YOUR ACC. NO") 
 l1.place(x=10,y=130) 
 L1=tkinter.Entry(root5) 
 L1.place(x=150,y=130) 
 l2=Label(root5,text="YOUR NAME") 
 l2.place(x=10,y=170) 
 L2=tkinter.Entry(root5) 
 L2.place(x=150,y=170) 
 b1=Button(root5,text="CHECK BALANCE FIRST",command=transent)  b1.place(x=100,y=210) 
 l4=Label(root5,text="RECIEVER'S ACCNO.") 
 l4.place(x=10,y=250) 
 L4=tkinter.Entry(root5) 
 L4.place(x=150,y=250) 
 l5=Label(root5,text="RECIEVER'S NAME") 
 l5.place(x=10,y=290) 
 L5=tkinter.Entry(root5) 
 L5.place(x=150,y=290) 
 l6=Label(root5,text="AMOUNT TO TRANSFER") 
 l6.place(x=10,y=330) 
 L6=tkinter.Entry(root5)
 L6.place(x=150,y=330) 
 l7=Label(root5,text="DATE(YYYY-MM-DD)") 
 l7.place(x=10,y=370) 
 L7=tkinter.Entry(root5) 
 L7.place(x=150,y=370) 
 b2=Button(root5,text="SUBMIT",command=transfinal) 
 b2.place(x=150,y=410) 
  
 root.resizable(False,False) 
 root5.mainloop() 
def deletentry(): 
 global p1,p2 
 acno=p1.get() 
 name=p2.get() 
 mycursor.execute("delete from banktrans where acno='"+str(acno)+"'") 
 mycursor.execute("delete from bank_master where acno='"+str(acno)+"' and name='"+name+"'")  mydb.commit() 
 k="Your account has been deleted" 
 tkinter.messagebox.showinfo("Result",k) 
  
  
 #deleting an account 
def delete(): 
 global p1,p2
 root6=Tk() 
 label=Label(root6,text="DELETE ACCOUNT",font='arial 25 bold')  label.pack() 
 frame=Frame(root6,height=500,width=200) 
 frame.pack() 
 l1=Label(root6,text="ACC. NO") 
 l1.place(x=10,y=130) 
 p1=tkinter.Entry(root6) 
 p1.place(x=100,y=130) 
 l2=Label(root6,text="NAME") 
 l2.place(x=10,y=170) 
 p2=tkinter.Entry(root6) 
 p2.place(x=100,y=170) 
 b1=Button(root6,text="SUBMIT",command=deletentry) 
 b1.place(x=150,y=370) 
  
 root.resizable(False,False) 
 root6.mainloop() 
root=Tk() 
label=Label(root,text="SHR BANK OF INDIA",font="arial 40 bold",bg='white') b1=Button(text="Create Accoount",font="impact 9",bg='cyan',command=createacc) b2=Button(text="Withdraw",font="impact 11",bg='cyan',command=withdraw) b3=Button(text="Deposit",font="impact 11",bg='cyan',command=deposit) b4=Button(text="Transfer",font="impact 11",bg='cyan',command=transfer) 
b5=Button(text="Display Account",font='impact 11',bg='cyan',command=display) b6=Button(text="Delete Account",font='impact 11',bg='cyan',command=delete) b7=Button(text="Exit",font='arial 20 bold',command=root.destroy,bg='yellow') label.pack() 
b1.pack(side=LEFT,padx=10) 
b2.pack(side=LEFT,padx=10) 
b3.pack(side=LEFT,padx=10) 
b4.pack(side=LEFT,padx=10) 
b5.pack(side=LEFT,padx=10) 
b6.pack(side=LEFT,padx=10) 
b7.pack(side=LEFT,padx=10) 
frame=Frame(root,height=400,width=100) 
frame.pack() 
root.resizable(False,False) 
root.mainloop()
