from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
img1=PhotoImage(file='.\\home.png')
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=10)
def nextpage(e=1):
    root.destroy()
    import page2
Label(frame1,image=img).grid(row=0,column=0,padx=w/2.5)
Label(frame1,text="Online Bus Booking System",font="Arial 20 bold",bg='light blue',fg='red').grid(row=1,column=0)
Label(frame1,text="Add Bus Operator Details",font="Arial 18 bold",fg='green').grid(row=2,column=0,pady=20)
Label(root,text="Operator id",font="Arial 14 bold").grid(row=3,column=0,pady=20)
oid=Entry(root,font="Arial 14 bold")
oid.grid(row=3,column=1,pady=20,sticky=W)
Label(root,text="Name",font="Arial 14 bold").grid(row=3,column=2,pady=20)
name=Entry(root,font="Arial 14 bold")
name.grid(row=3,column=3,pady=20,sticky=W)
Label(root,text="Address",font="Arial 14 bold").grid(row=3,column=4,pady=20)
address=Entry(root,font="Arial 14 bold")
address.grid(row=3,column=5,pady=20,sticky=W)
Label(root,text="Phone",font="Arial 14 bold").grid(row=3,column=6,pady=20)
phone=Entry(root,font="Arial 14 bold")
phone.grid(row=3,column=7,pady=20,sticky=W)
Label(root,text="Email",font="Arial 14 bold").grid(row=3,column=8,pady=20)
email=Entry(root,font="Arial 14 bold")
email.grid(row=3,column=9,pady=20,sticky=W)

Button(root,text="Edit",font='Arial 14 bold',bg='green').grid(row=4,column=8)
Button(root,image=img1,command=nextpage).grid(row=4,column=9)
def add():
    if len(oid.get())==0 or len(name.get())==0 or len(address.get())==0 or len(phone.get())==0 or len(email.get())==0:
        showerror('Value Missing','Enter values')
    else:
        conn=mysql.connector.connect(host='localhost',user='root',password='Raghav@2001',database='project')
        cur=conn.cursor()
        cur.execute("""insert into bus_operator(op_id,oname,address,phone,email)values("{}","{}","{}","{}","{}")""".format(oid.get(),name.get(),address.get(),phone.get(),email.get()))
        conn.commit()
        conn.close()
Button(root,text="Add",font='Arial 14 bold',bg='green',command=add).grid(row=4,column=7)    
root.mainloop()