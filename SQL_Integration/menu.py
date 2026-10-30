
import mysql.connector


def get_db_connection():
    try:
        #connection to db file(student_db)
        con = mysql.connector.connect(
            user="root",
            password="root",
            host="localhost",
            database="student_db"
        )
        print(con)
        return con

    except:
        print("Failed to connect")
        return


def create_student(id, name, age, place, marks):
    con = get_db_connection()
    try:
        c = con.cursor()
        query = "insert into student(id,name,age,place,marks)values(%s,%s,%s,%s,%s)"
        data = (id, name, age, place, marks)
        c.execute(query, data)
        con.commit()
        print("Student record is created")

    except:
        print("Failed to insert student data")

    finally:
        c.close()
        con.close()


def read_students():
    con = get_db_connection()
    try:
        c = con.cursor()
        query = "select * from student"
        c.execute(query)
        records = c.fetchall()

        if records:  #if records is not empty list
            for row in records:
                print(row)
        else:  #if empty
            print("no records found")

    except:
        print("Failed to read")

    finally:
        c.close()
        con.close()


def read_student(id):
    con = get_db_connection()
    try:
        c = con.cursor()
        query = "select * from student where id=%s"
        data = (id,)
        c.execute(query, data)
        record = c.fetchone()

        if record:
            print(record)
        else:
            print("No student record matching with given id")

    except:
        print("Failed to read student record")

    finally:
        c.close()
        con.close()


def update_student(id, name, age, place, marks):
    con = get_db_connection()
    try:
        c = con.cursor()
        query = "update student set name=%s,age=%s,place=%s,marks=%s where id=%s"
        data = (name, age, place, marks, id)
        c.execute(query, data)
        con.commit()

        if c.rowcount > 0:
            print("updated successfully")
        else:
            print("no student record is updated")

    except:
        print("failed to update student record")

    finally:
        c.close()
        con.close()


def delete_student(id):
    con = get_db_connection()
    try:
        c = con.cursor()
        query = "delete from student where id=%s"
        data = (id,)
        c.execute(query, data)
        con.commit()

        if c.rowcount > 0:
            print("deleted successfully")
        else:
            print("no student record is deleted")

    except:
        print("failed to delete")

    finally:
        c.close()
        con.close()


pip install mysql-connector-python
while (1):
    print("Menu driven code ")

    print("1.Create a new student record")
    print("2.Read all student records")
    print("3.Read student record by id")
    print("4.Update student record ")
    print("5.Delete student record")
    print("6.Exit")

    ch = int(input("Enter choice"))

    if ch == 1:
        id = int(input("Enter student id"))
        name = input("Enter student name")
        age = int(input("Enter age"))
        place = input("Enter place")
        marks = int(input("Enter marks"))
        create_student(id, name, age, place, marks)

    elif ch == 2:
        read_students()

    elif ch == 3:
        id = int(input("Enter id"))
        read_student(id)

    elif ch == 4:
        id = int(input("Enter student id"))
        name = input("Enter student name")
        age = int(input("Enter age"))
        place = input("Enter place")
        marks = int(input("Enter marks"))
        update_student(id, name, age, place, marks)

    elif ch == 5:
        id = int(input("Enter student id"))
        delete_student(id)

    else:
        exit()
