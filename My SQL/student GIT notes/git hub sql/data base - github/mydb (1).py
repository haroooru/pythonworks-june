from idlelib import query

import mysql.connector
from unicodedata import category

# # or from mysql import connector (This can also to be used for calling.)
# con=mysql.connector.connect(user="root",password="root",host="localhost")
# # establish connection between python code and mysql server
# # it returns a connection object
# c=con.cursor() # used to execute sql queries/commands
# c.execute("create database school_db")
# print("Database File executed")
#
# con=mysql.connector.connect(user="root",password="root",host="localhost",database="school_db")
# c=con.cursor()
# c.execute('''
# create table student(roll_no int not null primary key,
# name varchar(20),
# age int,
# place varchar(20),
# phone varchar(20),
# total_mark int)''')
# print("table created successfully")
# c.execute('''
# insert into student(roll_no,name,age,place,phone,total_mark)
# values(101,"arun",11,'ekm','734398929',145),
# (102,"amal",12,'ekm','7343458929',140),
# (103,"anu",12,'tcr','8922322345',147),
# (104,"hari",11,'ekm','734398929',144),
# (105,"manu",11,'ekm','8328433423',141)
# ''');
# query="insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)"
# data=(106,"kiran",12,"ekm","54934343",140)
# c.execute(query,data)
# con.commit() # to save data permanently inside_db
# print("Data Inserted")
# query="select * from student"
# c.execute(query)
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("No Records")
# number=input("Enter the Roll Number:")
# query ="select * from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
# record=c.fetchall()
# if record:
#     print(record)
# else:
#     print("No record")
# update the record
# number=input("Enter the Roll Number:")
# new_marks=input("Enter the New Marks: ")
# query ="update student set total_mark=%s where roll_no=%s"
# data=(new_marks,number)
# c.execute(query,data)
# con.commit()
# print("Marks updated")

#delete the record
# number=input("Enter the Roll Number:")
# query ="delete from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
# con.commit()
# print("Deleted")

# Create A new Record using values entered by user
# c.execute('''
# create table student(roll_no int not null primary key,
# name varchar(20),
# age int,
# place varchar(20),
# phone varchar(20),
# total_mark int)''')
# number=int(input("Enter the Roll Number: "))
# name=input("Enter the Name: ")
# age=int(input("Enter the Age: "))
# place=input("Enter the Place: ")
# phone=input("Enter the Phone Number: ")
# total_mark=int(input("Enter the Mark: "))
# query="insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)"
# data=(number,name,age,place,phone,total_mark)
# c.execute(query,data)
# con.commit()
# print("Values Added")
# Create a database named shop
#
# Create a table `Product` with the following fields:
#
#  `product_id` – Primary Key
#  `name`
#  `brand`
#  `category`
#  `price`
#  `stock`
#
# Write a menu-driven Python program using MySQL with the following options:
#
# text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit
# con=mysql.connector.connect(user="root",password="root",host="localhost")
# c=con.cursor() # used to execute sql queries/commands
# c.execute("create database shop")
# print("Database File executed")
con=mysql.connector.connect(user="root",password="root",host="localhost",database="shop")
c=con.cursor()
# c.execute('''
# create table product(product_id int not null primary key,
# name varchar(20),
# brand varchar(20),
# category varchar(20),
# price int,
# stock int)''')
# print("table created successfully")
def insert():
    query = "insert into product(product_id,name,brand,category,price,stock)values(%s,%s,%s,%s,%s,%s)"
    data=(product_id,name,brand,category,price,stock)
    c.execute(query,data)
    con.commit()
    print("Values Added")
def get():
    query="select * from product"
    c.execute(query)
    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("No Records Foud")
def search():
    query="select * from product where product_id=%s"
    data=(product_id,)
    c.execute(query,data)
    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("No Records Found")
def update():
    query="update product set stock=%s where product_id=%s"
    data=(new_stock,product_id)
    c.execute(query,data)
    print("Stock Updated")
    con.commit()
def delete():
    query="delete from product where product_id=%s"
    data=(product_id,)
    c.execute(query,data)
    print("Product Deleted")
    con.commit()
while(1):
        print("Menu Driven")
        print(" 1. Insert Product details")
        print("2. Read all Product details")
        print("3. Search a Product by product_id")
        print("4. Update the stock of a Product")
        print("5. Delete a Product record")
        print(" 6. Exit")
        ch=int(input("Enter the Choice: "))
        if ch==1:
            product_id = int(input("Enter the Product Id: "))
            name=input("Enter the Name: ")
            brand=(input("Enter the Brand: "))
            category=input("Enter the Category: ")
            price=int(input("Enter the Price: "))
            stock=int(input("Enter the Stock: "))
            insert()
        if ch==2:
            get()
        if ch==3:
            product_id=int(input("Enter the Product Id: "))
            search()
        if ch==4:
            product_id = int(input("Enter the Product Id: "))
            new_stock=int(input("Enter the New Stock: "))
            update()
        if ch==5:
            product_id=int(input("Enter the Product id: "))
            delete()
        if ch==6:
            exit()