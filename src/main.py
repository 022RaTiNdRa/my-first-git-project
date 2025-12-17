from utils import load_students, save_student

students = load_students()

while True:
    print("\nStudent Management System")
    print("1. Add student")
    print("2. View students")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter student name: ").strip()
        if name:
            save_student(name)
            students.append(name)
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
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
