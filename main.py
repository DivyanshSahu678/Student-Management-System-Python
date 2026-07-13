from utils.menu import show_menu
from services.student_service import StudentService
from models.student import Student

from utils.validator import (
    is_valid_email,
    is_valid_phone,
    is_valid_year,
    is_valid_cgpa,
)


def main():
    service = StudentService()

    while True:
        show_menu()

        choice = input("\nEnter Choice: ")

        if choice == "1":

            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            branch = input("Enter Branch: ")

            try:
                year = int(input("Enter Year: "))
                cgpa = float(input("Enter CGPA: "))
            except ValueError:
                print("❌ Year must be an integer and CGPA must be a number.")
                continue

            if not is_valid_email(email):
                print("❌ Invalid Email")
                continue

            if not is_valid_phone(phone):
                print("❌ Invalid Phone Number")
                continue

            if not is_valid_year(year):
                print("❌ Year must be between 1 and 4")
                continue

            if not is_valid_cgpa(cgpa):
                print("❌ CGPA must be between 0 and 10")
                continue

            student = Student(
                roll_no,
                name,
                email,
                phone,
                branch,
                year,
                cgpa
            )

            service.add_student(student)
        elif choice == "2":
            service.view_students()
        
        elif choice == "3":
            service.search_student()
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            service.update_student()
            input("\nPress Enter to continue...")
        
        elif choice == "0":
            print("\nThank You 😊")
            break

        else:
            print("\nFeature Coming Soon...")


if __name__ == "__main__":
    main()