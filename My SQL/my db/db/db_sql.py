import mysql.connector
#
# con = mysql.connector.connect(user = "root", password ="root", host ="localhost")
#
# c=con.cursor()

# con = mysql.connector.connect(user = "root", password ="root", host ="localhost",database = "mydb2")
#
# c=con.cursor()
#
# c.execute('create table if not exists employee(empid int primary key, name varchar(30),age int, salary int, gender varchar(20),place varchar(20)')
#








import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="mydb2"
)

c = con.cursor()

# Correct CREATE TABLE with closing parenthesis
# c.execute('create table if not exists employee(empid int primary key, name varchar(30), age int, salary int, gender varchar(20), place varchar(20))')
# print("Table created")
#
# c.execute("""
# insert into employee (empid, name, age, salary, gender, place) values
# (101, 'Arun', 23, 20000, 'Male', 'Ekm'),
# (102, 'Anu', 24, 25000, 'Female', 'Thrissur'),
# (103, 'Dev', 26, 30000, 'Male', 'TVM'),
# (104, 'Meera', 22, 22000, 'Female', 'Kochi'),
# (105, 'Ajay', 30, 40000, 'Male', 'Calicut')
# """)
#
# con.commit()
# c.close()
# con.close()

c.execute('select * from employee')
k=c.fetchall()
print(k)
c.execute('select * from employee where empid = 101')
k=c.fetchall()
print(k)


c.execute('select name,age from employee where empid = 101')
k=c.fetchall()
print(k)