from database.connection import get_connection


class StudentService:

    def __init__(self):
        self.connection = get_connection()

    def add_student(self, student):
        pass

    def view_students(self):
        pass

    def search_student(self):
        pass

    def update_student(self):
        pass

    def delete_student(self):
        pass