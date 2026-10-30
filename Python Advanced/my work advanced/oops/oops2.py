# Q. Define a class Student with data members and methods
# Define a class named Student with the following details:
# Data members:
# sname, rollNo, cls, mark1, mark2, mark3.
# Member methods:
# calculate() - Calculates the total and average
# showdetails() - Displays the details of a student with average mark
# Create one object for the class and call the above member methods.


class Student:
    def __init__(self):
        # take input for student details
        self.sname = input("Enter Student Name: ")
        self.rollno = int(input("Enter Roll No: "))
        self.cls = input("Enter Class: ")
        self.mark1 = int(input("Enter Mark1: "))
        self.mark2 = int(input("Enter Mark2: "))
        self.mark3 = int(input("Enter Mark3: "))

    def calculate(self):
        # total and average
        self.total = self.mark1 + self.mark2 + self.mark3
        self.avg = self.total / 3

    def showdetails(self):
        # display details with average
        print("Name:", self.sname)
        print("Roll No:", self.rollno)
        print("Class:", self.cls)
        print("Mark1:", self.mark1)
        print("Mark2:", self.mark2)
        print("Mark3:", self.mark3)
        print("Total:", self.total)
        print("Average:", self.avg)

# create object and call methods
s = Student()
s.calculate()
s.showdetails()


# Q. Define a class Book with the following descriptions:
# Data members:
# bookname, book id, author id, author name, price, book title
# Member methods:
# getauthorid(), getauthorname(), getbooktitle(), getprice(),
# setauthorname(), setbooktitle(), setprice()

class Book:
    def __init__(self):
        self.bname = input("Enter Book Name: ")
        self.bid = input("Enter Book ID: ")
        self.aid = input("Enter Author ID: ")

    def getauthorid(self):   # getter method
        print("Author ID:", self.aid)

    def setauthorid(self):   # setter method
        self.aid = input("Enter new Author ID: ")
        self.getauthorid()

# object creation
b = Book()
b.setauthorid()

# Teaching Notes: Getter and Setter Methods

# 1. Getter Method (get...)
#    - Purpose: To READ or DISPLAY the value of a data member.
#    - Example: getauthorid() prints the current Author ID.
#    - Classroom line: "Getter means you are only reading the value, not changing it."

# 2. Setter Method (set...)
#    - Purpose: To UPDATE or MODIFY the value of a data member.
#    - Example: setauthorid() asks for new Author ID, stores it, then shows it.
#    - Classroom line: "Setter means you are writing a new value into the object."

# 3. Working of Code:
#    - Step 1: Object b is created → constructor runs → takes Book Name, Book ID, Author ID.
#    - Step 2: b.setauthorid() is called → asks for new Author ID.
#    - Step 3: New value replaces old one in self.aid.
#    - Step 4: getauthorid() prints the updated Author ID.

# 4. Key Point:
#    - GET = READ
#    - SET = WRITE


# Q1. Create a class named Account with attributes acctnumber, acctname, and balance.
# Initialize these values using a constructor by taking input from the user.
# Define the following methods:
# withdraw() - to withdraw an amount from the account and update the balance.
# deposit() - to deposit an amount into the account and update the balance.
# showbalance() - to display the current balance of the account.
# Create an object of the class and call the methods to perform withdrawal.

class Account:
    def __init__(self):
        self.acctnumber = input("Enter Account Number: ")
        self.acctname = input("Enter Account Name: ")
        self.balance = float(input("Enter Initial Balance: "))

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        self.balance = self.balance - amount

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance = self.balance + amount

    def showbalance(self):
        print("Balance amount is =", self.balance)

# object creation
a = Account()
a.withdraw()
a.deposit()
a.showbalance()


# Enter Account Number: 12345
# Enter Account Name: Priya
# Enter Initial Balance: 20000
# Enter amount to withdraw: 1000
# Enter amount to deposit: 5000
# Balance amount is = 24000

# or

a = Bank()      # first object created
b = Bank()      # second object created
l = [a, b]      # both objects stored inside a list

for i in l:     # loop through the list
    print(i.accno, i.name, i.balance)   # print details of each object


