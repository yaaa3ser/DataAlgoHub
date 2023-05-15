from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        self.stack.push_front(value)

    def pop(self):
        return self.stack.pop_front()

    def is_empty(self):
        return self.stack.head is None

    def peek(self):
        if self.stack.head is None:
            return "Stack is empty"
        return self.stack.head.data

    def size(self):
        return self.stack.size
    
    def retrieve(self):
        self.stack.retrieve()
        
    
# "============================================="
# "================= TESTING ==================="
# "============================================="  
s = Stack()
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