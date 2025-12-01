EMPLOYEE_FILE = "Test1.txt"


def load_employees():
    employees = []
    try:
        with open(EMPLOYEE_FILE, "r") as file:
            for line in file:
                parts = [p.strip() for p in line.strip().split(",")]

                if len(parts) == 7:
                    emp = {
                        "id": parts[0],
                        "first": parts[1],
                        "last": parts[2],
                        "street": parts[3],
                        "city": parts[4],
                        "state": parts[5],
                        "zip": parts[6]
                    }
                    employees.append(emp)
    except FileNotFoundError:
        pass
    return employees


def save_employees(employees):
    with open(EMPLOYEE_FILE, "w") as file:
        for emp in employees:
            file.write(
                f"{emp['id']}, {emp['first']}, {emp['last']}, "
                f"{emp['street']}, {emp['city']}, {emp['state']}, {emp['zip']}\n"
            )
    print("Employees saved!")


def add_employee(employees):
    emp = {
        "id": input("ID: "),
        "first": input("First name: "),
        "last": input("Last name: "),
        "street": input("Street: "),
        "city": input("City: "),
        "state": input("State: "),
        "zip": input("ZIP: ")
    }
    employees.append(emp)
    print("Employee added!")


def delete_employee(employees):
    emp_id = input("Enter ID of employee to delete: ")
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted!")
            return
    print("Employee not found.")


def change_employee(employees):
    emp_id = input("Enter employee ID to modify: ")

    # find the employee
    for emp in employees:
        if emp["id"] == emp_id:
            break
    else:
        print("Employee not found.")
        return

    # Change menu
    while True:
        print("\nChange Menu")
        print("1. Change First Name")
        print("2. Change Last Name")
        print("3. Change Street")
        print("4. Change City")
        print("5. Change State")
        print("6. Change ZIP")
        print("7. Done Changing")

        choice = input("Choose an option: ")

        if choice == "1":
            emp["first"] = input("New First Name: ")
        elif choice == "2":
            emp["last"] = input("New Last Name: ")
        elif choice == "3":
            emp["street"] = input("New Street: ")
        elif choice == "4":
            emp["city"] = input("New City: ")
        elif choice == "5":
            emp["state"] = input("New State: ")
        elif choice == "6":
            emp["zip"] = input("New ZIP: ")
        elif choice == "7":
            print("Finished modifying employee.")
            break
        else:
            print("Invalid choice.")
    
    print("Employee updated!")


def list_employees(employees):
    if not employees:
        print("No employees to show.")
        return

    print("\n--- Employee List ---")
    for emp in employees:
        print(
            f"ID: {emp['id']} | "
            f"{emp['first']} {emp['last']} | "
            f"{emp['street']}, {emp['city']}, {emp['state']} {emp['zip']}"
        )
    print("----------------------\n")


# -------- Program starts here -------- #

employees = load_employees()

while True:
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Change Employee")   # ← added here
    print("4. List Employees")
    print("5. Save Employees")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_employee(employees)
    elif choice == "2":
        delete_employee(employees)
    elif choice == "3":
        change_employee(employees)
    elif choice == "4":
        list_employees(employees)
    elif choice == "5":
        save_employees(employees)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")