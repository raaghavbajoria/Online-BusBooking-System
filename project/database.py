import sqlite3
con = sqlite3.Connection('database.db')
cur = con.cursor()
cur.execute("create table passenger(passenger_id INTEGER PRIMARY KEY AUTOINCREMENT,pname varchar(50),gender varchar(20),no_of_seats int,mob_no numeric(20),age int ,source varchar(30),destination varchar(30),bdate date,tdate date,fare numeric(20),bus_id int)")
cur.execute("create table bus(bus_id int,bus_type varchar(30),capacity int ,fare int,op_id int, route_id int,primary key(bus_id))")
cur.execute("create table route(route_id int ,station_id int,station_name varchar(30),primary key(route_id,station_id))")
cur.execute("create table running_details(bus_id int,running_date date,seat_available int,primary key(bus_id,running_date))")
cur.execute("create table bus_operator(op_id int ,oname varchar(30),address varchar(30),email varchar(30),phone int,primary key(op_id))")

cur.execute('insert into bus_operator values(01,"Kamla","Jhansi","kamlatravel@gmail.com",884531259);')
cur.execute('insert into bus_operator values(02,"Hans","Kanpur","Hanstravel@gmail.com",963258741);')

cur.execute('insert into route values(31,1,"Guna");')
cur.execute('insert into route values(31,2,"Jaypee");')
cur.execute('insert into route values(31,3,"Binagarh")')
cur.execute('insert into route values(31,4,"Biaora");')
cur.execute('insert into route values(31,5,"Bhopal");')

cur.execute('insert into route values(32,1,"Bhopal");')
cur.execute('insert into route values(32,2,"Biaora");')
cur.execute('insert into route values(32,3,"Binagarh");')
cur.execute('insert into route values(32,4,"Jaypee");')
cur.execute('insert into route values(32,5,"Guna");')

cur.execute('insert into bus values(21,"AC 2x2",50,1000,01,31);')
cur.execute('insert into bus values(22,"2x2",60,800,02,32);')

cur.execute('insert into running_details values(21,"27/11/22",50);')
cur.execute('insert into running_details values(22,"28/11//22",60);')

con.commit()
con.close()