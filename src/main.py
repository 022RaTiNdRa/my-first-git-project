import argparse
from utils import (
    load_students,
    add_student,
    delete_student,
    search_student
)

students = load_students()

parser = argparse.ArgumentParser(
    description="Student Management System CLI"
)

parser.add_argument("action", choices=["add", "list", "delete", "search"])
parser.add_argument("--name", help="Student name")

args = parser.parse_args()

if args.action == "add":
    if args.name:
        add_student(students, args.name)
        print(f"{args.name} added successfully")
    else:
        print("Error: --name is required for add")

elif args.action == "list":
    if not students:
        print("No students found")
    else:
        for s in students:
            print("-", s)

elif args.action == "delete":
    if args.name:
        if delete_student(students, args.name):
            print(f"{args.name} deleted")
        else:
            print("Student not found")
    else:
        print("Error: --name is required for delete")

elif args.action == "search":
    if args.name:
        if search_student(students, args.name):
            print("Student found")
        else:
            print("Student not found")
    else:
        print("Error: --name is required for search")
