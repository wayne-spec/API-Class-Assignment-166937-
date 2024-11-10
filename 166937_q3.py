class Employee:
    def __init__(self, name, employee_id, salary):
        # Initialize an employee with name, ID, and salary
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        # Display the employee's details
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}")

    def update_salary(self, new_salary):
        # Update the employee's salary to the new salary provided
        self.salary = new_salary
        print(f"Updated salary for {self.name} to ${self.salary}")


class Department:
    def __init__(self, department_name):
        # Initialize a department with a name and an empty list of employees
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        # Add an employee to the department
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        # Calculate and display the total salary expenditure for the department
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department is ${total_salary}")

    def display_all_employees(self):
        # Display all employees in the department
        if self.employees:
            print(f"Employees in {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in {self.department_name} department.")


def main():
    # Initialize a sample department for demonstration
    department = Department("Engineering")

    while True:
        # Display menu options to manage the department
        print("\nEmployee and Department Management System")
        print("1. Add an employee")
        print("2. Update employee salary")
        print("3. Display all employees")
        print("4. Display total salary expenditure")
        print("5. Exit")

        # Get the user's choice from the menu
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new employee
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            try:
                salary = float(input("Enter employee salary: "))
                employee = Employee(name, employee_id, salary)
                department.add_employee(employee)
            except ValueError:
                print("Invalid salary input. Please enter a numeric value.")

        elif choice == "2":
            # Update the salary of an existing employee
            employee_id = input("Enter employee ID to update salary: ")
            employee = next((emp for emp in department.employees if emp.employee_id == employee_id), None)
            if employee:
                try:
                    new_salary = float(input("Enter new salary: "))
                    employee.update_salary(new_salary)
                except ValueError:
                    print("Invalid salary input. Please enter a numeric value.")
            else:
                print(f"No employee found with ID {employee_id}")

        elif choice == "3":
            # Display all employees in the department
            department.display_all_employees()

        elif choice == "4":
            # Calculate and display the total salary expenditure for the department
            department.calculate_total_salary_expenditure()

        elif choice == "5":
            # Exit the program
            print("Exiting the Employee and Department Management System.")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Run the main function to start the interactive system
main()
