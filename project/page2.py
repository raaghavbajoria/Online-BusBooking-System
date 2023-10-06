from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=10)
Label(frame1,image=img).grid(row=0,column=0,padx=w/2.5)
Label(frame1,text="Online Bus Booking System",font="Arial 20 bold",bg='light blue',fg='red').grid(row=1,column=0)
def nextpage(e=1):
    root.destroy()
    import page3
def nextpage1(e=1):
    root.destroy()
    import check_your_boolikg
def nextpage2(e=1):
    root.destroy()
    import page4

Button(root,text="Seat Booking",font='Arial 18 bold',bg='light green',command=nextpage).grid(row=2,column=0,pady=h//10,padx=w/7)
Button(root,text="Check Booked Seat",font='Arial 18 bold',bg='green',command=nextpage1).grid(row=2,column=1,pady=h/10)
Button(root,text="Add bus Details",font='Arial 18 bold',bg='dark green',command=nextpage2).grid(row=2,column=2,pady=h/10,padx=150)
Label(root,text="For Admin Only",font='Arial 14 bold',fg='red').grid(row=3,column=2)
def nextpage(e=1):
    root.destroy()
    import page2

root.mainloop()
