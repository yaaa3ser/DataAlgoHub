# mutability: the ability to change
class Employee:
    def __init__(self):
        self.c = 0
        
def inc_id(emp):
    print(id(emp)) # return a unique id for the specified object
    emp.c += 1
    
obj1 = Employee ()
obj2 = obj1

print(id(obj1)) # == ⤸
print (id(obj2))

print(obj1.c) # 0
inc_id(obj1)
print(obj1.c) # 1

inc_id(obj2)
print(obj1.c) # 2
print(obj2.c) # 2

# we created obj1 object 
# we also changed its internal value (c) to 1
# such object is called mutable object ===> its value can be changed in-place
# ======================================================================

# Immutablity: the inability to change
x = 30
y = x
z = 30
print(id(x)) # 1111
print(id(y)) # 1111
print(id(z)) # 1111
print(id(30))# 1111

# value 30 is created in memory
# int is immutable object ===> no one can change value at memory address 1111
# anything that needs value 30 might be bounded to the same memory address 1111 
# same with strings
# ======================================================================

# mix of mutable and immutable objects
class Employee:
    def __init__(self, name):
        self.name = name

obj1 = Employee("John")
obj2 = "John"

my_tuple = (obj1, obj2)
# my_tuple[0] = Employee("Jane") # TypeError

x, y = my_tuple
print(x.name) # John
# tuple itself is immutable
# we can't replace tuple items, but if an item is mutable, we can change its internal value
obj1.name = "Jane"
x, y = my_tuple
print(x.name) # Jane
# ======================================================================

# is: return True if both variables point to the same object (memory address)
# can be used also for checking types ===> if type(x) is int:
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True
print(a is b) # False

# ======================================================================

del x # delete the reference to the object, we don't delete the object itself, it will be deleted by garbage collector

# =================================================

# here is a useful link for visualization: https://pythontutor.com/

