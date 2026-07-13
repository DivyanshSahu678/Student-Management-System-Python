import re


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def is_valid_cgpa(cgpa):
    try:
        cgpa = float(cgpa)
        return 0 <= cgpa <= 10
    except ValueError:
        return False