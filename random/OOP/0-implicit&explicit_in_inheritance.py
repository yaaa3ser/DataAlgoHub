class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)   # Explicit call to super class constructor
        
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)        # Implicit call to super class constructor ===> changing in Person class name will not affect this class 
        # no self parameter is required here because we actually here have an object returned by super() function
        # or
        super(Student, self).__init__(name, age) # Explicit call to super class constructor
        
