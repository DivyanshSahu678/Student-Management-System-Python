from database.connection import get_connection
from models import student


class StudentService:

    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor()

    def add_student(self, student):

        query = """
        INSERT INTO students
        (roll_no, name, email, phone, branch, year, cgpa)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
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

        self.cursor.execute(query, values)
        self.connection.commit()

        print("\n✅ Student Added Successfully!")