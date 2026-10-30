# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
# factorial using math.factorial with try-except

# import math
# try:
#     n = int(input("Enter number"))
#     print("Factorial", math.factorial(n))
# except ValueError:
#     print("Invalid input")
#
#
# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.

# simple calculator with exception handling

# try:
#     print("1 Add")
#     print("2 Sub")
#     print("3 Multipli")
#     print("4 Div")
#
#     choice = int(input("Enter choice "))
#     a = int(input("Enter first number"))
#     b = int(input("Enter second number "))
#
#     if choice == 1:
#         print("Result", a + b)
#     elif choice == 2:
#         print("Result=", a - b)
#     elif choice == 3:
#         print("Result", a * b)
#     elif choice == 4:
#         try:
#             print("Result =", a / b)
#         except ZeroDivisionError:
#             print("Division by zero")
#     else:
#         print("Invalif")
#
# except ValueError:
#     print("Invalid input")


# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist

# file open with exception handling

try:
    f = open("myfile.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File does not exist")
