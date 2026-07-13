class Student:
    def __init__(self, roll_no, name, email, phone, branch, year, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.email = email
        self.phone = phone
        self.branch = branch
        self.year = year
        self.cgpa = cgpa

    def __str__(self):
        return (
            f"Roll No : {self.roll_no}\n"
            f"Name    : {self.name}\n"
            f"Email   : {self.email}\n"
            f"Phone   : {self.phone}\n"
            f"Branch  : {self.branch}\n"
            f"Year    : {self.year}\n"
            f"CGPA    : {self.cgpa}"
        )