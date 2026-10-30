# mysql
# mysql - connect - python
#
# mysql.connect()
#
# parameters - user password host
#
import mysql.connector


con = mysql.connector.connect(user = "root", password ="root", host ="localhost")

c=con.cursor()

con = mysql.connector.connect(user = "root", password ="root", host ="localhost",database = "mydb2")

c=con.cursor()

c.execute('create table if not exists employee(empid int primary key, name varchar(30),age int, salary int, gender varchar(20),place varchar(20)')









import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="mydb2"
)

c = con.cursor()

# Correct CREATE TABLE with closing parenthesis
# c.execute('create table if not exists employee(empid int primary key, name varchar(30), age int, salary int, gender varchar(20), place varchar(20))')
# print("Table created")
#
# c.execute("""
# insert into employee (empid, name, age, salary, gender, place) values
# (101, 'Arun', 23, 20000, 'Male', 'Ekm'),
# (102, 'Anu', 24, 25000, 'Female', 'Thrissur'),
# (103, 'Dev', 26, 30000, 'Male', 'TVM'),
# (104, 'Meera', 22, 22000, 'Female', 'Kochi'),
# (105, 'Ajay', 30, 40000, 'Male', 'Calicut')
# """)
#
# con.commit()
# c.close()
# con.close()

c.execute('select * from employee')
k=c.fetchall()
print(k)
c.execute('select * from employee where empid = 101')
k=c.fetchall()
print(k)


c.execute('select name,age from employee where empid = 101')
k=c.fetchall()
print(k)


# Create a database file school.db
import sqlite3

con = mysql.connector.connect(host="localhost",user="root",password="root")
c = con.cursor()

c.execute("create database if not exists school")

con = mysql.connector.connect(host="localhost",user="root",password="root")
c = con.cursor()
# create a table Student with fields roll_no(pk),name,age,gender,course,mark


c.execute("""create table if not exists Student(roll_no int primary key,name varchar(20),age int,
                gender varchar(20),course varchar(20),mark int)""")

# write a menu driven code
#
#                     1.Insert Student details
#                     2.Read all student details
#                     3.search a student by rollno
#                     4.update the mark of a student
#                     5.Delete a student record
#                     6.Exit

def insert_record():
    r = int(input("Enter Roll No: "))
    n = input("Enter Name: ")
    a = int(input("Enter Age: "))
    g = input("Enter Gender: ")
    crs = input("Enter Course: ")
    m = int(input("Enter Mark: "))
    c.execute("insert into Student values(%s,%s,%s,%s,%s,%s)", (r, n, a, g, crs, m))
    con.commit()
    print("Record inserted")

def read_all():
    c.execute("select * from Student")
    for row in c.fetchall():
        print(row)

def search_record():
    r = int(input("Enter Roll No to search: "))
    c.execute("select * from Student where roll_no=%s", (r,))
    row = c.fetchone()
    if row:
        print(row)
    else:
        print("Student not found")

def update_record():
    r = int(input("Enter Roll No to update: "))
    newmark = int(input("Enter new mark: "))
    c.execute("update Student set mark=%s where roll_no=%s", (newmark, r))
    con.commit()
    print("Mark updated")

def delete_record():
    r = int(input("Enter Roll No to delete: "))
    c.execute("delete from Student where roll_no=%s", (r,))
    con.commit()
    print("Record deleted")

while True:
    print("\nMenu")
    print("1. Insert Student details")
    print("2. Read all student details")
    print("3. Search a student by rollno")
    print("4. Update the mark of a student")
    print("5. Delete a student record")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        insert_record()
    elif ch == 2:
        read_all()
    elif ch == 3:
        search_record()
    elif ch == 4:
        update_record()
    elif ch == 5:
        delete_record()
    elif ch == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")

con.close()