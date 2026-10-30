# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# # Store student records in a list and perform all operations using the student's roll number.
#
# class Student:
#     def __init__(self):
#         self.rollno = input("Enter roll Number")
#         self.name = input("Enter Name ")
#         self.marks = float(input("Enter Marks "))
#
#     def updateMarks(self):
#         newmarks = int(input("Enter new marks"))
#         self.marks = newmarks
#
#
#     def showDetails(self):
#         print(self.rollno , self.name , self.marks)
#
#
# l = []


# while True:
#     print("\nMenu Driven Program")
#     print("1. Add Student")
#     print("2. Update Markks")
#     print("3. Display All Student Details")
#     print("4. Search Student by Roll Number")
#     print("5. Delete  Student")
#     print("6. Exit")
#
#     ch = int(input("Enter choice"))
#
#     if ch == 1:
#         s = Student()
#         l.append(s)
#
#     elif ch == 2:
#         num = input("Enter roll number")
#         for i in l:
#             if i.rollno == num:
#                 i.updateMarks()
#                 break
#         else:
#             print("student Not Found")
#
#     elif ch == 3:
#         if len(l) == 0:
#             print("No student records found")
#         else:
#             for i in l:
#                 i.showDetails()
#
#     elif ch == 4:
#         num = input("Enter roll no")
#         for i in l:
#             if i.rollno == num:
#                 i.showDetails()
#                 break
#         else:
#             print("Student Not Found")
#
#     elif ch == 5:
#         num = input("Enter roll number")
#         for i in l:
#             if i.rollno == num:
#                 l.remove(i)
#                 print("Student deleted ")
#                 break
#         else:
#             print("Student Not Found")
#
#     elif ch == 6:
#         print("Exiting program...")
#         break
#
#     else:
#         print("Invalid choice")


class Student(Person):
    super().showDetails()
    print("Roll No:", self.rollno)

s = Student()
s.studentDetails()


# Company and Employee classes

class Company:
    def __init__(self):
        self.name = input("Enter Company Name: ")

    def showDetails(self):
        print("Company Name:", self.name)


class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid = input("Enter Employee ID: ")
        self.designation = input("Enter Designation: ")
        self.salary = int(input("Enter Salary: "))

    def getsalary(self):
        print("Salary:", self.salary)

    def showEmployeeDetails(self):
        super().showDetails()
        print("Employee ID:", self.empid)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


# create object
e = Employee()
e.showEmployeeDetails()









# Hospital, Department, and Patient classes

class Hospital:
    def __init__(self):
        self.hname = input("Enter Hospital Name: ")

    def showHospital(self):
        print("Hospital Name:", self.hname)


class Department:
    def __init__(self):
        self.dname = input("Enter Department Name: ")

    def showDepartment(self):
        print("Department Name:", self.dname)


class Patient(Hospital, Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.pname = input("Please enter patient name: ")
        self.dischargedate = ""

    def setdischargedate(self):
        self.dischargedate = input("Please enter discharge date: ")

    def fullsummary(self):
        self.showHospital()
        self.showDepartment()
        print("Patient Name:", self.pname)
        if self.dischargedate == "":
            print("Not yet discharged.")
        else:
            print("Discharge date:", self.dischargedate)


# create object
p = Patient()
p.fullsummary()
p.setdischargedate()
p.fullsummary()
