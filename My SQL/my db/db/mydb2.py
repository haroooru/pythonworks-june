import sqlite3

# Connect to database (creates file if not exists)
con = sqlite3.connect("company.db")

# Create table
# con.execute("create table if not exists person (id int primary key, name varchar(30), age int)")
# print("Table created")

# Insert a record
# con.execute("insert into person(id, name, age) values(1, 'arun', 23)")
# con.commit()
# print("Record inserted")

# Verify
# e = con.execute("select * from person")
# print(e.fetchall())

#
# i =int(input("enter id"))
# n = input("enter name")
# a = int(input("enter age"))
#
#
# con.execute('insert into person (id,name,age) values(?,?,?)',(i,n,a))
# con.commit()

#read operations

i =int(input("enter id"))

e=con.execute( 'select * from person where id=?' , (i,))
print(e.fetchall())
