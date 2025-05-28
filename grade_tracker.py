import json
import os

STUDENTS_DATA_FILE = "student_grades.json"

def load_students_data():
    if not os.path.exists(STUDENTS_DATA_FILE):
        return {}
    with open(STUDENTS_DATA_FILE, 'r') as f:
        file_content = f.read()
    if not file_content.strip():
        return {}
    data = json.loads(file_content)
    return data

def save_students_data(students):
    with open(STUDENTS_DATA_FILE, 'w') as f:
        json.dump(students, f, indent=4)
    print("Data saved.")

def calculate_average(grades_list):
    if not grades_list:
        return 0.0
    total = 0
    for grade in grades_list:
        total += grade
    return total / len(grades_list)

def add_student(students):
    name = input("Enter student's name: ")
    if not name.strip():
        print("Student name cannot be empty.")
        return

    name = name.strip().title()

    if name in students:
        print(f"Student '{name}' already exists.")
        return

    grades = []
    while True:
        grade_input = input(f"Enter marks for {name} (0-100), or type 'done' to finish: ")
        if grade_input.lower().strip() == 'done':
            break
        grade = float(grade_input)
        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Invalid grade. Please enter a number between 0 and 100, or type 'done'.")

    if not grades:
        print(f"No grades entered for {name}. Student not added.")
        return

    students[name] = grades
    print(f"Student '{name}' added with grades: {grades}")
    save_students_data(students)

def view_all_students(students):
    if not students:
        print("No students in the tracker yet.")
        return

    print("\n--- Student Roster ---")
    for name, grades in students.items():
        average = calculate_average(grades)
        print(f"Student: {name}")
        print(f"  Grades: {grades}")
        print(f"  Average: {average:.2f}")
        print("-" * 20)

def calculate_overall_class_average(students):
    if not students:
        print("No students to calculate class average.")
        return

    all_student_averages = []
    for name in students:
        student_grades = students[name]
        if student_grades:
            student_avg = calculate_average(student_grades)
            all_student_averages.append(student_avg)

    if not all_student_averages:
        print("No grades recorded yet to calculate class average.")
        return

    class_avg = calculate_average(all_student_averages)
    print(f"\nOverall Class Average Grade: {class_avg:.2f}")

def find_top_student(students):
    if not students:
        print("No students to determine the top student.")
        return

    highest_average = -1.0
    top_scorers = []

    for name, grades in students.items():
        if not grades:
            continue
        current_average = calculate_average(grades)
        if current_average > highest_average:
            highest_average = current_average
            top_scorers = [name]
        elif current_average == highest_average:
            top_scorers.append(name)

    if not top_scorers:
        print("No grades recorded to find the top student.")
    else:
        print(f"\nTop Student(s) (Average: {highest_average:.2f}):")
        for scorer in top_scorers:
            print(f"- {scorer}")

def update_grades(students):
    name = input("Enter the name of the student to update: ").strip().title()
    if name not in students:
        print(f"Student '{name}' not found.")
        return

    print(f"Current grades for {name}: {students[name]}")

    new_grades = []
    print("Enter new grades (replacing all existing):")
    while True:
        grade_input = input(f"Enter new marks for {name} (0-100), or 'done': ")
        if grade_input.lower().strip() == 'done':
            break
        grade = float(grade_input)
        if 0 <= grade <= 100:
            new_grades.append(grade)
        else:
            print("Invalid marks. Please enter a number between 0 and 100, or type 'done'.")

    if not new_grades:
        print("No new grades entered. Grades remain unchanged.")
    else:
        students[name] = new_grades
        print(f"Grades for {name} updated to: {students[name]}")
        save_students_data(students)

def remove_student_record(students):
    name = input("Enter the name of the student to remove: ").strip().title()
    if name not in students:
        print(f"Student '{name}' not found.")
        return

    confirm = input(f"Are you sure you want to remove {name}? (yes/no): ").lower()
    if confirm == 'yes':
        del students[name]
        print(f"Student '{name}' removed.")
        save_students_data(students)
    else:
        print("Removal cancelled.")

def search_for_student(students):
    name = input("Enter the name of the student to search for: ").strip().title()
    if name in students:
        grades = students[name]
        average = calculate_average(grades)
        print(f"\n--- Student Details ---")
        print(f"Student: {name}")
        print(f"  Grades: {grades}")
        print(f"  Average: {average:.2f}")
    else:
        print(f"Student '{name}' not found.")

def main():
    student_records = load_students_data()

    while True:
        print("\n--- Student Grade Tracker Menu ---")
        print("1. Add Student and Grades")
        print("2. View All Students")
        print("3. Calculate Overall Class Average")
        print("4. Find Top Student(s)")
        print("5. Update Student Grades (Replaces all)")
        print("6. Remove Student")
        print("7. Search for Student")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_student(student_records)
        elif choice == '2':
            view_all_students(student_records)
        elif choice == '3':
            calculate_overall_class_average(student_records)
        elif choice == '4':
            find_top_student(student_records)
        elif choice == '5':
            update_grades(student_records)
        elif choice == '6':
            remove_student_record(student_records)
        elif choice == '7':
            search_for_student(student_records)
        elif choice == '8':
            print("Exiting Student Grade Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()