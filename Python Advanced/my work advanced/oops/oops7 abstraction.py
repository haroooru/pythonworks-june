# # class example
# class Employee:
#     # attributes
#     # (here we can store data like name, age, etc.)
#
#     # methods
#     def show(self):
#         print(self.name)
#
#
# # object creation
# e = Employee()
# e.show()
#
# e1 = Employee()
# e1.show()


# CLASS → blueprint for objects
# ATTRIBUTES → variables inside class (like name, age)
# METHODS → functions inside class (like show())

# self → refers to the current object
# self.name → means "name" of that particular object

# e = Employee() → creates object e
# e.show() → calls show() method for object e
# print(self.name) → prints the name attribute of that object

# If we don’t assign e.name before calling show(),
# it will give error because 'name' is not defined yet.




# SUPER KEYWORD NOTES
# -------------------
# super() → used in child class to call parent class methods/constructors
# Types:
#   1) super().__init__() → call parent constructor
#   2) super().show()     → call parent method
#   3) super().anymethod()→ call any parent method
#   4) super().variable   → access parent variable (if defined in __init__)



# # Example 1: super().__init__()
# class Person:
#     def __init__(self):
#         self.name = "Hari"
#         print("Parent init")
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()   # call parent constructor
#         self.rollno = 101
#         print("Child init")
#
# s = Student()
# print(s.name, s.rollno)
#
# # Output:
# # Parent init
# # Child init
# # Hari 101




# # Example 2: super().show()
# class Person:
#     def show(self):
#         print("Parent show")
#
# class Student(Person):
#     def show(self):
#         super().show()   # call parent show
#         print("Child show")
#
# s = Student()
# s.show()
#
# # Output:
# # Parent show
# # Child show


# # Example 3: super().anymethod()
# class A:
#     def greet(self):
#         print("Hello from A")
#
# class B(A):
#     def greet(self):
#         super().greet()   # call parent greet
#         print("Hello from B")
#
# b = B()
# b.greet()
#
# # Output:
# # Hello from A
# # Hello from B


# # Example 4: super().variable
# class Base:
#     def __init__(self):
#         self.x = 10
#
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#         print("Value from parent:", super().x)
#
# d = Derived()
#
# # Output:
# # Value from parent: 10






# # Method overriding (inheritance)
#
# class A:
#     def f(self):
#         # code1
#
# class B(A):
#     pass
#
# b = B()
# b.f()
#
# # Child f


# METHOD OVERRIDING → when child class defines same method as parent
# Inheritance → child class (B) gets all methods of parent (A)
# If child does not override → parent method runs
# If child overrides → child method replaces parent method

# In this code:
# class A has method f()
# class B inherits from A
# class B has no f() → so it uses parent’s f()
# b = B() → creates object of child class
# b.f() → calls f() from parent (since child has none)










# # Python → no true method overloading
# # Last def wins
# # f(10) works only if default args are used
# # Other languages → compiler keeps all versions
# # Python workaround → default args or *args
#
#
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
# a.f(10)        # ❌ ERROR → missing 1 argument (b)
# a.f(20,30)     # ✅ prints "code3"
#
# # In Python:
# # - Only the LAST definition of f() survives.
# # - That is def f(self,a,b).
# # - So f() expects 2 arguments (a,b).
# # - a.f() → error (needs 2 args, got 0)
# # - a.f(10) → error (needs 2 args, got 1)
# # - a.f(20,30) → works (2 args given)
#
#
# # Example: + operator
# print(10 + 20)        # adds numbers → 30
# print("Hari" + "Priya")  # concatenates strings → HariPriya
# print([1,2] + [3,4])  # merges lists → [1,2,3,4]
#
# # Behind the scenes:
# # 10 + 20 → calls int.__add__(10,20)
# # "Hari" + "Priya" → calls str.__add__("Hari","Priya")
# # [1,2] + [3,4] → calls list.__add__([1,2],[3,4])
#
#
# # Polymorphism → "same name, different behavior"
# # Operator Overloading is a type of polymorphism.
# # Example:
# #   + works differently for int, str, list, and user-defined classes.
# #   Same operator, multiple forms → polymorphism.
#
#
# # Abstraction in Python
# # ---------------------
# # → Hiding implementation details
# # → Showing only essential features to the user
#
# # Implemented using:
# #   1) Abstract Class
# #   2) Abstract Method
#
# # Abstract Class → class that contains abstract methods
# # Abstract Method → method without implementation (only declaration)
#
#
#
#
#
#
#
#
# class classname:
#     #attributes
#     #methods
#     def f(self):
#         #code
#
# class AbstractClass:
#     #attributes
#     #methods
#     def f(self):
#         pass
# # Normal Class (classname):
# # - Can have attributes (variables) and methods (functions).
# # - Methods contain actual code (implementation).
# # - Objects can be created directly.
#
# # Abstract Class (AbstractClass):
# # - Contains abstract methods (methods with no code).
# # - def f(self): pass → means "method declared but not implemented".
# # - Abstract class sets a rule → child classes must implement those methods.
# # - Cannot create object of abstract class directly.
# # - Used to hide implementation and enforce structure.
#
#
#
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
#
# # Vehicle → parent class (abstract style)
# # - Methods are declared but only 'pass' (no code).
# # - This is abstraction → hiding implementation.
#
# # Car → child class (inherits Vehicle)
# # - Overrides start() method with its own code.
# # - Other methods (stop, accelerate, apply_brak) still empty
# #   unless Car overrides them too.
#
# # Object of Car → can call start(), stop(), accelerate(), apply_brak()
# # - start() will run Car’s version
# # - others will run parent’s 'pass' (do nothing) until overridden
#









# # Abstract Class
# # --------------
# # - Acts as a template for subclasses
# # - Cannot create object of abstract class directly
# # - Subclasses must implement all abstract methods
# # - If subclass misses any → ERROR
#
# from abc import ABC, abstractmethod
#
# class Abstract_class(ABC):   # Abstract Base Class
#     @abstractmethod
#     def f(self):             # Abstract method
#         pass                 # no code here
#
#     # non-abstract methods can also be written here


# # She is teaching ABSTRACTION
# # - Abstract class acts as a TEMPLATE
# # - It defines "what methods must exist" (area, perimeter)
# # - It hides "how they work" → no code inside
# # - Child classes (Rectangle, Square) must implement those methods
# # - Only then you can create objects of child classes
#
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
# s = Shape()   # ❌ ERROR

# ERROR → Cannot create object of abstract class
# Reason → Abstract class has abstract methods (no code)
# Python rules → You must override all abstract methods in child class
# If you try to instantiate Shape directly → TypeError





# # coorect example
# class Rectangle(Shape):
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
# r = Rectangle()
# r.get_area()
# r.get_perimeter()
