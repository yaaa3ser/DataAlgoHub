class QueueArray:
    def __init__(self, capacity = 1):
        self.capacity = capacity
        self.arr = [None]*capacity
        self.write = 0
        self.read = 0
        
    def is_empty(self):
        return self.write == self.read
    
    def is_full(self):
        return (self.write + 1) % self.capacity == self.read
    
    def enqueue(self, item):
        if self.is_full():
            self.__resize(self.capacity * 2)
        self.arr[self.write] = item
        self.write = (self.write + 1) % self.capacity
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        item = self.arr[self.read]
        self.read = (self.read + 1) % self.capacity
        # Resize if the queue is 1/4 full
        if self.capacity > 1 and (self.write - self.read) <= self.capacity // 4:
            self.__resize(self.capacity // 2)
        return item
    # resize the array to the new capacity and edit the read and write pointers
    def __resize(self, new_capacity):
        new_arr = [None] * new_capacity
        # array is not wrapped around
        if self.read <= self.write:
            # Copy elements straightforwardly
            for i in range(self.read, self.write):
                new_arr[i - self.read] = self.arr[i]
            
            self.arr = new_arr
            self.capacity = new_capacity
            self.write = self.write - self.read
            self.read = 0
        # array is wrapped around
        else:
            # Wrap around and copy elements
            i = 0
            # Copy elements from self.read to the end of the array
            for j in range(self.read, self.capacity):
                new_arr[i] = self.arr[j]
                i += 1
            # Copy elements from the beginning to self.write
            for j in range(self.write):
                new_arr[i] = self.arr[j]
                i += 1
            
            self.arr = new_arr
            self.capacity = new_capacity
            self.write = i
            self.read = 0
            
            
    def retrieve(self):
        for i in range(self.read, self.write):
            print(self.arr[i], end = " ")
        print()
    
# "============================================="
# "================= TESTING ==================="
# "============================================="

q = QueueArray(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.write, q.read, q.capacity)
print(q.dequeue())
# print(q.dequeue())
print(q.write, q.read, q.capacity)
# print(q.dequeue())
# print(q.write, q.read, q.capacity)

q.enqueue(4)
q.enqueue(5)
print(q.write, q.read, q.capacity)
q.enqueue(6)
# q.enqueue(7)
# print(q.is_full())
# q.enqueue(8)
# q.retrieve()
print(q.write, q.read, q.capacity)
print(q.is_full())
q.enqueue(7)
print(q.write, q.read, q.capacity)
# q.retrieve()
q.dequeue()
q.dequeue()
q.dequeue()
q.retrieve()
print(q.write, q.read, q.capacity)

