# define a class to perform database operations on book table
# create a class  named booklist createretriveupdatedelete and define methods
#list for reading all records
#create for creating a new record
#retrieve(id)-for reading a specific record
#update(id,data)-for updating a specific record
#for deleting a specific record
import mysql.connector

# class BookListCreateRetrieveUpdateDelete:
#     def __init__(self):
#         self.con=mysql.connector.connect(user="root",password="root",host="localhost",database="library_db")
#         self.c=self.con.cursor()
#         print("DataBase Connection Established")
#     def list(self):
#         query="select * from book"
#         self.c.execute(query)
#         records=self.c.fetchall()
#         if records:
#             for row in records:
#                 print(row)
#         else:
#             print("No Records Found")
#     def create(self,title,author,price,pages,language):
#         # self.title=input("Enter the Title of the Book: ")
#         # self.author=input("Enter the Author of the Book: ")
#         # self.price=int(input("Enter the Title of the Book: "))
#         # self.pages = int(input("Enter the Price of the Book: "))
#         # self.language = input("Enter the Language of the Book: ")
#         # query="insert into book (title,author,price,pages,language)values(%s,%s,%s,%s,%s)"
#         # data=(self.title,self.author,self.price,self.pages,self.language)
#         # self.c.execute(query,data)
#         # self.con.commit()
#         # query="insert into book (title,author,price,pages,language)values(%s,%s,%s,%s,%s)"
#         # data=(title,author,price,pages,language)
#         # self.c.execute(query,data)
#         # self.con.commit()
#         print("Data Inserted")
#     def retrieve(self,id):
#         query="select * from book where id=%s"
#         data=(id,)
#         self.c.execute(query,data)
#         records=self.c.fetchone()
#         if records:
#            print(records)
#         else:
#             print("No Records Found")
#     def update(self,id,title,author,price,pages,language):
#         query = "update  book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
#         data = (title, author, price, pages, language,id)
#         self.c.execute(query, data)
#         self.con.commit()
#     def delete (self,id):
#         query="delete from book where id=%s"
#         data=(id,)
#         self.c.execute(query,data)
#         self.con.commit()
#         if self.c.rowcount>0:
#             print("Data is Deleted")
#         else:
#             print("No Record Found")
# a= BookListCreateRetrieveUpdateDelete()
# # a.list()
# # a.create("Alchemist","arun",280,30,"malayalam")
# # a.retrieve(1)
# # a.delete(4)
# a.update(1,"alchemist","jhon",2000,28,"english")
# class called vehicle createretriveupdatedelete
# class BookListCreateRetrieveUpdateDelete:
#     def __init__(self):
#         self.con=mysql.connector.connect(user="root",password="root",host="localhost",database="showroom")
#         self.c=self.con.cursor()
#         print("DataBase Connection Established")
#     def list(self):
#         query="select * from vehicle"
#         self.c.execute(query)
#         records=self.c.fetchall()
#         if records:
#             for row in records:
#                 print(row)
#         else:
#             print("No Records Found")
#     def create(self,brand,model,price,year):
#         query="insert into vehicle (brand,model,price,year)values(%s,%s,%s,%s)"
#         data=(brand,model,price,year)
#         self.c.execute(query,data)
#         self.con.commit()
#         print("Data Inserted")
#     def retrieve(self,id):
#         query="select * from vehicle where id=%s"
#         data=(id,)
#         self.c.execute(query,data)
#         record=self.c.fetchone()
#         if record:
#             print(record)
#         else:
#             print("No Records Found")
#     def update(self,id,brand,model,price,year):
#         query="update vehicle set brand=%s,model=%s,price=%s,year=%s where id=%s"
#         data=(brand,model,price,year,id)
#         self.c.execute(query,data)
#         self.con.commit()
#     def delete(self,id):
#         query="delete from vehicle where id=%s"
#         data=(id,)
#         self.c.execute(query,data)
#         self.con.commit()
#         if self.c.rowcount>0:
#             print("Data Deleted")
#         else:
#             print("No Records Found")
# v=BookListCreateRetrieveUpdateDelete()
# v.list()
# v.create("bmw","m3",10000000,2025)
# v.retrieve(2)
# v.update(id=3,brand="audi",model="q5",price=200000000,year=2020)
# v.delete(5)