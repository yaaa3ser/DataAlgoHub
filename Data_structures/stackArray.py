from arrray import DynamicArray
class StackArray:
    def __init__(self):
        self.stack = DynamicArray()
    
    def push(self, item):
        self.stack.push(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack.at(self.stack.size - 1)
    
    def is_empty(self):
        return self.stack.is_empty()
    
    def size(self):
        return self.stack.size
    
    def retrieve(self):
        self.stack.retrieve()
    
    def __str__(self):
        return str(self.stack)
    

# "============================================="
# "================= TESTING ==================="
# "============================================="
s = StackArray()
# print(s.is_empty())
# print(s.size())
# s.push(1)
# print(s.size())
# s.pop()
# s.push(2)  
# s.retrieve()

s.push(1)
s.push(2)
s.push(3)
print(s.peek())
s.retrieve()
s.pop()
s.retrieve()
print(s.peek()) 
s.pop() 
s.retrieve()
print(s.peek())
s.pop()
s.retrieve()
print(s.peek())
print(s.size())