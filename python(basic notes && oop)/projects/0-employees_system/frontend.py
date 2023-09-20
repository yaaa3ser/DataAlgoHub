from backend import EmployeesManager
from utilities import input_valid_int

class FrontendManager:
    def __init__(self):
        self.employees_manger = EmployeesManager()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = F'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                print('\nEnter employee data:')
                emp_name = input('Enter the name: ')
                emp_age = input_valid_int('Enter the age: ')
                emp_salary = input_valid_int('Enter the salary: ')

                self.employees_manger.add_employee(emp_name, emp_age, emp_salary)
            elif choice == 2:
                self.employees_manger.list_employees()
            elif choice == 3:
                age_from = input_valid_int('Enter age from: ')
                age_to = input_valid_int('Enter age to: ')
                # for simplicity: I assume no input such as 60 30_oop , but valid one: 30_oop 60 (small large)
                self.employees_manger.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input('Enter name: ')
                salary = input_valid_int('Enter new salary: ')
                self.employees_manger.update_salary_by_name(name, salary)
            else:
                break
