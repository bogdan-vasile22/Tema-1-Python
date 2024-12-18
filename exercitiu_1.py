class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        """Displays the number of employees"""
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        """Displays employee details"""
        print("Name: ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1
    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)



class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        NUME_ECHIPA = "F35-"  # Prefixul echipei
        super().__init__(name, salary)
        self.department = NUME_ECHIPA + department
        Manager.mgr_count += 1

    def display_employee(self):
        """Modify display_employee based on X % 3"""
        X = 6  # Numărul de litere din numele tău
        if X % 3 == 0:
            print("Name: ", self.name)
        elif X % 3 == 1:
            print("Salary: ", self.salary)
        elif X % 3 == 2:
            print("Department: ", self.department)


if __name__ == "__main__":
    # Crearea a 4 obiecte Manager (Y / 3 = 4)
    manager1 = Manager("Mihai", 4100, "Development")
    manager2 = Manager("Cristina", 2800, "Operations")
    manager3 = Manager("Florin", 3500, "Support")
    manager4 = Manager("Raluca", 3000, "Sales")

    # Afișarea informațiilor pentru Manageri
    print("Detalii Manageri:")
    manager1.display_employee()
    manager2.display_employee()
    manager3.display_employee()
    manager4.display_employee()

    # Crearea a 3 angajați pentru testare
    employee1 = Employee("Ionescu", 2800)
    employee2 = Employee("Marin", 3400)
    employee3 = Employee("Dumitru", 1900)

    # Afișarea informațiilor pentru Employee
    print("\nDetalii Angajați:")
    employee1.display_employee()
    employee2.display_employee()
    employee3.display_employee()

    # Afișarea numărului total de manageri și angajați
    print(f"\nNumărul total de manageri: {Manager.mgr_count}")
    print(f"Numărul total de angajați: {Employee.empCount}")
