def add_student(students, name):
    students.append(name)
    print(f"{name} added successfully")

def show_students(students):
    print("Student List:")
    for s in students:
        print("-", s)

students = []

add_student(students, "Rahul")
add_student(students, "Anita")
show_students(students)
