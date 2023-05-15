class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def retrieve(self):
        current = self.head
        while current != None:
            print(current.data, end=" ")
            current = current.next
        print()
    
    def size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0 # or self.head == None
    
    # returns the value of the nth item (starting at 0 for first)
    def value_at(self, index):
        if index >= self.size or index < 0:
            return None
        else:
            current = self.head
            for i in range(index):
                current = current.next
            return current.data
        
    # adds an item to the front of the list
    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    # remove front item and return its value
    def pop_front(self):
        if self.is_empty():
            return None
        else:
            current = self.head
            self.head = current.next
            self.size -= 1
            return current.data
        
    # adds an item at the end
    def push_back(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    
    # removes end item and returns its value
    def pop_back(self):
        if self.is_empty():
            return None
        if self.size == 1:
            self.tail = None
            return self.pop_front()
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
            self.size -= 1
            return current.data
    
    # get value of front item
    def front(self):
        return self.head.data
    
    # get value of end item
    def back(self):
        return self.tail.data
    
    # insert value at index, so current item at that index is pointed to by new item at index
    def insert(self, index, value):
        if index > self.size or index < 0:
            return None
        elif index == 0:
            self.push_front(value)
        elif index == self.size:
            self.push_back(value)
        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            # cnt = 0
            # while cnt < index-1:
            #     current = current.next
            #     cnt+=1
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
            self.size += 1
    
    # removes node at given index
    def erase(self, index):
        if index >= self.size or index < 0:
            return None
        elif index == 0:
            self.pop_front()
        elif index == self.size-1:
            self.pop_back()
        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            current.next = current.next.next
            self.size -= 1
    
    # removes the first item in the list with this value
    def remove_value(self, value):
        current = self.head
        if current.data == value:
            self.pop_front()
            if self.size == 0:
                self.tail = None
            return
        while current.next != None:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
        return None
    
    # reverses the list
    def reverse(self):
        if self.size == 0:
            return
        current = self.head
        prev = None
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    # returns the value of the node at nth position from the end of the list
    def value_n_from_end(self, n):
        if n >= self.size or n < 0:
            return None
        else:
            current = self.head
            for i in range(self.size-n-1):
                current = current.next
            return current.data
    
"============================================="
"================= TESTING ==================="
"============================================="        
ll = LinkedList()
# print(ll.is_empty())
# print(ll.size)
# print(ll.value_at(0))
# ll.push_front(1)
# print(ll.is_empty())
# print(ll.size)
# print(ll.value_at(0))
# ll.retrieve()
# ll.push_front(2)
# ll.push_front(3)
# ll.retrieve()
# print(ll.value_at(0))
# print(ll.value_at(1))
# print(ll.value_at(2))
# print(ll.value_at(3))
# ll.retrieve()
# print(ll.pop_front())
# ll.retrieve()
# print(ll.pop_front())
# ll.retrieve()
# print(ll.pop_front())
# ll.retrieve()

# ll.push_back(1)
# ll.push_back(2)
# ll.push_back(5)
# ll.retrieve()
# ll.pop_back()
# ll.retrieve()
# ll.pop_front()
# ll.retrieve()
# print(ll.size)
# print(ll.is_empty())
# ll.pop_back()
# print(ll.is_empty())


# ll.push_back(1)
# ll.push_back(2)
# ll.push_back(3)
# ll.insert(1, 5)
# ll.retrieve()
# ll.reverse()
# ll.retrieve()
# print(ll.value_n_from_end(1))
# ll.remove_value(2)
# ll.remove_value(1)
# ll.remove_value(3)
# ll.retrieve()
# print(ll.size)
# print(ll.head, ll.tail)