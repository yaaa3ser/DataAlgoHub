class Employee0:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

yasser = Employee0("Yasser", 1000)
print(yasser) # <__main__.Employee object at 0x0000020F4F6F4E80> (memory address)
# ===================================
class Employee1:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __str__(self): # must return a string
        return "Employee name: " + self.name + ", salary: " + str(self.salary)

yasser = Employee1("Yasser", 1000)
print(yasser) # Employee name: Yasser, salary: 1000
# ===================================
class Employee2:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __repr__(self): # must return a string
        return "Employee name: " + self.name + ", salary: " + str(self.salary) + "***"

yasser = Employee2("Yasser", 1000)
print(yasser) # Employee name: Yasser, salary: 1000***
# ===================================

# why both str and repr?
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __str__(self): # intended for end user / goal: readability
        return "Employee name: " + self.name + ", salary: " + str(self.salary)
    
    def __repr__(self): # intended for developer for debugging, logging / goal: unambiguity
        return 'Employee(name="' + self.name + '", salary=' + str(self.salary) + ')'

yasser = Employee("Yasser", 1000)
print(str(yasser)) # Employee name: Yasser, salary: 1000
print(repr(yasser)) # Employee(name="Yasser", salary=1000)