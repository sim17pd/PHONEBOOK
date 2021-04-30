from Tkinter import*
root=Tk()

Label(root,text='Project Title : PhoneBook',font="bold").grid(row=0,column=0)
Label(root,text='Project of Python and Database',font="none 16 bold").grid(row=1,column=1)
Label(root,text='Developed By : SIMPLE PRASAD',fg="blue",font="none 13 bold").grid(row=2,column=1)
Label(root,text='make mouse movement over this screen to close',font="none 10",fg="red").grid(row=3,column=1)
root.geometry('650x350')

def close(e=1):
    root.destroy()
root.bind('<Motion>',close)
#Button(root,text='close',command=close).pack()
root.mainloop()
