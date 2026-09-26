import json
import os
students = []
def  save_data():
    with open('students.json','w') as f:
        json.dump(students,f,indent=4)

def load_data():
    global students

    if os.path.exists("students.json"):
        try:
            with open("students.json", "r") as f:
                students = json.load(f)
        except json.JSONDecodeError:
            students = []
    else:
        students = []
def add_student():
    roll = input("Enter Roll Number of student: ")

    # Check for duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("A student with this Roll Number already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    marks = input("Enter Marks: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "department": department,
        "marks": marks
    }

    students.append(student)
    save_data()
    print("\nStudents are  added successfully!")


def view_students():
    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n========== Student Records ==========")

    for student in students:
        print(f"Roll Number : {student['roll']}")
        print(f"Name        : {student['name']}")
        print(f"Age         : {student['age']}")
        print(f"Department  : {student['department']}")
        print(f"Marks       : {student['marks']}")
        print("-" * 35)


def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found")
            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['name']}")
            print(f"Age         : {student['age']}")
            print(f"Department  : {student['department']}")
            print(f"Marks       : {student['marks']}")
            return

    print("Student not found.")


def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["roll"] == roll:

            print("\nLeave blank if you don't want to change the value.\n")

            name = input(f"Enter New Name ({student['name']}): ")
            age = input(f"Enter New Age ({student['age']}): ")
            department = input(f"Enter New Department ({student['department']}): ")
            marks = input(f"Enter New Marks ({student['marks']}): ")

            if name:
                student["name"] = name

            if age:
                student["age"] = age

            if department:
                student["department"] = department

            if marks:
                student["marks"] = marks
            save_data()
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_data()
            print("Student deleted successfully!")
            return
    print("Student not found.")

load_data()
while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank you for using Student Management System.")
        break

    else:
        print("Invalid choice! Please try again.")
