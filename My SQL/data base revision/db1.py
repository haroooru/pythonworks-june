# database
# organised collection of related data so that it can be easily stored retrieved updated or deleted
#
#
# DBMS - database management system - data management software - mysql sqlite postgress
#
# set of programs that helps to create update or delete from db/
# is an interface bw user/apllication and database
#
# CRED - DB operation - create read update delete
#
# Relational Database - data is organised as tables - rows and columns
#
# SQL - structured quiere language - programming language used to interact with relational db
#
# SQL quireis / commands - ?
#
#                             sql commands / quires
# python code / application ----------------------------> sqlite db
#
# no interface no installation integrated db
#
#
# DB browser - ?

import sqlite3


con = sqlite3.connect('company_revision.db')  #create or open if exists

# create table - SQL commands
#
# command = """create table tablename ( field type, field type,......)"""


con.execute("DROP TABLE IF EXISTS employee_rev")
#
command = """create table if not exists employee_rev
(empid int primary key, name varchar(30),age int, place varchar(30),
gender varchar(10),salary int)"""
#
con.execute(command)

#
# #now after creating table commend it

#INSERT Command/ Create New Record

#command = """ Insert into tablename(field, field,...)values(val1,val2,....)"""

# insert one record
employees = [
    (101,'miya',24,'kochi','f',30000),

    (102,'liam',21,'tvm','m',25000),

    (103,'hari',23,'kochi','f',50000),

    (104,'anand',25,'karur','m',200000)
             ]


command = """insert into employee_rev (empid,name,age,place,gender,salary)values(?,?,?,?,?,?)"""
con.executemany(command,employees)
con.commit()
print("Record inserted")

# or

command= """
insert into employee_rev (empid,name,age,place,gender,salary)
            values (105,'willson', 30 , 'pkd' , 'm' , 60000),
                    (106,'siya', 21 , 'kochi' , 'f', 20000)"""

con.execute(command)
con.commit()
print("Record inserted")



# read operations

#command = select attributes from tablename where condition

command = """select * from employee_rev"""
e = con.execute(command) #e is cursor
print(e.fetchall())












