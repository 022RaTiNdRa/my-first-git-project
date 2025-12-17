FILE_PATH = "data/students.txt"

def load_students():
    try:
        with open(FILE_PATH, "r") as file:
            students = [line.strip() for line in file.readlines()]
        return students
    except FileNotFoundError:
        return []

def save_student(name):
    with open(FILE_PATH, "a") as file:
        file.write(name + "\n")
