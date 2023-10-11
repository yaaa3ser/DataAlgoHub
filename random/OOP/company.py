'''
Part 1: Employees
-----------------
● We need to represent a company and its payroll:
    ○ Working people: either volunteers or employees
        ■ The minimal common between them is name and address information
        ■ Any working person is paid money based on its type
        ■ Each employee is paid in a specific day (varying from a person to another)

    ○ Employees could be hourly based or salaried based.
        ■ Also a commision salaried employee takes extra money as the ratio of the sales s/he did

● Develop the classes (high-level)

- Features for each class type you figure out
- amount_to_pay property that returns the salary
'''

class WorkingPerson:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
class Volunteer(WorkingPerson):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.salary = salary
            
    @property
    def amount_to_pay(self):
        return self.salary

class Employee(WorkingPerson):
    def __init__(self, name, address, day):
        super().__init__(name, address)
        self.day = day
    
class HourlyEmployee(Employee):
    def __init__(self, name, address, day, hours, salary_per_hour):
        super().__init__(name, address, day)
        self.hours = hours
        self.salary_per_hour = salary_per_hour
    
    @property
    def amount_to_pay(self):
        return self.hours*self.salary_per_hour

class SalariedEmployee(Employee):
    def __init__(self, name, address, day, monthly_salary):
        super().__init__(name, address, day)
        self.monthly_salary = monthly_salary

    @property
    def amount_to_pay(self):
        return self.monthly_salary


class CommissionSalariedEmployee(SalariedEmployee):
    def __init__(self, name, address, day, monthly_salary, commission_rate, current_month_sales):
        super().__init__(name, address, day, monthly_salary)
        self.commission_rate = commission_rate
        self.current_month_sales = current_month_sales

    @property
    def amount_to_pay(self):
        return super().amount_to_pay + self.current_month_sales * self.commission_rate

em = CommissionSalariedEmployee('Ahmed', 'Cairo', 1, 1000, 0.1, 1000)
print(em.amount_to_pay)

'''
Part 2: Invoices & Payroll
● Let’s extend the system

● There are invoices: each invoice has set of items (e.g. books, food, etc)
    ○ Each item has description, total quantity and price per item
    ○ Each item has its own details (e.g. book author name)
    ○ Invoice price: sum of the items’ prices
    
● The payroll consists of a payables list
    ○ Each payable is either employee or invoice
    ○ The total paid money is the total paid money for the added employees and invoices

● Create class Company
    ○ It creates several types of payables, add to Payroll and compute total paid money
'''

class Item:
    def __init__(self, desc, quantity, price_per_one):
        self.desc = desc
        self.quantity = quantity
        self.price_per_one = price_per_one
    
    @property
    def price(self):
        return self.quantity * self.price_per_one

'''
we can create multiple items (Book, Food, etc) which inherit from Item
'''

class Invoice:
    def __init__(self, id):
        self.id = id
        self.items = []
    
    def add_item(self,item):
        self.items.append(item)
    
    @property
    def amount_to_pay(self):
        return sum([item.price for item in self.items])

class Payroll:
    def __init__(self):
        self.payables = []
    
    def add_payable(self, payable):
        self.payables.append(payable)
    
    @property
    def amount_to_pay(self):
        return sum([payable.amount_to_pay for payable in self.payables])

class Company:
    def __init__(self):
        self.payroll = Payroll()

    def run(self):
        self.payroll.add_payable(Volunteer('Most', 'AddressV', 700))
        self.payroll.add_payable(HourlyEmployee('Belal', 'AddressH', 1, 10, 3))
        self.payroll.add_payable(SalariedEmployee('Ziad', 'AddressS', 2, 3000))
        self.payroll.add_payable(CommissionSalariedEmployee('Safa', 'AddressC', 6, 2500, 0.001, 5000))

        invoice = Invoice(1234)
        invoice.add_item(Item('book1', 10, 7))
        invoice.add_item(Item('food1', 5, 6))
        self.payroll.add_payable(invoice)

        print(self.payroll.amount_to_pay)

Company().run()


'''

'''