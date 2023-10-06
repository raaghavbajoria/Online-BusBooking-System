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
Label(frame1,text="Add Bus Route Details",font="Arial 18 bold",fg='green').grid(row=2,column=0,pady=20)
Label(root,text="Route ID",font="Arial 11 bold").grid(row=3,column=0,padx=20)
rid=Entry(root,font="Arial 11 bold")
rid.grid(row=3,column=1)
Label(root,text="Station Name",font="Arial 11 bold").grid(row=3,column=2,padx=10)
name=Entry(root,font="Arial 11 bold")
name.grid(row=3,column=3)
Label(root,text="Station ID",font="Arial 11 bold").grid(row=3,column=4,padx=10)
sid=Entry(root,font="Arial 11 bold")
sid.grid(row=3,column=5)
def add():
    if(len(rid.get())==0 or len(name.get())==0 or len(sid.get())==0):
        showerror('Value Missing','Enter values')
    else:
        conn=mysql.connector.connect(host='localhost',user='root',password='Raghav@2001',database='project')
        cur=conn.cursor()
        cur.execute("""insert into route(route_id,station_id,station_name)values("{}","{}","{}")""".format(rid.get(),sid.get(),name.get()))
        conn.commit()
        conn.close()
Button(root,text="Add Route",font='Arial 14 bold',bg='light green',command=add).grid(row=3,column=6,pady=20)
Button(root,text="Delete Route",font='Arial 14 bold',bg='light green',fg='red').grid(row=3,column=7,pady=20)
Button(root,image=img1).grid(row=3,column=8,pady=20)



root.mainloop()