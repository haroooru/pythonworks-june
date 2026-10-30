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
