from database.connection import get_connection
from models import student
from tabulate import tabulate


class StudentService:

    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor()

    import mysql.connector
from database.connection import get_connection


class StudentService:

    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor()

    def add_student(self, student):

        query = """
        INSERT INTO students
        (roll_no, name, email, phone, branch, year, cgpa)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            student.roll_no,
            student.name,
            student.email,
            student.phone,
            student.branch,
            student.year,
            student.cgpa
        )

        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("\n✅ Student Added Successfully!")

        except mysql.connector.IntegrityError:
            print("\n❌ Roll Number or Email already exists.")

        except mysql.connector.Error as err:
            print(f"\n❌ Database Error: {err}")
    def view_students(self):
            query = """
                SELECT id, roll_no, name, branch, year, cgpa
                FROM students
                ORDER BY id;
                """

            self.cursor.execute(query)
            students = self.cursor.fetchall()

            if not students:
                    print("\n❌ No students found.")
                    return

            headers = [
                    "ID",
                    "Roll No",
                    "Name",
                    "Branch",
                    "Year",
                    "CGPA"
                ]

            print()
            print(tabulate(students, headers=headers, tablefmt="grid"))
    
    def search_student(self):

        print("\n===== Search Student =====")
        print("1. Search by Roll Number")
        print("2. Search by Name")
        print("3. Search by Branch")
        print("0. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            field = "roll_no"
            value = input("Enter Roll Number: ")

        elif choice == "2":
            field = "name"
            value = input("Enter Name: ")

        elif choice == "3":
            field = "branch"
            value = input("Enter Branch: ")

        elif choice == "0":
            return

        else:
            print("❌ Invalid Choice")
            return

        query = f"""
        SELECT id, roll_no, name, branch, year, cgpa
        FROM students
        WHERE {field} LIKE %s
        """

        self.cursor.execute(query, (f"%{value}%",))
        students = self.cursor.fetchall()

        if not students:
            print("\n❌ No student found.")
            return

        headers = [
            "ID",
            "Roll No",
            "Name",
            "Branch",
            "Year",
            "CGPA"
        ]

        print()
        print(tabulate(students, headers=headers, tablefmt="grid"))