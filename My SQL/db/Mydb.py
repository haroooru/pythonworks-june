
import sqlite3
con=sqlite3.connect('company.db')


# command="""create table employee1(empid int primary key,
#                 name varchar(30),
#                 age int,
#                 place varchar(30),
#                 gender varchar(10),
#                 designation varchar(30),
#                 salary int)"""
#
# #Primary key field used to identify a particular record
# #it must be unique/no duplicate value
#
# con.execute(command)
# print("Table created")


# command="""insert into employee1(empid ,name,age,place,gender,designation,salary)values(100,"Joyal",21,"Trivandrum","Male","Developer",50000)
# ,(101,"Angelina",16,"Trivandrum","Female","Artist",500000)"""
# con.execute(command)
# con.commit()
# print("Record inserted")
# con.close()

# command = "select * from employee1"
# e = con.execute(command)
# print(e.fetchall())


e=con.execute("select name, age from employee1")
print(e.fetchall())

e=con.execute("select name, age from employee1 where empid=101")
print(e.fetchall())

e=con.execute("select * from employee1 where age >= 20 and salary>=1000")
print(e.fetchall())
#
# e=con.execute("select * from employee1 where place = "ekm" or age <= 25")
# print(e.fetchall()) wronggg

e = con.execute("select * from employee1 where place = 'ekm' or age <= 25")
print(e.fetchall())

e = con.execute("select * from employee1 where salary between 2000 and 300000")
print(e.fetchall())


e = con.execute("select name from employee1 where salary between 2000 and 300000")
print(e.fetchall())

#Like
e = con.execute("select * from employee1 where name like 'A%'")
print(e.fetchall())

e = con.execute("select * from employee1 where name like 'J____'")
print(e.fetchall())

e = con.execute("select * from employee1 where name like 'J%'")
print(e.fetchall())

e = con.execute("select * from employee1 where name like '____l'")
print(e.fetchall())

# e = con.execute("select * from employee1 where age <25 and name 'A%'")
# print(e.fetchall()) wrongg

e = con.execute("select * from employee1 where age < 25 and name like 'A%'")
print(e.fetchall())


e = con.execute("select * from employee1 where age < 25 and place like 'T_______'")
print(e.fetchall())

e = con.execute("select * from employee1 where age in (21,25,16)")
print(e.fetchall())

#order by

e = con.execute("select * from employee1 order by age")
print(e.fetchall())

e = con.execute("select * from employee1 order by name desc")
print(e.fetchall())


e = con.execute("select distinct(place) from employee1 ")
print(e.fetchall())

#update

con.execute('update employee1 set name ="hari", age=24 where empid =101 ')
con.commit()

#delete
con.execute('delete from employee1 where empid=103')
con.commit()

# # Insert new rows
# con.execute("insert into employee1(empid, name, age, place, gender, designation, salary) values(104, 'Meera', 22, 'Kochi', 'Female', 'Designer', 45000)")
# con.execute("insert into employee1(empid, name, age, place, gender, designation, salary) values(105, 'Arjun', 28, 'Thrissur', 'Male', 'Manager', 60000)")
# con.execute("insert into employee1(empid, name, age, place, gender, designation, salary) values(106, 'Divya', 25, 'TVM', 'Female', 'Tester', 35000)")
# con.commit()

