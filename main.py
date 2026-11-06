import mysql.connector

from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Meena@18062005",
        database="EmployeeDB"
    )

def add_employee():
    db = connect_db()
    cursor = db.cursor()

    name = input("Employee Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    dept = input("Department: ")
    salary = float(input("Salary: "))
    email = input("Email: ")
    city = input("City: ")

    query = """INSERT INTO Employees
    (EmployeeName, Age, Gender, Department, Salary, Email, City)
    VALUES (%s,%s,%s,%s,%s,%s,%s)"""

    values = (name, age, gender, dept, salary, email, city)

    cursor.execute(query, values)
    db.commit()

    print("Employee Added Successfully!")

    cursor.close()
    db.close()


def view_employees():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Employees")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


def search_employee():
    db = connect_db()
    cursor = db.cursor()

    emp_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "SELECT * FROM Employees WHERE EmployeeID = %s",
        (emp_id,)
    )

    result = cursor.fetchall()
    print(result if result else "Employee Not Found!")

    cursor.close()
    db.close()


def update_employee():
    db = connect_db()
    cursor = db.cursor()

    emp_id = int(input("Enter Employee ID: "))
    salary = float(input("Enter New Salary: "))

    cursor.execute(
        "UPDATE Employees SET Salary = %s WHERE EmployeeID = %s",
        (salary, emp_id)
    )

    db.commit()
    print("Employee Updated Successfully!")

    cursor.close()
    db.close()


def delete_employee():
    db = connect_db()
    cursor = db.cursor()

    emp_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "DELETE FROM Employees WHERE EmployeeID = %s",
        (emp_id,)
    )

    db.commit()
    print("Employee Deleted Successfully!")

    cursor.close()
    db.close()


while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
