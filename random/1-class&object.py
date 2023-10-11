class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return 3.14 * self.radius * self.radius

class Editor:
    def __init__(self):
        self.rect = None
        self.circle = None
        
    def create_rect(self, width, height):
        self.rect = Rectangle(width, height)
        
    def create_circle(self, radius):
        self.circle = Circle(radius)
    
    def change(self, factor):
        self.rect.width += factor
        self.rect.height += factor
        self.circle.radius += factor
        # if we created 2 methods: change_rect and change_circle and instead, calling the 2 methods here will achieve **single responsibility principle**
    
    def print(self):
        if self.rect != None:
            print("Rectangle area: ", self.rect.get_area())
        if self.circle != None:
            print("Circle area: ", self.circle.get_area())
        
e = Editor()
e.create_rect(3, 5)
e.print()
e.create_circle(5)
e.change(2)
e.print()
# ===============================================


class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
    
    def has_next(self):
        return self.start < self.end 
    
    def get_next(self):
        if self.step > 0:
            self.start += self.step 
            return self.start - self.step
        else:
            self.end += self.step
            return self.end - self.step
            

r = MyRange(5, 10, 1)
while r.has_next():
    print(r.get_next(), end=" ")
print()

r = MyRange(5, 10, -2)
while r.has_next():
    print(r.get_next(), end=" ")
print()

