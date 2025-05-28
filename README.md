      
# README.md

# 🎓 Student Grade Tracker

A simple command-line application written in Python to manage student names and their grades. This project demonstrates basic Python concepts including functions, loops, conditionals, dictionaries, lists, and file I/O using JSON for data persistence.

## 🌟 Features

*   **Add Students:** Add new students along with their grades.
*   **View All Students:** Display a list of all students, their individual grades, and their average grade.
*   **Calculate Class Average:** Compute the overall average grade for all students in the tracker.
*   **Find Top Student(s):** Identify student(s) with the highest average grade.
*   **Update Grades:** Modify the grades for an existing student (this will replace all existing grades for that student).
*   **Remove Student:** Delete a student's record from the tracker.
*   **Search for Student:** Look up a specific student and display their details.
*   **Data Persistence:** Student data is saved locally in a `student_grades.json` file, so information is retained between sessions.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Python:** Version 3.6 or higher. (The script uses f-strings and standard library modules like `json` and `os` which are available in these versions). You can download Python from [python.org](https://www.python.org/downloads/).
*   **Git:** (Optional, but recommended for cloning the repository). You can download Git from [git-scm.com](https://git-scm.com/downloads).

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### 1. Clone the Repository (Optional)

If you have Git installed and this project is hosted on a platform like GitHub, open your terminal or command prompt and run:
git clone <https://github.com/Ratan-Priyanshu/Student_Grade_Tracker.git>
and go to the directory by : 
cd Student_Grade_Tracker

If you don't want to clone, simply save the Python code above as a file named grade_tracker.py.

### 2. Navigate to the Project Directory

If you cloned, you should already be in the project directory. If you saved the file manually, navigate to the directory where you saved grade_tracker.py.

### 3. Run the Application

Execute the Python script from your terminal:      
python grade_tracker.py
The application will start, and you will see a menu with options to manage student grades.

### 💻 How to Use

Once the application is running, you will be presented with a menu:
      
--- Student Grade Tracker Menu ---
1. Add Student and Grades
2. View All Students
3. Calculate Overall Class Average
4. Find Top Student(s)
5. Update Student Grades (Replaces all)
6. Remove Student
7. Search for Student
8. Exit

Enter the number corresponding to the action you wish to perform and follow the on-screen prompts.

   When adding or updating grades (marks), enter numeric values between 0 and 100.
   Type done when prompted to finish entering grades for a student.

### 💾 Data Storage : 

   Student data (names and their lists of grades) is stored in a file named student_grades.json in the same directory as the grade_tracker.py script.
   This file is automatically created when you save data for the first time (e.g., after adding the first student).
   If the student_grades.json file is deleted or is empty, the program will start with an empty student list.

### 🏗️ Project Structure : 

If you only have the script, your structure will be:      
your_project_directory/
└── grade_tracker.py        # The main Python script
└── student_grades.json     # Data file (auto-generated on first save)

###💡 Potential Future Enhancements :

   - More Robust Error Handling: Implement try-except blocks for input validation (e.g., non-numeric grades) and file operations to prevent crashes.
   - Granular Grade Updates: Allow appending new grades or modifying specific grades instead of replacing all.
   - Support for Multiple Subjects/Assignments: Extend the data structure to handle grades for different subjects or assignments per student.
   - Sorting and Filtering: Add options to sort students by name or average grade, or filter by grade range.
   - Import/Export Data: Functionality to import student data from or export to formats like CSV.
   - Graphical User Interface (GUI): Develop a GUI using libraries like Tkinter, PyQt, or Kivy for a more user-friendly experience.
   - Unit Tests: Write tests to ensure the reliability of different functions.

### 🤝 Contributing :

This is a simple project, but it is hosted publicly, typical contribution guidelines would apply. For personal use, feel free to modify and extend it as you see fit!
