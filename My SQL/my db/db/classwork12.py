
# 1.Create a table named students to store student information.

import sqlite3

con = sqlite3.connect("classroom.db")
# Table: students
# Column Name
# Data Type
# Description
# command = """ create table students (studentid int primary key
#                                     , name varchar(100), age int, gender varchar(10),
#                                     course varchar(10), marks int , city varchar(100) )"""

# con.execute(command)
# student_id
# INT (Primary Key)
# Unique student ID
#
# name
# VARCHAR(100)
# Name of the student
#
# age
# INT
# Age of the student
#
# gender
# VARCHAR(10)
# Gender
#
# course
# VARCHAR(100)
# Enrolled course
#
# marks
# INT
# Marks obtained
#
# city
# VARCHAR(100)
# City of the student
# command = """insert into students(studentid, name, age, gender, course, marks, city)
#              values
#              (100, 'Hari', 24, 'M', 'Arts', 94, 'Kochi'),
#              (101, 'Meera', 22, 'F', 'Science', 88, 'Thrissur'),
#              (102, 'Arjun', 25, 'M', 'Commerce', 76, 'TVM'),
#              (103, 'Divya', 23, 'F', 'Maths', 91, 'Kollam')
#              """
# con.execute(command)
# con.commit()



#
# Questions
# Display all records from the students table.
e = con.execute("select * from students")
print(e.fetchall())

# Display name, course, and marks for all students.

e = con.execute("select name, course , marks from students")
print(e.fetchall())

# Display names and marks of students who scored more than 80.
e = con.execute("select name, marks from students where marks> 80")
print(e.fetchall())

# Display all details of students enrolled in Computer Science.
e = con.execute("select name, marks from students where course = 'Science'")
print(e.fetchall())
# Display names, ages, and cities of students whose age is between 18 and 22.
e = con.execute("select name,age, city from students where age > 18 and age < 22")
print(e.fetchall())

# # Display names, marks, and courses of students from Kochi, sorted by marks in descending order.
e = con.execute("select name , marks, course from students where city = 'Kochi'")
print(e.fetchall())
# Insert a new record into the students table.

con.execute("""insert into students(studentid, name, age, gender, course, marks, city)
               values(106, 'Sneha', 23, 'F', 'Science', 89, 'Kochi')""")
con.commit()

# # Update marks of all students who scored below 50 by adding 5 bonus marks.
con.execute("update students set marks = marks + 5 where marks < 50")
con.commit()

# # Delete all student records where marks are less than 35.
# Delete all student records where marks are less than 35
con.execute("delete from students where marks < 35")
con.commit()

# Verify deletion
e = con.execute("select studentid, name, marks from students")
print(e.fetchall())
