# class inheritance and overrriding its purpose


# # modification vs extention
# # 1
# class A:
#     def f(self):
#         #code1
#
# class B(A):
#     def f(self):
#         #code2
#
# b = B()
# b.f()
#
# # 2
#
# class A:
#     def f(self):
#         #code1
#
# class B(A):
#     def f(self):
#         super().f()   # call parent’s f()
#         #code2
#
# b = B()
# b.f()


# # overloading
# class A:
#     def f(self):
#         print("code1")
#
#     def f(self, a):
#         print("code2")
#
#     def f(self, a, b):
#         print("code3")
#
# a = A()
# a.f()          # ❌ ERROR → missing arguments
# a.f(10)        # ❌ ERROR → missing 1 argument
# a.f(10, 30)    # ✅ prints "code3"




# Operator overloading → same operator, multiple behaviors
# In Python:
#   + calls __add__ method internally
#   int.__add__(12,10) → addition
#   str.__add__("12","10") → concatenation
#   list.__add__([12],[10]) → merge lists
# So + is overloaded → polymorphism


# # Same operator (+) behaves differently depending on data type
#
# print(12 + 10)        # 22 → addition
# print("12" + "10")    # "1210" → string concatenation
# print([12] + [10])    # [12, 10] → list merging





# Abstraction → Hiding implementation, showing only essentials
# Example: ATM
#   - You press buttons → see balance, withdraw cash
#   - You don’t see how bank servers, cash dispenser, encryption works
# Example: Vehicle
#   - You press accelerator → car moves
#   - You don’t see how engine burns fuel, gears rotate



# Abstract Class → class which contains abstract methods
# Abstract Method → method that does not contain implementation/code

# class classname:
#     # attributes
#     # methods
#     def f(self):
#         # code (implementation)

# class Student:
#     def show(self):
#         print("Hello Student")
#
# s = Student()
# s.show()   # Hello Student




# class Vehicle:
#     def start(self):
#         pass
#     def stop(self):
#         pass
#     def accelerate(self):
#         pass
#     def apply_brak(self):
#         pass
#
# class Car(Vehicle):
#     def start(self):
#         #code


# Abstract Class → only template (rules, no code)
# Subclass → actual design (implementation)
# You cannot design logic in abstract class because it has abstract methods
# You must design (write code) in the subclass

# from abc import ABC, abstractmethod
#
# class Abstract_class(ABC):   # Abstract Base Class
#     @abstractmethod
#     def f(self):             # Abstract method
#         pass                 # no code
#
#     # attributes
#     # non-abstract methods (with code) can also be added





# Abstraction Example in Python
# -----------------------------
# Abstract class → template (rules only, no code)
# Subclass → must implement (design happens here)
# Object → created only from subclass, not abstract class

# from abc import ABC, abstractmethod
#
# class Shape(ABC):                      # Abstract class
#     @abstractmethod
#     def get_area(self):
#         pass                           # rule only, no code
#     @abstractmethod
#     def get_perimeter(self):
#         pass                           # rule only, no code
#
#
# class Rectangle(Shape):                # Subclass → design here
#     def __init__(self):
#         self.length = int(input("Enter length: "))
#         self.breadth = int(input("Enter breadth: "))
#
#     def get_area(self):
#         print("AREA =", self.length * self.breadth)
#
#     def get_perimeter(self):
#         print("PERIMETER =", 2 * (self.length + self.breadth))
#
#
# class Square(Shape):                   # Another subclass → design here
#     def __init__(self):
#         self.side = int(input("Enter side: "))
#
#     def get_area(self):
#         print("AREA =", self.side ** 2)
#
#     def get_perimeter(self):
#         print("PERIMETER =", 4 * self.side)
#
#
# # Object creation → only from subclass
# r = Rectangle()
# r.get_area()
# r.get_perimeter()
#
# s = Square()
# s.get_area()
# s.get_perimeter()


# -----------------------------
# NOTES (hash style)
# -----------------------------
# Abstract class → skeleton, cannot create object
# Abstract method → no code, only rule
# Subclass → must override and design code
# Implementation happens only in subclass
# If subclass misses → ERROR
# Rectangle → area = l*b, perimeter = 2(l+b)
# Square → area = side^2, perimeter = 4*side

# Mam is showing you errors first (when you try s = Shape()) → to prove abstract class cannot be instantiated.
#
# Then she changes code dynamically → adds Rectangle, Square → to show how implementation happens only in subclass.
#
# That’s why she says “designing only in subclass” → because abstract class is just rules, subclass is where you write the actual logic.