from employee import Employee

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, salary):
        self.employees.append(Employee(name, age, salary))

    def list_employees(self):
        if len(self.employees) == 0:
            print('\nNo employees at the moment!')
            return

        print('\n**Employees list**')
        for emp in self.employees:
            print(emp)

    def delete_employees_with_age(self, age_from, age_to):
        # remove from the back! such that we don't change the index of the next item to delete
        for idx in range(len(self.employees)-1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print('\tDeleting', emp.name)
                self.employees.pop(idx)

        # Tip - pop from middle of a list is slow! O(n)
        # One trick to make things efficient is as following
        # for every item to delete swap with the end of the list
        # e.g. if we will delete 3 items swap them to be the last 3 elements in list
        # now delete the last 3 elements
        # pros: very efficient
        # cons: we altered the list order. It depends then on the app!

        # Another easier trick is to mark the removed person with None
        # if there is a new employee to add, just put him in one of the None
        # this way complete no deletion at all!
        # you can have another playlist with None locations
        # cons: if there are many removed employees, you iterate a lot
        # workaround: after somethreshold: recreate a new fresh employees list


    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)

        if emp is None:
            print('Error: No employee with such a name')
        else:
            emp.salary = salary
