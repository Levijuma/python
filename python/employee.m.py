class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Salary: ${self.salary:.2f}")

    def calculate_annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, employees_managed=None):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.employees_managed = employees_managed or []

    def display_managed_employees(self):
        print(f"Managed employees (Department: {self.department}):")
        for emp in self.employees_managed:
            print(f"  - {emp.name}")


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_languages=None):
        super().__init__(name, employee_id, salary)
        self.programming_languages = programming_languages or set()

    def add_programming_language(self, language):
        self.programming_languages.add(language)


class Intern(Employee):
    def __init__(self, name, employee_id, salary, school_name, graduation_year):
        super().__init__(name, employee_id, salary)
        self.school_name = school_name
        self.graduation_year = graduation_year


# Example usage:
if __name__ == "__main__":
    # Create instances of different employee types
    manager1 = Manager("John Doe", "M001", 80000, "Engineering", [])
    developer1 = Developer("Alice Smith", "D001", 60000, {"Python", "JavaScript"})
    intern1 = Intern("Eva Brown", "I001", 20000, "Tech University", 2024)

    # Add managed employees for the manager
    manager1.employees_managed.append(developer1)
    manager1.employees_managed.append(intern1)

    # Display information
    manager1.display_info()
    manager1.display_managed_employees()
    developer1.display_info()
    intern1.display_info()

    # Calculate annual salary
    print(f"Annual salary for {developer1.name}: ${developer1.calculate_annual_salary():.2f}")
