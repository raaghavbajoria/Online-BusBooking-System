from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

def info2():
    if len(name.get())==0 or len(no.get())==0 or len(mobile.get())==0 or len(age.get())==0:
        showerror('Value Missing','Enter Details')
    elif len(mobile.get())!=10:
        showerror('Wrong Inpit','Enter Valid Mobile No.')
    elif int(age.get())>100:
        showerror('Wrong Inpit','Enter Valid Age')
    else:
        # cur.execute(""" insert into booking_history(mobile,pname, gender,age,no_of_seats,dob,bfrom,dot,bname,fare,bto) values({},"{}","{}",{},{},current_date,"{}","{}","{}",{},"{}")""".format(int(mobile.get()),name.get(),gender.get(),int(age.get()),int(no.get()),From.get(),journey.get(),res[0][0],res[0][4],to.get()))
        book_ticket()
def book_ticket():
    conn=mysql.connector.connect(host='localhost',user='root',password='Raghav@2001',database='project')
    cur=conn.cursor()
    cur.execute('select sum(no_of_seats) from passenger where tdate="{}"'.format(date.get()))
    q=cur.fetchall()
    x=int(q[0][0])
    cur.execute(""" select O.oname,B.bus_type,R.seat_available,B.capacity,B.fare,B.bus_id from bus_operator as O,bus as B, running_details as R, route as F, route as T where F.station_name="{}" and T.station_name="{}" and F.route_id=T.route_id and F.station_id<T.station_id and R.running_date="{}" and B.route_id=T.route_id and o.op_id=b.op_id""".format(fr.get(),to.get(),date.get()))
    r=cur.fetchall()
    avb=int(r[0][3])-x
    if len(name.get())==0 or len(no.get())==0 or len(mobile.get())==0 or len(age.get())==0 :
        showerror("Value missing","Enter Values")
    elif len(mobile.get())!=10:
        showerror('Wrong Inpit','Enter Valid Mobile No.')
    elif int(age.get())>100:
        showerror('Wrong Inpit','Enter Valid Age')
    elif int(no.get())>int(r[0][3]):
        showerror('Error','Seats are Limited!')
    elif int(no.get())>avb:
        showerror('Error','Seats are Limited!')

    else:
        result=askquestion('Ticket Confirmation','Do You want to confirm your ticket?')
        if result=='yes':
            
            a=r[0][4]
            b=r[0][5]
            cur.execute('insert into passenger(pname,gender,no_of_seats,mob_no,age,source,destination,bdate,tdate,fare,bus_id) values("{}","{}",{},{},{},"{}","{}",current_date(),"{}",{},{})'.format(name.get(),gender.get(),no.get(),mobile.get(),age.get(),fr.get(),to.get(),date.get(),a,b))
            conn.commit()
            conn.close()
            root.destroy()
            import bus_ticket

def info():
    if len(to.get())==0:
        showerror('Value Missing','Enter Destination')
    elif len(fr.get())==0:
        showerror('Value Missing','Enter Starting Point')
    elif len(date.get())==0:
        showerror('Value Missing','Enter date')
    else:
        Label(root,text="Select Bus",font="Arial 14 bold",fg="green").grid(row=5,column=0)
        Label(root,text="Operator",font="Arial 12 bold",fg="green").grid(row=5,column=1)
        Label(root,text="Bus Type",font="Arial 12 bold",fg="green").grid(row=5,column=2)
        Label(root,text="Available",font="Arial 12 bold",fg="green").grid(row=5,column=3)
        Label(root,text="Capacity",font="Arial 12 bold",fg="green").grid(row=5,column=4)
        Label(root,text="Fare",font="Arial 12 bold",fg="green").grid(row=5,column=5)
        bus_select=IntVar()
        Radiobutton(root,text='Select Bus',variable=bus_select,value=1).grid(row=6,column=0)
        Button(root,text="Proceed To Book",command=info1,font='Arial 14 bold',bg='light green').grid(row=6,column=7)
        conn=mysql.connector.connect(host='localhost',user='root',password='Raghav@2001',database='project')
        cur=conn.cursor()
        cur.execute("""select O.oname,B.bus_type,R.seat_available,B.capacity,B.fare from bus_operator as O,bus as B, running_details as R, route as F, route as T where F.station_name="{}" and T.station_name="{}" and F.route_id=T.route_id and F.station_id<T.station_id and R.running_date="{}" and B.route_id=T.route_id and o.op_id=b.op_id""".format(fr.get(),to.get(),date.get()))
        res=cur.fetchall()
        cur.execute('select sum(no_of_seats) from passenger where tdate="{}"'.format(date.get()))
        q=cur.fetchall()
        x=int(q[0][0])
        avb=int(res[0][3])-x
        if(avb<1):
            showerror('No Seats Available','Bus Full')
        else:
            Label(root,text=res[0][0]).grid(row=6,column=1)
            Label(root,text=res[0][1]).grid(row=6,column=2)
            Label(root,text=avb).grid(row=6,column=3)
            Label(root,text=res[0][3]).grid(row=6,column=4)
            Label(root,text=res[0][4]).grid(row=6,column=5)
            conn.commit()
            conn.close()


def info1():
    
    Label(root,text='Fill Passenger Details to book the bus ticket',font='Arial 20 bold',bg='light blue',fg='red').grid(row=7,column=0,pady=20,columnspan=10)
    Label(root,text="Name",font="Arial 8 bold").grid(row=8,column=0)
    #name=Entry(root,font="Arial 8")
    name.grid(row=8,column=1,sticky=W)
    Label(root,text="Gender",font="Arial 8 bold").grid(row=8,column=2)
    #gender=StringVar()
    option=['Male','Female','Third Gender']
    gender.set('Male')
    d_menue=OptionMenu(root,gender,*option)
    d_menue.grid(row=8,column=3,sticky=W)
    Label(root,text="No of Seats",font="Arial 8 bold").grid(row=8,column=4,sticky=W)
    #no=Entry(root,font="Arial 8")
    no.grid(row=8,column=5,sticky=W)
    Label(root,text="Mobile No",font="Arial 8 bold").grid(row=8,column=6,sticky=W)
    #mobile=Entry(root,font="Arial 8")
    mobile.grid(row=8,column=7,sticky=W)
    Label(root,text="Age",font="Arial 8 bold").grid(row=8,column=8)
    #age=Entry(root,font="Arial 8")
    age.grid(row=8,column=9,sticky=W)
    
    Button(root,text="Book Seat",font='Arial 8 bold',bg='light green',command=info2).grid(row=9,column=9)
    #conn=sqlite3.Connection('database.db')
    #cur=conn.cursor()
    #cur.execute("insert into passenger values()")
img=PhotoImage(file='.\\Bus_for_project.png')
img1=PhotoImage(file='.\\home.png')
frame1=Frame(root)
frame1.grid(row=0,column=0,columnspan=10)
Label(frame1,image=img).grid(row=0,column=0,padx=w/2.5)
Label(frame1,text="Online Bus Booking System",font="Arial 20 bold",bg='light blue',fg='red').grid(row=1,column=0)
Label(frame1,text="Enter Journey Details",font="Arial 15 bold",bg='light green',fg='green').grid(row=2,column=0,pady=20)
Label(root,text="To",font="Arial 14 bold").grid(row=3,column=0,pady=20)
to=Entry(root,font="Arial 14 bold")
to.grid(row=3,column=1,pady=20,sticky=W)
Label(root,text="From",font="Arial 14 bold").grid(row=3,column=2,pady=20)
fr=Entry(root,font="Arial 14 bold")
fr.grid(row=3,column=3,pady=20,sticky=W)
Label(root,text="Journey Date",font="Arial 14 bold").grid(row=3,column=4,pady=20)
date=Entry(root,font="Arial 14 bold")
date.grid(row=3,column=5,pady=20,sticky=W)
Button(root,text="Show Bus",command= info ,font='Arial 14 bold',bg='green').grid(row=3,column=6)
Button(root,image=img1).grid(row=3,column=7)
name=Entry(root,font="Arial 8")
no=Entry(root,font="Arial 8")
mobile=Entry(root,font="Arial 8")
age=Entry(root,font="Arial 8")
gender=StringVar()

root.mainloop()
