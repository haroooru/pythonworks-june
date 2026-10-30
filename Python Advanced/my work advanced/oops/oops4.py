# data members member methods?

# class Employee:        # class definition
#
#     # attributes
#     # methods
#
#     def show(self):    # method inside class
#         print(self.name)
#
# e = Employee()         # object creation
# e.show()               # method call using object






# # OOP Basic Terms (Classroom Notes)
#
# # 1. Class
# # - Blueprint or design.
# # - Defines attributes (variables) and methods (functions).
# # Example:
# class Student:
#     pass
#
# # 2. Attribute
# # - Variable inside a class.
# # - Stores data about the object.
# # Example:
# class Student:
#     def __init__(self):
#         self.name = "Priya"   # attribute
#         self.rollno = 12      # attribute
#
# # 3. Method
# # - Function inside a class.
# # - Works on object data.
# # Example:
# class Student:
#     def show(self):          # method
#         print(self.name)
#
# # 4. Object
# # - Real instance created from class.
# # Example:
# s = Student()   # object
#
# # 5. Method Call
# # - Using object to run a method.
# # Example:
# s.show()        # method call → prints name





# # Types of Inheritance (Classroom Notes)
#
# # 1. Single Inheritance
# # - One parent class, one child class.
# # - Child inherits properties of parent.
#
# class A:
#     def showA(self):
#         print("Class A method")
#
# class B(A):   # inherits A
#     def showB(self):
#         print("Class B method")
#
# obj = B()
# obj.showA()
# obj.showB()
#
#
#
#
# # 2. Multiple Inheritance
# # - One child class inherits from two parent classes.
# class A:
#     def showA(self):
#         print("Class A method")
#
# class C:
#     def showC(self):
#         print("Class C method")
#
# class B(A, C):   # inherits A and C
#     def showB(self):
#         print("Class B method")
#
# obj = B()
# obj.showA()
# obj.showC()
# obj.showB()
#
# # 3. Multilevel Inheritance
# # - Chain of inheritance (grandparent → parent → child).
# class A:
#     def showA(self):
#         print("Class A method")
#
# class B(A):   # inherits A
#     def showB(self):
#         print("Class B method")
#
# class C(B):   # inherits B (and A indirectly)
#     def showC(self):
#         print("Class C method")
#
# obj = C()
# obj.showA()
# obj.showB()
# obj.showC()
#
# # 4. Hierarchical Inheritance
# # - One parent, multiple children.
# class A:
#     def showA(self):
#         print("Class A method")
#
# class B(A):   # child 1
#     def showB(self):
#         print("Class B method")
#
# class C(A):   # child 2
#     def showC(self):
#         print("Class C method")
#
# obj1 = B()
# obj2 = C()
# obj1.showA()
# obj1.showB()
# obj2.showA()
# obj2.showC()
#
# # 5. Hybrid Inheritance
# # - Combination of two or more types (e.g., multiple + multilevel).
# # - Example: A → B, A → C, then D inherits from B and C.
# class A:
#     def showA(self):
#         print("Class A method")
#
# class B(A):
#     def showB(self):
#         print("Class B method")
#
# class C(A):
#     def showC(self):
#         print("Class C method")
#
# class D(B, C):   # hybrid (inherits from B and C)
#     def showD(self):
#         print("Class D method")
#
# obj = D()
# obj.showA()
# obj.showB()
# obj.showC()
# obj.showD()



#31 july 2026

# oops
# Inheritance

# B is child class  B(A)

# # Types of Inheritance
#
# # 1. Single level
# # One child from one parent
# class Parent:
#     # code
# class Child(Parent):
#     # code
#
# # Diagram:
# # Parent
# #   ↓
# # Child
#
#
# # 2. Multiple
# # One child from multiple parents
# class A:
#     # code
# class B:
#     # code
# class C(A, B):
#     # code
#
# # Diagram:
# # Parent A   Parent B
# #     ↓        ↓
# #       Child
#
#
# # 3. Multi level
# # Grandparent → Parent → Child
# class A:
#     # code
# class B(A):
#     # code
# class C(B):
#     # code
#
# # Diagram:
# # A
# # ↓
# # B
# # ↓
# # C
#
#
# # 4. Hierarchical
# # One parent → many children
# class Parent:
#     # code
# class Child1(Parent):
#     # code
# class Child2(Parent):
#     # code
#
# # Diagram:
# #        Parent
# #        ↓    ↓
# #   Child1   Child2
#
#
# # 5. Hybrid
# # Combination of multiple + multilevel
# class A:
#     # code
# class B(A):
#     # code
# class C(A):
#     # code
# class D(B, C):
#     # code
#
# # Diagram:
# #        A
# #       / \
# #      B   C
# #       \ /
# #        D







# # Single Level Inheritance Example
#
# class Person:          # Parent class
#     def m1(self):
#         print("m1")
#     def m2(self):
#         print("m2")
#     def showdetails(self):
#         print("Person details")
#
# class Student(Person): # Child class inherits Person
#     def m3(self):
#         print("m3")
#
# # Object creation
# s = Student()
# s.m1()          # from Person
# s.m2()          # from Person
# s.showdetails() # from Person
# s.m3()          # from Student
#
# # Diagram:
# # Person
# #   ↓
# # Student










# # Method Overriding (Classroom Notes)
#
# # Definition:
# # - When child class has a method with the same name as parent class.
# # - Child method replaces (overrides) parent method.
# # - Used to extend or change parent functionality.
#
# class Person:
#     def m1(self):
#         print("inside parent class m1")
#
# class Student(Person):
#     def m1(self):   # overriding parent method
#         super().m1()   # call parent version first
#         print("inside child class m1")  # extend functionality
#     def m3(self):
#         print("m3")
#
# # Object creation
# s = Student()
# s.m1()   # calls child m1 (which also calls parent m1)
# s.m3()





# Constructor and super() in Inheritance

class Person:   # Parent class
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def showDetails(self):
        print("Name:", self.name, "Age:", self.age)


class Student(Person):   # Child class
    def __init__(self):
        super().__init__()   # call parent constructor
        self.rollno = int(input("Enter your roll no: "))

    def studentDetails(self):
        super().showDetails()   # call parent method
        print("Roll No:", self.rollno)


# Object creation
s = Student()
s.studentDetails()
