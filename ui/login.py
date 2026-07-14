from ui.dashboard import Dashboard
import customtkinter as ctk


class LoginWindow:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.title("Student Management System")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Heading
        title = ctk.CTkLabel(
            self.root,
            text="Student Management System",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=30)

        # Username
        self.username = ctk.CTkEntry(
            self.root,
            width=250,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        # Password
        self.password = ctk.CTkEntry(
            self.root,
            width=250,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        # Login Button
        login_btn = ctk.CTkButton(
            self.root,
            text="Login",
            command=self.login
        )
        login_btn.pack(pady=25)
    
    def login(self):

        user = self.username.get()
        password = self.password.get()

        if user == "admin" and password == "admin123":

            self.root.destroy()

            dashboard = Dashboard()
            dashboard.run()

        else:
            print("Invalid Credentials")

    def run(self):
        self.root.mainloop()