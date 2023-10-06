from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,padx=w/2.5)
Label(root,text="Online Bus Booking System",font="Arial 20 bold",bg='light blue',fg='red').grid(row=1,column=0)
Label(root,text="Name : Raghav Bajoria",font="Arial 14 bold",fg='Blue').grid(row=2,column=0,pady=h/30)
Label(root,text="Er : 211B235",font="Arial 14 bold",fg='Blue').grid(row=3,column=0,pady=h/50)
Label(root,text="Mobile No. : 9696131488",font="Arial 14 bold",fg='Blue').grid(row=4,column=0,pady=h/50)
Label(root,text="Submitted To : Dr. Mahesh Kumar",font="Arial 18 bold",bg='light blue',fg='red').grid(row=5,column=0,pady=h/20)
Label(root,text="Project Based Learning",font="Arial 14 bold",fg='red').grid(row=6,column=0)
def nextpage(e=1):
    root.destroy()
    import page2
root.bind('<KeyPress>',nextpage)
root.mainloop()
