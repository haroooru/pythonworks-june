# single level inheritance
# company example

# +-------------------+
# |     Company       |
# +-------------------+
# | - name            |
# +-------------------+
# | + ShowDetails()   |
# +-------------------+
#          |
#          |
#          v
# +---------------------------+
# |        Employee           |
# +---------------------------+
# | - Empid                   |
# | - Designation             |
# | - Salary                  |
# +---------------------------+
# | + getSalary()             |
# | + ShowEmployeeDetails()   |
# +---------------------------+


class Company:   # Parent class
    def __init__(self):   # only self
        self.name = input("Enter company name: ")

    def showDetails(self):
        print("Company Name:", self.name)


class Employee(Company):   # Child class
    def __init__(self):   # only self
        super().__init__()   # call parent constructor
        self.empid = int(input("Enter employee id: "))
        self.designation = input("Enter designation: ")
        self.salary = int(input("Enter salary: "))

    def getSalary(self):
        return self.salary

    def showEmployeeDetails(self):
        super().showDetails()   # show company info first
        print("EmpID:", self.empid)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


# Object creation
e = Employee()
e.showEmployeeDetails()
print("Fetched Salary:", e.getSalary())


# Multi-level inheritance

# +---------------------------+       +---------------------------+
# |         Hospital          |       |     DepartmentName        |
# +---------------------------+       +---------------------------+
# | - HName                   |       | - DocName                 |
# | - Location                |       +---------------------------+
# +---------------------------+       | + ShowDeptDetails()       |
# | + ShowDetails()           |       +---------------------------+
# +---------------------------+                  |
#            |                                   |
#            |                                   |
#            +---------------+-------------------+
#                            |
#                            v
# +----------------------------------+
# |            Patient               |
# +----------------------------------+
# | - id                             |
# | - name                           |
# | - gender                         |
# | - place                          |
# | - adm_date                       |
# | - dischargedate                  |
# +----------------------------------+
# | + fullSummary()                  |
# | + dischargeDetails()             |
# +----------------------------------+

# Multi Level Inheritance (Classroom Notes)

# Multiple Inheritance (Classroom Notes)

# - Hospital class: hname
# - Department class: docname
# - Patient inherits both Hospital and Department
# - Input taken inside __init__() with only self

# class Hospital:   # Parent 1
#     def __init__(self):   # only self
#         self.hname = input("Enter hospital name: ")
#
#     def showDetails(self):
#         print("Hospital Name:", self.hname)
#
#
# class Department:   # Parent 2
#     def __init__(self):   # only self
#         self.docname = input("Enter doctor name: ")
#
#     def showDeptDetails(self):
#         print("Doctor Name:", self.docname)
#
#
# class Patient(Hospital, Department):   # Child inherits both
#     def __init__(self):   # only self
#         Hospital.__init__(self)     # call Hospital constructor
#         Department.__init__(self)   # call Department constructor
#         self.id = int(input("Enter patient id: "))
#         self.name = input("Enter patient name: ")
#         self.gender = input("Enter gender: ")
#         self.place = input("Enter place: ")
#         self.adm_date = input("Enter admission date: ")
#         self.dischargedate = input("Enter discharge date: ")
#
#     def fullSummary(self):
#         self.showDetails()
#         self.showDeptDetails()
#         print("Patient ID:", self.id)
#         print("Name:", self.name)
#         print("Gender:", self.gender)
#         print("Place:", self.place)
#         print("Admission Date:", self.adm_date)
#         print("Discharge Date:", self.dischargedate)
#
#     def dischargeDetails(self):
#         print("Patient", self.name, "discharged on", self.dischargedate)
#
#
# # Object creation
# p = Patient()
# p.fullSummary()
# p.dischargeDetails()

