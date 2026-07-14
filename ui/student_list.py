import customtkinter as ctk
from tkinter import ttk

from services.student_service import StudentService


class StudentList(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.service = StudentService()

        self.pack(fill="both", expand=True, padx=20, pady=20)

        title = ctk.CTkLabel(
            self,
            text="Student List",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=15)

        refresh_btn = ctk.CTkButton(
            self,
            text="🔄 Refresh",
            command=self.load_students
        )
        refresh_btn.pack(pady=10)

        columns = (
            "Roll No",
            "Name",
            "Branch",
            "Year",
            "CGPA",
            "Email",
            "Phone"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.load_students()

    def load_students(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        students = self.service.view_students()

        for student in students:
            self.tree.insert("", "end", values=student)