class Student:
    def __init__(self, name, student_id):
        # Initialize a student with a name, unique student ID, and an empty dictionary for assignments
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        # Add a grade for a specific assignment to the student's record
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        # Display all the assignments and grades for this student
        if self.assignments:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f"  {assignment}: {grade}")
        else:
            print(f"{self.name} has no grades recorded.")


class Instructor:
    def __init__(self, name, course_name):
        # Initialize an instructor with a name, course name, and an empty list of students
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        # Add a student to the course, ensuring they are in the instructor's student list
        self.students.append(student)
        print(f"Added student {student.name} (ID: {student.student_id}) to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        # Assign a grade to a student for a specific assignment
        # First, locate the student by their ID in the list of students
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            # If the student exists, add the grade for the assignment
            student.add_assignment(assignment_name, grade)
        else:
            # If the student was not found, display an error message
            print(f"Student ID {student_id} not found in course '{self.course_name}'.")

    def display_students_and_grades(self):
        # Display a summary of all students and their grades in the course
        print(f"Students and grades for course '{self.course_name}':")
        for student in self.students:
            print(f"\n{student.name} (ID: {student.student_id}):")
            student.display_grades()


def main():
    # Initialize the instructor and course
    instructor = Instructor("Dr. Smith", "Introduction to Python")
    
    while True:
        # Display menu options to the instructor
        print("\nOnline Course Management System")
        print("1. Add a student")
        print("2. Assign a grade")
        print("3. Display all students and their grades")
        print("4. Exit")
        
        # Get the instructor's choice
        choice = input("Enter your choice: ")

        if choice == "1":
            # Adding a student to the course
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            # Create a new student and add them to the instructor's list
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            # Assigning a grade to a student
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            try:
                # Convert the grade input to a float and assign the grade
                grade = float(input("Enter grade: "))
                instructor.assign_grade(student_id, assignment_name, grade)
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")

        elif choice == "3":
            # Display all students and their grades for the course
            instructor.display_students_and_grades()

        elif choice == "4":
            # Exit the program
            print("Exiting the Online Course Management System.")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Run the main function to start the interactive system
main()
