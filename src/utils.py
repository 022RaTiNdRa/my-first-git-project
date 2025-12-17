import json

FILE_PATH = "data/students.json"

def load_students():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_students(students):
    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)

def add_student(students, name):
    students.append(name)
    save_students(students)

def delete_student(students, name):
    if name in students:
        students.remove(name)
        save_students(students)
        return True
    return False

def search_student(students, name):
    return name in students
