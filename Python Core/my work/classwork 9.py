# # 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# #
# # getarea() – to calculate and display the area of the circle.
# # getperimeter() – to calculate and display the perimeter (circumference) of the circle.
# #
# # Create an object of the Circle class and call both methods to display the results.




# import math
# class Circle:
#     def __init__(self):
#         self.radius = int(input("Enter radius of circle: "))
#
#     def getarea(self):
#         return math.pi * self.radius * self.radius
#
#     def getperimeter(self):
#         return 2 * math.pi * self.radius
#
# c = Circle()
# print("Area of circle:", c.getarea())
# print("Perimeter of circle:", c.getperimeter())






#
# # 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
# #
# # withdraw() – to withdraw an amount from the account and update the balance.
# # deposit() – to deposit an amount into the account and update the balance.
# # showbalance() – to display the current balance of the account.
# #
# # Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.



# class Account:
#     def __init__(self):
#         self.Accnumber = input("Enter Account Number: ")
#         self.Acctname = input("Enter Account Name: ")
#         self.balance = int(input("Enter Balance: "))
#
#     def withdraw(self):
#         amount = int(input("Enter amount to withdraw: "))
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             print("Withdraw successful")
#         else:
#             print("Withdraw failed")
#
#     def deposit(self):
#         amount = int(input("Enter amount to deposit: "))
#         self.balance = self.balance + amount
#         print("Deposit successful")
#
#     def showbalance(self):
#         print("Current balance:", self.balance)
#
#
# # create two objects
# a1 = Account()
# a2 = Account()
#
# # store them in a list
# l = [a1, a2]
#
# # print details of both accounts
# for k in l:
#     print(f"Account no: {k.Accnumber} Name: {k.Acctname} Balance: {k.balance}")




# Write a menu-driven Python program for a banking system using a class
# Account to perform the following operations:
#
# 1. Create an account
# 2. Withdraw money
# 3. Deposit money
# 4. Display balance
# 5. Exit
#
# Store account details in a list and search accounts using the account
# number.
# Display "Account Not Found" if the account does not exist.

class Account:
    def __init__(self):
        self.accno = input("Enter your Account Number: ")
        self.name = input("Enter your Name: ")
        self.balance = float(input("Enter your Balance: "))

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw successful")
        else:
            print("Withdraw failed")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("Deposit successful")

    def showbalance(self):
        print("Balance amount is =", self.balance)


l = []   # list to store accounts

while True:
    print("\nMenu Driven Program")
    print("1. Create an Account")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Display Balance")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        a = Account()
        l.append(a)

    elif ch == 2:
        num = input("Enter your account number: ")
        for i in l:
            if i.accno == num:
                i.withdraw()
                break
        else:
            print("Account Not Found")

    elif ch == 3:
        num = input("Enter your account number: ")
        for i in l:
            if i.accno == num:
                i.deposit()
                break
        else:
            print("Account Not Found")

    elif ch == 4:
        num = input("Enter your account number: ")
        for i in l:
            if i.accno == num:
                i.showbalance()
                break
        else:
            print("Account Not Found")

    elif ch == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")
