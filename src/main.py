from utils import add_student, get_students

students = []

print(add_student(students, "Rahul"))
print(add_student(students, "Anita"))

print("\nStudent List:")
for student in get_students(students):
    print("-", student)
