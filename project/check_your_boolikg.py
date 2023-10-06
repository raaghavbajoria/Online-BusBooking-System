from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
def ticket_box():
    if len(mobile.get())==0:
        showerror('Value Missing','Enter Mobile No.')
    elif len(mobile.get())!=10 :
        showerror('Invalid Value','Enter a valid Mobile No.')
    else:
        conn=mysql.connector.connect(host='localhost',user='root',password='Raghav@2001',database='project')
        cur=conn.cursor()
        cur.execute('select passenger_id,pname,gender,no_of_seats,mob_no,age,source,destination,bdate,tdate,fare,bus_id from passenger where mob_no = {}'.format(mobile.get()))
        res=cur.fetchall()
        final=LabelFrame(root)
        final.grid(row=8,column=5,columnspan=3)
        Label(final, text='Passenger: {}'.format(res[0][1]),font='Arial 10 bold').grid(row=8,column=0)
        Label(final, text='No of Seats: {}'.format(res[0][3]),font='Arial 10 bold').grid(row=9,column=0)
        Label(final, text='Age: {}'.format(res[0][5]),font='Arial 10 bold').grid(row=10,column=0)
        Label(final, text='Booking Ref.: {}'.format(res[0][0]),font='Arial 10 bold').grid(row=11,column=0)
        Label(final, text='Travels on: {}'.format(res[0][9]),font='Arial 10 bold').grid(row=12,column=0)
        Label(final, text='Gender: {}'.format(res[0][2]),font='Arial 10 bold').grid(row=8,column=1)
        Label(final, text='Phone: {}'.format(res[0][4]),font='Arial 10 bold').grid(row=9,column=1)
        Label(final, text='Fare Rs: {}'.format(int(res[0][10])*int(res[0][3])),font='Arial 10 bold').grid(row=10,column=1)
        Label(final, text='Booked On: {}'.format(res[0][8]),font='Arial 10 bold').grid(row=11,column=1)
        Label(final, text='Boarding Point: {}'.format(res[0][6]),font='Arial 10 bold').grid(row=12,column=1)
        Label(final, text='Total amount Rs{} to be paid at the time of boarding he bus: '.format(int(res[0][10])*int(res[0][3])),fg='grey').grid(row=14,column=0,columnspan=2)

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,padx=w//2.5,columnspan=15)
Label(root,text="Online Bus Booking System",font="Arial 25 bold",fg="red",bg='light blue').grid(row=2,column=0,padx=w//2.5,columnspan=15)
Label(root,text="Check Your Booking",font="Arial 15 bold",fg="green",bg="light green").grid(row=3,column=0,pady=30,columnspan=15)
Label(root,text="Enter Your Mobile No:",font="Arial 12 bold").grid(row=4,column=6)
mobile=Entry(root)
Button(root,text="Check booking",font="Arial 12 bold",command=ticket_box).grid(row=4,column=8,pady=50)
mobile.grid(row=4,column=7)
box=Frame(root,relief='groove',bd=3)
box.grid(row=8,column=6,columnspan=4)
root.mainloop()
