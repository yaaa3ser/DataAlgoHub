'''
In our system, items are either simple or complex. A complex
item consists of other items. Those items themselves could consist of other
items, and so on. Items share name, id and price.
Notice, a complex item price is actually the total price of its inner items. 
For example, one of our special chairs consists of 2 left legs (each for $65) and 1 right leg.
This right leg is actually a base (for $30) and an extension (for $70). 
The total price of this special chair is 65+65+30+70 = $230

Implement a simple system that represents this logic
'''

class Item:
    def __init__(self, name, id, price=0):
        self.name = name
        self.id = id
        self._price = price
        self.parts = []
    
    def add_item(self, item):   
        self.parts.append(item)
        
    @property
    def price(self):
        # print(self.name, [part.name for part in self.parts])
        return self._price + sum(item.price for item in self.parts)
                
        
class ComplexItem(Item):
    def __init__(self, name, id):
        super().__init__(name, id)
    
    
left_leg1 = Item('Left Leg', 2, 65)
left_leg2 = Item('Left Leg', 3, 65)

base_leg = Item('Base', 5, 30)
extension_leg = Item('Extension', 6, 70)

right_leg = ComplexItem('Right Leg', 4)
right_leg.add_item(base_leg)
right_leg.add_item(extension_leg)

# print(right_leg.price)

special_chair = ComplexItem('Special Chair', 1)
special_chair.add_item(left_leg1)
special_chair.add_item(left_leg2)
special_chair.add_item(right_leg)

print(special_chair.price)

    