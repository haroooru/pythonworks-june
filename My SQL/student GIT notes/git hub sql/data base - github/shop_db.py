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
import mysql.connector
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
    query="update product set stock=%s"
    data=(new_stock,product_id)
    c.execute(query,data)
    print("Stock Updated")
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
