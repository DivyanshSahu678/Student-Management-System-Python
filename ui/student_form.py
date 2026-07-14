import customtkinter as ctk
from tkinter import messagebox

from models.student import Student
from services.student_service import StudentService
from utils.validator import (
    is_valid_email,
    is_valid_phone,
    is_valid_year,
    is_valid_cgpa
)


class StudentForm(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.service = StudentService()

        self.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            self,
            text="Add New Student",
            font=("Arial", 28, "bold")
        ).pack(pady=20)

        self.roll = ctk.CTkEntry(self, width=350, placeholder_text="Roll Number")
        self.roll.pack(pady=8)

        self.name = ctk.CTkEntry(self, width=350, placeholder_text="Student Name")
        self.name.pack(pady=8)

        self.email = ctk.CTkEntry(self, width=350, placeholder_text="Email")
        self.email.pack(pady=8)

        self.phone = ctk.CTkEntry(self, width=350, placeholder_text="Phone")
        self.phone.pack(pady=8)

        self.branch = ctk.CTkEntry(self, width=350, placeholder_text="Branch")
        self.branch.pack(pady=8)

        self.year = ctk.CTkEntry(self, width=350, placeholder_text="Year")
        self.year.pack(pady=8)

        self.cgpa = ctk.CTkEntry(self, width=350, placeholder_text="CGPA")
        self.cgpa.pack(pady=8)

        ctk.CTkButton(
            self,
            text="Save Student",
            width=250,
            command=self.save_student
        ).pack(pady=25)

    def save_student(self):

        roll = self.roll.get().strip()
        name = self.name.get().strip()
        email = self.email.get().strip()
        phone = self.phone.get().strip()
        branch = self.branch.get().strip()

        try:
            year = int(self.year.get())
            cgpa = float(self.cgpa.get())
        except ValueError:
            messagebox.showerror("Error", "Year and CGPA must be numeric.")
            return

        if not is_valid_email(email):
            messagebox.showerror("Error", "Invalid Email")
            return

        if not is_valid_phone(phone):
            messagebox.showerror("Error", "Invalid Phone Number")
            return

        if not is_valid_year(year):
            messagebox.showerror("Error", "Year must be between 1 and 4")
            return

        if not is_valid_cgpa(cgpa):
            messagebox.showerror("Error", "CGPA must be between 0 and 10")
            return

        student = Student(
            roll,
            name,
            email,
            phone,
            branch,
            year,
            cgpa
        )

        success, message = self.service.add_student(student)

        if success:

            messagebox.showinfo("Success", message)

            self.clear_form()

        else:

            messagebox.showerror("Error", message)

    def clear_form(self):

        self.roll.delete(0, "end")
        self.name.delete(0, "end")
        self.email.delete(0, "end")
        self.phone.delete(0, "end")
        self.branch.delete(0, "end")
        self.year.delete(0, "end")
        self.cgpa.delete(0, "end")