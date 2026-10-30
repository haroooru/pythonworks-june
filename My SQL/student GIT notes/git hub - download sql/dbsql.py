# import sqlite3
#
# con = sqlite3.connect("company.db")
# command = """create table employee(empid int primary key,
#                                   name varchar(30),
#                                   age int, place varchar(30),
#                                   gender varchar(30),
#                                   salary int)"""

import sqlite3
con=sqlite3.connect('company.db')


command="""create table employee(empid int primary key,
                name varchar(30),
                age int,
                place varchar(30),
                gender varchar(10),
                designation varchar(30),
                salary int)"""

#Primary key field used to identify a particular record
#it must be unique/no duplicate value

con.execute(command)
print("Table created")
