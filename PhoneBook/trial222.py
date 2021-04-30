import sqlite3
import splash
from Tkinter import*
from tkMessageBox import *
root=Tk()
con=sqlite3.Connection('phonebookdb')
cur=con.cursor()
cur.execute("create table if not exists PHONE_DETAILS(contactID integer PRIMARY KEY AUTOINCREMENT,fname varchar2(30),mname varchar2(30),lname varchar2(30),company varchar2(15),address varchar2(50),city char(3),PINCODE integer,website varchar2(20),DOB date)")

cur.execute("create table if not exists PHONE_TYPE_DETAILS(contactID,contact_type varchar2(15),phone_no integer,FOREIGN KEY(contactID) REFERENCES PHONE_DETAILS(contactID))")
cur.execute("create table if not exists MAIL_DETAILS(ContactID,email_id_type,email_id,FOREIGN KEY(contactID) REFERENCES PHONE_DETAILS(contactID))")
i=PhotoImage(file='C:\Users\HP\Desktop\phoneimage.gif')
y=0
Label(root,image=i).grid(row=0,column=1)
Label(root,text='First Name').grid(row=1,column=0)
e1=Entry(root)
e1.grid(row=1,column=1)
Label(root,text='Middle Name').grid(row=2,column=0)
e2=Entry(root)
e2.grid(row=2,column=1)
Label(root,text='Last Name').grid(row=3,column=0)
e4=Entry(root)
e4.grid(row=3,column=1)
Label(root,text='Company Name').grid(row=4,column=0)
e5=Entry(root)
e5.grid(row=4,column=1)
Label(root,text='Address').grid(row=5,column=0)
e6=Entry(root)
e6.grid(row=5,column=1)
Label(root,text='City Name').grid(row=6,column=0)
e7=Entry(root)
e7.grid(row=6,column=1)
Label(root,text='Pin Code').grid(row=7,column=0)
e8=Entry(root)
e8.grid(row=7,column=1)
Label(root,text='Website URL').grid(row=8,column=0)
e9=Entry(root)
e9.grid(row=8,column=1)
Label(root,text='DOB').grid(row=9,column=0)
e10=Entry(root)
e10.grid(row=9,column=1)
Label(root,text='Select Phone Type').grid(row=10,column=0)
v1=IntVar()
v2=IntVar()
Radiobutton(root,text='Office',variable=v1,value=1).grid(row=10,column=1)
Radiobutton(root,text='Home',variable=v1,value=2).grid(row=10,column=2)
Radiobutton(root,text='Mobile',variable=v1,value=3).grid(row=10,column=3)
Label(root,text='Phone Number').grid(row=11,column=0)
e11=Entry(root)
e11.grid(row=11,column=1)
Label(root,text='Select Email Type').grid(row=12,column=0)
Radiobutton(root,text='Office',variable=v2,value=1).grid(row=12,column=1)
Radiobutton(root,text='Personal',variable=v2,value=2).grid(row=12,column=2)
Label(root,text='Email ID').grid(row=13,column=0)
e12=Entry(root)
e12.grid(row=13,column=1)

def fnamefun():
   
    cur.execute("insert into PHONE_DETAILS (fname,mname,lname,company,address,city,PINCODE,website,DOB)values(?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get()))
    cur.execute('select contactID from PHONE_DETAILS ORDER BY contactID DESC')
    fk1=cur.fetchall()
    cur.execute("insert into PHONE_TYPE_DETAILS(contactID,contact_type,phone_no)values(?,?,?)",(fk1[0][0],v1.get(),e11.get()))
    #cur.execute("insert into PHONE_TYPE_DETAILS(contact_type,phone_no)values(?,?)",(v1.get(),e11.get()))
    cur.execute("insert into MAIL_DETAILS(contactID,email_id_type,email_id)values(?,?,?)",(fk1[0][0],v2.get(),e12.get()))
    showinfo('Save','record successfully saved!')
    con.commit()
def closefun():
    
    x=askyesno('close','Do you really want to close?')
    if x==True:
        root.destroy()
def searchfun():
    root1=Tk()
    root1.geometry('650x650')
    def closeroot1():
        root1.destroy()
    Label(root1,text="Searching Phone Book",font='arial 20',bg='blue').grid(row=0,column=1)
    Label(root1,text='Enter Name').grid(row=1,column=0)
    f1=Entry(root1)
    f1.grid(row=1,column=1)
    lb=Listbox(root1)
    lb.grid(row=2,column=1)
    def rawfun(event):
        p=event.char
        f1.insert(END,p)
        cur.execute("select fname from PHONE_DETAILS where fname like ?",('%'+f1.get()+'%',))
        x=cur.fetchall()
        print x
        for i in x:
            lb.insert(0,i[0])
        
    root.bind("<KeyPress>",rawfun)
    #Button(root1,text='search',command=rawfun).grid(row=1,column=2)
    def selfun():
        sel=lb.curselection()
        for i in sel:
            y=lb.get(i)
        lb2=Listbox(root1)
        lb2.grid(row=2,column=1)
        
        cur.execute('select fname from PHONE_DETAILS where fname=?',(y,))
        cur.execute('select contactID from PHONE_DETAILS where fname=?',(y,))
        c=cur.fetchall()
       
        lb2.insert(END,'first name:')
        lb2.insert(END,y)
        
        cur.execute('select mname from PHONE_DETAILS where contactID=?',(c[0][0],))
        m=cur.fetchall()
        
        lb2.insert(END,'middle name:')
        lb2.insert(END,m[0][0])
        
        cur.execute('select lname from PHONE_DETAILS where contactID=?',(c[0][0],))
        last=cur.fetchall()
        lb2.insert(END,'last name:')
        lb2.insert(END,last[0][0])

        cur.execute('select company from PHONE_DETAILS where contactID=?',(c[0][0],))
        com=cur.fetchall()
        lb2.insert(END,'Company name:')
        lb2.insert(END,com[0][0])

        cur.execute('select address from PHONE_DETAILS where contactID=?',(c[0][0],))
        add=cur.fetchall()
        lb2.insert(END,'Adress:')
        lb2.insert(END,add[0][0])

        cur.execute('select city from PHONE_DETAILS where contactID=?',(c[0][0],))
        city=cur.fetchall()
        lb2.insert(END,'City:')
        lb2.insert(END,city[0][0])

        cur.execute('select PINCODE from PHONE_DETAILS where contactID=?',(c[0][0],))
        pin=cur.fetchall()
        lb2.insert(END,'Pin Code:')
        lb2.insert(END,pin[0][0])

        cur.execute('select address from PHONE_DETAILS where contactID=?',(c[0][0],))
        add=cur.fetchall()
        lb2.insert(END,'Address:')
        lb2.insert(END,add[0][0])

        cur.execute('select website from PHONE_DETAILS where contactID=?',(c[0][0],))
        web=cur.fetchall()
        lb2.insert(END,'Website URL:')
        lb2.insert(END,web[0][0])

        cur.execute('select DOB from PHONE_DETAILS where contactID=?',(c[0][0],))
        d=cur.fetchall()
        lb2.insert(END,'Date of Birth:')
        lb2.insert(END,d[0][0])
        lb2.insert(END,'phone details.......')

        cur.execute('select contact_type from PHONE_TYPE_DETAILS where contactID=?',(c[0][0],))
        pt=cur.fetchall()
        if pt==0:
            lb2.insert(END,'Office:')
            
        elif pt==1:
            lb2.insert(END,'Home:')
        elif pt==2:
            lb2.insert(END,'Mobile:')

    
        
        cur.execute('select phone_no from PHONE_TYPE_DETAILS where contactID=?',(c[0][0],))
        pn=cur.fetchall()
        
        lb2.insert(END,pn[0][0])

        cur.execute('select email_id from MAIL_DETAILS where contactID=?',(c[0][0],))
        mail=cur.fetchall()
        
        lb2.insert(END,mail[0][0])

        

        
        
        
        
    Button(root1,text='select',command=selfun).grid(row=3,column=0)
    Button(root1,text='close',command=closeroot1).grid(row=3,column=1)
    root1.mainloop()
def clearall():
    cur.execute('delete from PHONE_DETAILS where contactID>=1')
    cur.fetchall()
    
Button(root,text='save',command=fnamefun).grid(row=14,column=0)
#-----------to check--------------#cur=con.cursor*
#cur.execute('select * from PHONE_DETAILS')
#print cur.fetchall()
#cur.execute('select * from PHONE_TYPE_DETAILS')
#print cur.fetchall()
#cur.execute('select * from MAIL_DETAILS')
#print cur.fetchall()
Button(root,text='search',command=searchfun).grid(row=14,column=1)
Button(root,text='close',command=closefun).grid(row=14,column=2)
Button(root,text='edit',command=clearall).grid(row=14,column=3)
root.mainloop()
