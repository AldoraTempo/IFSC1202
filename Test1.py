EMPLOYEE_FILE = "employees.txt"


def load_employees():
    """Load employees from a plain text file."""
    employees = []
    try:
        with open(EMPLOYEE_FILE, "r") as file:
            for line in file:
                emp_id, name, role = line.strip().split(",")
                employees.append({"id": emp_id, "name": name, "role": role})
    except FileNotFoundError:
        pass  # If no file exists yet, return empty list
    return employees


def save_employees(employees):
    """Save employees to a plain text file."""
    with open(EMPLOYEE_FILE, "w") as file:
        for emp in employees:
            file.write(f"{emp['id']},{emp['name']},{emp['role']}\n")
    print("Employees saved!")


def add_employee(employees):
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    role = input("Enter employee role: ")

    employees.append({"id": emp_id, "name": name, "role": role})
    print("Employee added!")


def delete_employee(employees):
    emp_id = input("Enter ID of employee to delete: ")

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted!")
            return

    print("Employee not found.")


def list_employees(employees):
    if not employees:
        print("No employees to show.")
        return

    print("\n--- Employee List ---")
    for emp in employees:
        print(f"ID: {emp['id']} | Name: {emp['name']} | Role: {emp['role']}")
    print("----------------------\n")


def main():
    employees = load_employees()

    while True:
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. List Employees")
        print("4. Save Employees")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            delete_employee(employees)
        elif choice == "3":
            list_employees(employees)
        elif choice == "4":
            save_employees(employees)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
