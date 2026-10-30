# Q2. Create a class named Circle with an attribute radius.
# Use a constructor to initialize the radius by accepting input from the user.
# Define the following methods:
# getarea() - to calculate and display the area of the circle.
# getperimeter() - to calculate and display the perimeter (circumference) of the circle.
# (perimeter = 2 * pi * r, area = pi * r^2, use math.pi)
# Create an object of the Circle class and call both methods to display the results.



# # Q. Write a menu-driven Python program for a banking system using a class
# # Account to perform the following operations:
# #
# # 1. Create an account
# # 2. Withdraw money
# # 3. Deposit money
# # 4. Display balance
# # 5. Exit
# #
# # Store account details in a list and search accounts using the account number.
# # Display "Account Not Found" if the account does not exist.
#
# class Account:
#     def __init__(self):
#         self.accno = int(input("Enter Account Number: "))
#         self.name = input("Enter Account Name: ")
#         self.balance = float(input("Enter Initial Balance: "))
#
#     def withdraw(self):
#         amount = float(input("Enter amount to withdraw: "))
#         self.balance = self.balance - amount
#
#     def deposit(self):
#         amount = float(input("Enter amount to deposit: "))
#         self.balance = self.balance + amount
#
#     def showbalance(self):
#         print("Balance amount is =", self.balance)
#
#
# l = []   # list to store accounts
#
# while(1):
#     print("\nMenu Driven Program")
#     print("1. Create an Account")
#     print("2. Withdraw Money")
#     print("3. Deposit Money")
#     print("4. Display Balance")
#     print("5. Exit")
#     ch = int(input("Enter your choice: "))
#
#     if ch == 1:
#         a = Account()
#         l.append(a)
#
#     elif ch == 2:
#         num = int(input("Enter your account number: "))
#         for i in l:
#             if i.accno == num:
#                 i.withdraw()
#                 break
#         else:
#             print("Account not found")
#
#     elif ch == 3:
#         num = int(input("Enter your account number: "))
#         for i in l:
#             if i.accno == num:
#                 i.deposit()
#                 break
#         else:
#             print("Account not found")
#
#     elif ch == 4:
#         num = int(input("Enter your account number: "))
#         for i in l:
#             if i.accno == num:
#                 i.showbalance()
#                 break
#         else:
#             print("Account not found")
#
#     elif ch == 5:
#         exit()


# # Q. Write a menu-driven Python program using a class Student to perform the
# # following operations:
# #
# # 1 Add Student (roll no, name, marks)
# # 2 Update Marks
# # 3 Display All Student Details
# # 4 Search Student by Roll Number
# # 5 Delete Student
# # 6 Exit
# #
# # Store student records in a list and perform all operations using the
# # student's roll number.
#
# class Student:
#     def __init__(self):
#         self.rollno = int(input("Enter Roll Number: "))
#         self.name = input("Enter Name: ")
#         self.marks = float(input("Enter Marks: "))
#
#     def showdetails(self):
#         print("Roll No:", self.rollno, "Name:", self.name, "Marks:", self.marks)
#
#
# l = []   # list to store student objects
#
# while(1):
#     print("\nMenu Driven Program")
#     print("1. Add Student")
#     print("2. Update Marks")
#     print("3. Display All Student Details")
#     print("4. Search Student by Roll Number")
#     print("5. Delete Student")
#     print("6. Exit")
#     ch = int(input("Enter your choice: "))
#
#     if ch == 1:
#         s = Student()
#         l.append(s)
#
#     elif ch == 2:
#         num = int(input("Enter Roll Number to update marks: "))
#         for i in l:
#             if i.rollno == num:
#                 i.marks = float(input("Enter new Marks: "))
#                 break
#         else:
#             print("Student not found")
#
#     elif ch == 3:
#         for i in l:
#             i.showdetails()
#
#     elif ch == 4:
#         num = int(input("Enter Roll Number to search: "))
#         for i in l:
#             if i.rollno == num:
#                 i.showdetails()
#                 break
#         else:
#             print("Student not found")
#
#     elif ch == 5:
#         num = int(input("Enter Roll Number to delete: "))
#         for i in l:
#             if i.rollno == num:
#                 l.remove(i)
#                 print("Student deleted")
#                 break
#         else:
#             print("Student not found")
#
#     elif ch == 6:
#         exit()


# Notes:
# 1. Student objects are stored in a list (l).
# 2. Add Student → create object and append to list.
# 3. Update Marks → search by rollno, change marks.
# 4. Display All → loop through list, call showdetails().
# 5. Search → find student by rollno, print details.
# 6. Delete → find student by rollno, remove from list.
# 7. Exit → stop program.
#
# Key Point:
# - Roll Number is used as unique key to identify students.
# - List allows storing multiple student records together.
# - Menu gives user choice to perform different operations.




# OOPs Principles (Improved Notes)

# 1. Class
# - Blueprint or template.
# - Defines variables (data members) and functions (methods).
# - Example: class Student → rollno, name, marks.

# 2. Object
# - Real world entity.
# - Instance of a class created using class name.
# - Example: s = Student() → s is an object.

# 3. Inheritance
# - Child class can use properties/methods of parent class.
# - Promotes reusability.
# - Example:
#   class A: → has A1, A2, Add()
#   class B(A): → inherits A1, A2, Add(), plus adds A4, Diff()

# 4. Polymorphism
# - "Many forms" → same function name, different behavior.
# - Example: len("abc") → 3, len([1,2,3]) → 3.

# 5. Encapsulation
# - Wrapping data + methods together inside a class.
# - Protects data, controls access.
# - Example: balance variable + deposit(), withdraw() inside Account class.

# 6. Abstraction
# - Showing essential details, hiding background working.
# - Example: withdraw() hides calculation, user only sees result.

# Key Points:
# - Class = design
# - Object = actual thing
# - Inheritance = reuse from parent
# - Polymorphism = same name, many forms
# - Encapsulation = data hiding
# - Abstraction = detail hiding

