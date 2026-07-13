import re


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def is_valid_year(year):
    return year in [1, 2, 3, 4]


def is_valid_cgpa(cgpa):
    return 0 <= cgpa <= 10