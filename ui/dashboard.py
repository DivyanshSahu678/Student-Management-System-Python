from ui.student_list import StudentList
from ui.student_form import StudentForm
import customtkinter as ctk


class Dashboard:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.title("Student Management System")
        self.root.geometry("1200x700")
        self.root.resizable(False, False)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # =========================
        # Sidebar
        # =========================
        self.sidebar = ctk.CTkFrame(
            self.root,
            width=220,
            corner_radius=0
        )
        self.sidebar.pack(side="left", fill="y")

        # Logo
        ctk.CTkLabel(
            self.sidebar,
            text="🎓 SMS",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        # Sidebar Buttons
        self.dashboard_btn = ctk.CTkButton(
            self.sidebar,
            text="🏠 Dashboard",
            width=180
        )
        self.dashboard_btn.pack(pady=10)

        self.add_btn = ctk.CTkButton(
            self.sidebar,
            text="➕ Add Student",
            width=180,
            command=self.show_add_student
)
        self.add_btn.pack(pady=10)

        self.view_btn = ctk.CTkButton(
           self.sidebar,
           text="📋 View Students",
           width=180,
           command=self.show_student_list
)
        self.view_btn.pack(pady=10)

        self.search_btn = ctk.CTkButton(
            self.sidebar,
            text="🔍 Search Student",
            width=180
        )
        self.search_btn.pack(pady=10)

        self.export_btn = ctk.CTkButton(
            self.sidebar,
            text="📤 Export CSV",
            width=180
        )
        self.export_btn.pack(pady=10)

        self.logout_btn = ctk.CTkButton(
            self.sidebar,
            text="🚪 Logout",
            width=180,
            fg_color="red",
            hover_color="#8B0000",
            command=self.logout
        )
        self.logout_btn.pack(side="bottom", pady=30)

        # =========================
        # Main Content
        # =========================
        self.content = ctk.CTkFrame(
            self.root,
            corner_radius=0
        )
        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Top Bar
        topbar = ctk.CTkFrame(self.content, height=70)
        topbar.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(
            topbar,
            text="Student Management Dashboard",
            font=("Arial", 24, "bold")
        ).pack(side="left", padx=20)

        ctk.CTkLabel(
            topbar,
            text="👤 Admin",
            font=("Arial", 18)
        ).pack(side="right", padx=20)

        # Statistics Cards
        cards = ctk.CTkFrame(self.content)
        cards.pack(pady=20)

        self.create_card(cards, "Total Students", "0", 0)
        self.create_card(cards, "Branches", "0", 1)
        self.create_card(cards, "Average CGPA", "0.0", 2)

        # Welcome Text
        ctk.CTkLabel(
            self.content,
            text="Welcome Admin 👋",
            font=("Arial", 28, "bold")
        ).pack(pady=40)

        ctk.CTkLabel(
            self.content,
            text="Select an option from the sidebar to continue.",
            font=("Arial", 16)
        ).pack()

    # =========================
    # Statistics Card
    # =========================
    def create_card(self, parent, title, value, column):

        card = ctk.CTkFrame(
            parent,
            width=220,
            height=120
        )
        card.grid(row=0, column=column, padx=20)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 16)
        ).pack(pady=10)

        ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 32, "bold")
        ).pack()

    # =========================
    # Logout
    # =========================
    def logout(self):

        self.root.destroy()

    # =========================
    # Run
    # =========================
    def run(self):
        self.root.mainloop()
        
    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()
            
    def show_add_student(self):

        self.clear_content()

        StudentForm(self.content)
        
    def show_student_list(self):

        self.clear_content()

        StudentList(self.content)