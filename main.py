from utils.menu import show_menu
from services.student_service import StudentService
from models.student import Student


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
            year = int(input("Enter Year: "))
            cgpa = float(input("Enter CGPA: "))

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

        elif choice == "0":
            print("\nThank You 😊")
            break

        else:
            print("\nFeature Coming Soon...")


if __name__ == "__main__":
    main()