
import mysql.connector

def get_db_connection():
    try:
        con = mysql.connector.connect(
            user = "root",
            password = "root",
            host = "localhost",
            database="employee"
        )
        print(con)
        return con

    except:
       print("no connection")


def create_employee(employee_id, name, age, department, salary):
    con = get_db_connection()
    try:
        c = con.cursor()
        query = """insert into employees(employee_id, name, age, department,salary)
                  values(%s,%s,%s,%s,%s)"""
        data = (employee_id, name, age, department, salary)
        c.execute(query, data)
        con.commit()
        print("created")
    except:
        print("failed task")
    finally:
        c.close()
        con.close()


def read_employees():
    con = get_db_connection()
    try:
        c = con.cursor()
        query = "select * from employees"
        c.execute(query)
        records = c.fetchall()
        if records:
            for r in records:
                print(r)
        else:
            print("no records ")
    except:
        print("failed ")
    finally:
        c.close()
        con.close()


def read_employee(employee_id):
    con = get_db_connection()
    try:
        c = con.cursor()
        query = "select * from employees where employee_id=%s"
        data = (employee_id,)
        c.execute(query, data)
        record = c.fetchone()
        if record:
            print(record)
        else:
            print("no id")
    except:
        print("failed")
    finally:
        c.close()
        con.close()


def update_employee(employee_id, name, age, department, salary):
    con = get_db_connection()
    try:
        c = con.cursor()
        query = "update employees set name= %s,age=%s,department = %s,salary = %s where employee_id = %s"
        data = (name, age, department, salary, employee_id)
        c.execute(query, data)

        con.commit()

        if con.rowcount > 0:
            print("updated!!!")
        else:
            print("not updated")
    except:
        print("failed")
    finally:
        c.close()
        con.close()


def delete_employee(employee_id):
    con = get_db_connection()
    try:
        c = con.cursor()
        query = "delete from employee where employee_id = %s"
        data = (employee_id,)

        c.execute(query, data)
        con.commit()
        if c.rowcount > 0:
            print("deleted")
        else:
            print("failed")
    finally:
        c.close()
        con.close()


while (1):
    print("1, create record")
    print("2, read record")
    print("3, read record by id")
    print("4, update record ")
    print("5, delete record")
    print("6,exit")

    ch = int(input("enter choice"))

    if ch == 1:
        employee_id = int(input("enter id"))
        name = input("enter name")
        age = int(input("enter age"))
        department = input("enter dept")
        salary = float(input("enter salary"))
        create_employee(employee_id, name, age, department, salary)

    elif ch == 2:
        read_employees()

    elif ch == 3:
        employee_id = int(input("enter id"))
        read_employee(employee_id)


    elif ch == 4:
        employee_id = int(input("enter id"))
        name = input("enter name")
        age = int(input("enter age"))
        department = input("enter dept")
        salary = float(input("enter salary"))
        update_employee(employee_id, name, age, department, salary)



    elif ch == 5:
        employee_id = int(input("enter id"))
        delete_employee(employee_id)
    elif ch == 6:
        exit()
