from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
img1=PhotoImage(file='.\\home.png')
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=13)
Label(frame1,image=img).grid(row=0,column=0,padx=w/2.5)
Label(frame1,text="Online Bus Booking System",font="Arial 20 bold",bg='light blue',fg='red').grid(row=1,column=0)
Label(frame1,text="Add Bus Running Details",font="Arial 18 bold",fg='green').grid(row=2,column=0,pady=20)
Label(root,text="Bus ID",font="Arial 11 bold").grid(row=3,column=0,padx=20)
bid=Entry(root,font="Arial 11 bold")
bid.grid(row=3,column=1)
Label(root,text="Running Date",font="Arial 11 bold").grid(row=3,column=2,padx=10)
run=Entry(root,font="Arial 11 bold")
run.grid(row=3,column=3)
Label(root,text="Seat Available",font="Arial 11 bold").grid(row=3,column=4,padx=10)
seat=Entry(root,font="Arial 11 bold")
seat.grid(row=3,column=5)
def add():
    if len(bid.get())==0 or len(run.get())==0 or len(seat.get())==0:
        showerror('Value Missing','Enter values')
    else:
        conn=mysql.connector.connect(host='localhost',user='root',password='Raghav@2001',database='project')
        cur=conn.cursor()
        cur.execute("""insert into running_details(bus_id,running_date,seat_available)values("{}","{}","{}")""".format(bid.get(),run.get(),seat.get()))
        conn.commit()
        conn.close()

Button(root,text="Add Run",font='Arial 14 bold',bg='light green',command=add).grid(row=3,column=6,pady=20)
Button(root,text="Delete Run",font='Arial 14 bold',bg='light green').grid(row=3,column=7,pady=20)
Button(root,image=img1).grid(row=3,column=8,pady=20)



root.mainloop()