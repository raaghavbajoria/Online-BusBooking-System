from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
img1=PhotoImage(file='.\\home.png')
#frame1=Frame(root)
#frame1.grid(row=0,column=0,columnspan=10)
Label(root,image=img).grid(row=0,column=0,padx=w/2.5,columnspan=15)
Label(root,text="Online Bus Booking System",font="Arial 26 bold",bg='light blue',fg='red').grid(row=1,column=0,columnspan=15)
Label(root,text="Add New Details To DataBase",font="Arial 18 bold",bg='light green',fg='green').grid(row=2,column=0,pady=20,columnspan=15)
def nextpage(e=1):
    root.destroy()
    import page5
def nextpage1(e=1):
    root.destroy()
    import page6
def nextpage2(e=1):
    root.destroy()
    import page7
def nextpage3(e=1):
    root.destroy()
    import page8
Button(root,text="New Operator",font='Arial 15 bold',bg='light green',command=nextpage).grid(row=3,column=3)
Button(root,text="New Bus",font='Arial 15 bold',bg='orange',command=nextpage1).grid(row=3,column=6)
Button(root,text="New Route",font='Arial 15 bold',bg='light blue',command=nextpage2).grid(row=3,column=9)
Button(root,text="New Run",font='Arial 15 bold',bg='pink',command=nextpage3).grid(row=3,column=12)


root.mainloop()