#
# class Patient:
#     def setdischargedate(self):
#         self.dischargedate = input("Please enter discharge date: ")
#
#     def fullsummary(self):
#         Hospital.showdetails(self)
#         Department.showdepartment(self)
#         print("Patient details")
#         print("Patient name: ", self.pname)
#         if self.dischargedate == "":
#             print("Not yet discharged.")
#         else:
#             print("Discharge date: ", self.dischargedate)
#
# c = Patient()
# c.fullsummary()
# c.setdischargedate()
# c.fullsummary()











# # ============================
# # Polymorphism in Python
# # ============================
#
# # Example 1: Same function name in different classes
# class A:
#     def f1(self):
#         print("in class A f1")
#
# class B:
#     def f1(self):
#         print("in class B f1")
#
# class C:
#     def f1(self):
#         print("in class C f1")
#
# # Diagram:
# #   +---------+       +---------+       +---------+
# #   |  Class A|       |  Class B|       |  Class C|
# #   | f1()    |       | f1()    |       | f1()    |
# #   +---------+       +---------+       +---------+
# #        |                 |                 |
# #        v                 v                 v
# #   "in class A f1"   "in class B f1"   "in class C f1"
#
# a = A()
# a.f1()   # in class A f1
#
# b = B()
# b.f1()   # in class B f1
#
# c = C()
# c.f1()   # in class C f1
#
#
# # Example 2: Polymorphism with Inheritance (Method Overriding)
# class Parent:
#     def f1(self):
#         print("in parent class f1")
#
# class Child(Parent):
#     def f1(self):
#         print("in child class f1")
#
# # Diagram:
# #   Parent ----> Child
# #   f1() overridden
# #
# #   Parent.f1()  -> "in parent class f1"
# #   Child.f1()   -> "in child class f1"
#
# c = Child()
# c.f1()   # in child class f1
#
#
#
# # ============================
# # Polymorphism in Python
# # ============================
#
# # Case 1: In SAME class (method overloading attempt)
# class A:
#     def f1(self):
#         print("in f1")
#     def f1(self, a):
#         print("in f1", a)
#     def f1(self, a, b):
#         print("in f1", a, b)
#
# # Diagram:
# #   Class A
# #   └── f1()   [overwritten]
# #   └── f1(a)  [overwritten]
# #   └── f1(a,b) [last one kept]
# #
# # Only the LAST definition survives in Python.
#
# a = A()
# # a.f1()        # ERROR: missing arguments
# # a.f1(10)      # ERROR: missing arguments
# a.f1(10,20)     # Works → "in f1 10 20"
#
#
# # Case 2: In DIFFERENT classes (method names same, code different)
# class A:
#     def f1(self):
#         print("in class A f1")
#
# class B:
#     def f1(self):
#         print("in class B f1")
#
# class C:
#     def f1(self):
#         print("in class C f1")
#
# # Diagram:
# #   +---------+       +---------+       +---------+
# #   |  Class A|       |  Class B|       |  Class C|
# #   | f1()    |       | f1()    |       | f1()    |
# #   +---------+       +---------+       +---------+
# #        |                 |                 |
# #        v                 v                 v
# #   "in class A f1"   "in class B f1"   "in class C f1"
#
# a = A()
# a.f1()   # in class A f1
#
# b = B()
# b.f1()   # in class B f1
#
# c = C()
# c.f1()   # in class C f1
#
#
# # Case 3: Inheritance + Method Overriding
# class Parent:
#     def f1(self):
#         print("in parent class f1")
#
# class Child(Parent):
#     def f1(self):
#         print("in child class f1")
#
# # Diagram:
# #   Parent ----> Child
# #   f1() overridden
# #
# #   Parent.f1()  -> "in parent class f1"
# #   Child.f1()   -> "in child class f1"
#
# c = Child()
# c.f1()   # in child class f1
#






# Polymorphism
# → An entity behaves in different forms.
# → Same function/operator can work differently depending on context.

# Examples of Polymorphism in Python:
# Built-in operator +
#   + with integers → addition → 12+3 = 15
#   + with strings → concatenation → '12'+'3' = '123'
#   + with lists → merging → [0,1]+[2,3] = [0,1,2,3]

# Built-in function len()
#   len("hello") → counts characters → 5
#   len([10,20,30]) → counts elements → 3

# Polymorphism in Classes:
# → Different classes can have functions with the same name but different code.
# → Example: class A, class B, class C all have f1() but each prints differently.

# Polymorphism in Inheritance:
# → Child class can override parent class function.
# → This is called Method Overriding.

# Method Overriding
# → OOP allows a child class to provide specific implementation of a function already defined in parent class.
# → Used to modify or extend parent functionality.
# → Overriding methods must have same name and same number of parameters.



# 1. Create a class named Movie with attributes:
#    moviename, year, language, director, rating
#    and methods:
#    - display_details()
#    - update_rating()

# ==============================
# Hierarchical Inheritance Diagram
# ==============================

# +-----------------------------+
# |          Vehicle            |
# +-----------------------------+
# | - Brand                     |
# | - Model                     |
# | - Color                     |
# | - Year                      |
# +-----------------------------+
# | + display()                 |
# +-----------------------------+
#           /       \
#          /         \
# +----------------+   +----------------+
# |      Car       |   |      Bike      |
# +----------------+   +----------------+
# | - mileage      |   | - cc           |
# +----------------+   +----------------+
# | + display()    |   | + display()    |
# +----------------+   +----------------+
#
# Example object creation:
#   c = Car()
#   b = Bike()


# 2. Create a Python program using Hierarchical Inheritance
#    for a vehicle management system.
#    Create a parent class Vehicle with attributes:
#    brand, model, color, year
#    Add a method display() in Vehicle class to show details.
#    Create two child classes:
#    - Car with an additional attribute mileage
#    - Bike with an additional attribute cc
#    Override the display() method in both child classes
#    Create objects of both classes, accept input from user,
#    and display the details.


