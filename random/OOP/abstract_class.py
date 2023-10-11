# to create an abstract class we need to import ABC and abstractmethod from abc module

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    @abstractmethod
    def area(self):
        pass
        
    
sh = Shape("Circle") # TypeError: Can't instantiate abstract class Shape with abstract methods area