from utils import (
    load_students,
    add_student,
    delete_student,
    search_student
)

students = load_students()

while True:
    try:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. View students")
        print("3. Delete student")
        print("4. Search student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            if name:
                add_student(students, name)
                print(f"{name} added successfully")
            else:
                print("Name cannot be empty.")

        elif choice == "2":
            print("\nStudent List:")
            if not students:
                print("No students found.")
            else:
                for s in students:
                    print("-", s)

        elif choice == "3":
            name = input("Enter name to delete: ").strip()
            if delete_student(students, name):
                print(f"{name} deleted successfully")
            else:
                print("Student not found.")

        elif choice == "4":
            name = input("Enter name to search: ").strip()
            if search_student(students, name):
                print(f"{name} exists in records")
            else:
                print("Student not found.")

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")

    except Exception as e:
        print("An unexpected error occurred:", e)
