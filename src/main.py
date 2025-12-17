from utils import add_student, get_students

students = []

while True:
    print("\nStudent Management System")
    print("1. Add student")
    print("2. View students")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter student name: ")
        print(add_student(students, name))

    elif choice == "2":
        print("\nStudent List:")
        if not students:
            print("No students added yet.")
        else:
            for s in get_students(students):
                print("-", s)

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
