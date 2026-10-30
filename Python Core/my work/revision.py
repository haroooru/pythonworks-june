# # Write a Python program to find the maximum number in a list
# #
# #
# ##
# # Without using the max() function
#
# l = [23,78,45,70,12,56]
# max = l[0]
#
# for i in l:
#     if(i > max):
#         max = i
#
# print(max)
#
#
# # Write a Python program to find the minimum number in a list
# #
# #
# # Without using the min() function
#
# l = [23,78,45,70,12,56]
# min = l[0]
#
# for i in l:
#     if(i < min):
#         min = i
#
# print(min)
#
#
# #menu
#
# while(1):
#
#     print("\nMenu Driven File Operations")
#     print("1. File Read")
#     print("2. File Write")
#     print("3. File Append")
#     print("4. File Search")
#     print("5. File Remove")
#     print("6. Exit")
#
#     ch = int(input("Enter Your Choice: "))
#
#     if ch == 1:
#         file_read()
#
#     elif ch == 2:
#         file_write()
#
#     elif ch == 3:
#         file_append()
#
#     elif ch == 4:
#         file_search()
#
#     elif ch == 5:
#         file_remove()
#
#     elif ch == 6:
#         print("Program Exited")
#         break
#
#     else:
#         print("Invalid Choice")





















#1.File Read
#2.File write
#3.File append
# #4.File Search
# #5.File Remove
# #6.Exit
#
#
# import os
# def file_read():
#     file_name=input("Enter file nme ")
#     f=open(file_name,"r")
#     content=f.read()
#     print(content)
#
# def file_write():
#     file_name=input("enter file name ")
#     f=open(file_name,"w")
#     content=input("Enter file")
#     f.write(content)
#
# def file_append():
#     file_name=input("Enter file name:")
#     f=open(file_name,"a")
#     content=input("enter file content:")
#     f.write(content)
#
# def file_search():
#     file_name=input("Enter fil name:")
#     f=open(file_name,"r")
#     content=f.read().split()
#     w=input("Enter the file to search:")
#     for k in content:
#         if k==w:
#             print("word is presnt")
#             break
#     else:
#         print("word is not present")
# def file_remove():
#     file_name=input("Enter file name:")
#     os.remove(file_name)
#
# while(1):
#     print("Menu Driven-File Operation")
#     print("1.File Read")
#     print("2.File Write")
#     print("3.File append")
#     print("4.File Search")
#     print("5.File Remove")
#     print("6.Exit")
#
#     ch=int(input("enter choice:"))
#     if ch==1:
#         file_read()
#     elif ch==2:
#         file_write()
#     elif ch==3:
#         file_append()
#     elif ch==4:
#         file_search()
#     elif ch==5:
#         file_remove()
#     elif ch==6:
#         exit()
#     else:
#         print("Invalid Choice")



# Define a class named Student with the following details:
# Data members: sname, rollno, class, mark1, mark2, mark3
# Member methods:
# calculate() - calculates the total and average
# showdetails() - displays the details of a student with average mark

# class Student:
#     def __init__(self, sname, rollno, class_name, mark1, mark2, mark3):
#         self.sname = sname
#         self.rollno = rollno
#         self.class_name = class_name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3
#         self.total = 0
#         self.avg = 0
#
#     def calculate(self):
#         self.total = self.mark1 + self.mark2 + self.mark3
#         self.avg = self.total // 3   # integer division for classroom style
#
#     def showdetails(self):
#         print("Name:", self.sname)
#         print("Roll No:", self.rollno)
#         print("Class:", self.class_name)
#         print("Total Marks:", self.total)
#         print("Average Marks:", self.avg)
#
# # create one object and call methods
# s1 = Student("Haripriya", 101, "MSc", 78, 85, 90)
# s1.calculate()
# s1.showdetails()


#create two objects and call the above methods
class Book:
    def __init__(self):
        self.bname = input("Enter Book Name: ")
        self.bid = input("Enter Book ID: ")
        self.aid = input("Enter Author id: ")

    def getauthorid(self):
        print(self.aid)

    def setauthorid(self):
        self.aid = input("Enter new Author ID: ")
        self.getauthorid()

#object 1
b1 = Book()
b1.getauthorid()
b1.setauthorid()

#object 2
b2 = Book()
b2.getauthorid()
b2.setauthorid()

