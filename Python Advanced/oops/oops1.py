# oops
#
# whats programming paradigmn-
# style of writing program its of 3 types
#
# 1procedural
# 2oop
# 3functional
#
# python is multi paradigm programming
#
# in oops
# its mainly contained of two - class and object
# it enhance modularity and reuseability
from mimetypes import inited

# class -
# common property - eg humans,cars
# blueprint for creating objects

# something talked about - character and behavior idk

# object -
#
# real world entity that has same
# characterstics and behavior of class


# doubts
# data members and member classmethod
# whats initialisation
# whats innit
# whats self whats constructor
# whats this , whats self i only know python no java
# whats constructor whats data members
# whats user call
# whats vallue passing
# why is it invoking why its automatic
#
#
# #static
#
# class Classname :
#     def __init__(self , name , age):
#         self.name =name
#         self.age =age
#     def display(self):
#         print("name is", self.name ,self.age)
#
# #object creation
# #objectname =classname(arguments)
#
# p = Person("Athulya",23)
# p.display()


# # Question:
# # Define a class named Person. Accept name and age from the user.
# # Display the details by using show() method.
# # Create an object and call the method.
#
# class Person:
#     def __init__(self):
#         self.name = input("Enter your name: ")
#         self.age = int(input("Enter your age: "))
#
#     def show(self):
#         print(self.name, self.age)
#
# # creating objects and calling method
# p = Person()
# p.show()
#
# p1 = Person()
# p1.show()



# # Question:
# # Define a class named Employee with the following details.
# # Data members: Empid, name, age, salary, designation, place
# # Member methods: getsalary(), showpersonaldetails()
# # Create two objects for the Employee class and call the above member methods.
#
# # -------- Version 1: getsalary() with return --------
# class Employee:
#     def __init__(self):
#         self.empid = input("Enter employee ID: ")
#         self.name = input("Enter name: ")
#         self.age = int(input("Enter age: "))
#         self.salary = int(input("Enter salary: "))
#         self.designation = input("Enter designation: ")
#         self.place = input("Enter place: ")
#
#     def getsalary(self):   # returns salary
#         return self.salary
#
#     def showpersonaldetails(self):
#         print("ID:", self.empid, "Name:", self.name, "Age:", self.age,
#               "Designation:", self.designation, "Place:", self.place)
#
# e1 = Employee()
# print("Salary:", e1.getsalary())
# e1.showpersonaldetails()
#
# e2 = Employee()
# print("Salary:", e2.getsalary())
# e2.showpersonaldetails()
#
#
# # -------- Version 2: getsalary() without return --------
# class Employee2:
#     def __init__(self):
#         self.empid = input("Enter employee ID: ")
#         self.name = input("Enter name: ")
#         self.age = int(input("Enter age: "))
#         self.salary = int(input("Enter salary: "))
#         self.designation = input("Enter designation: ")
#         self.place = input("Enter place: ")
#
#     def getsalary(self):   # prints salary directly
#         print("Salary:", self.salary)
#
#     def showpersonaldetails(self):
#         print("ID:", self.empid, "Name:", self.name, "Age:", self.age,
#               "Designation:", self.designation, "Place:", self.place)
#
# e3 = Employee2()
# e3.getsalary()
# e3.showpersonaldetails()
#
# e4 = Employee2()
# e4.getsalary()
# e4.showpersonaldetails()




