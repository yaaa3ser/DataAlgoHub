class DynamicArray:
    def __init__(self, capacity = 1):
        self.size = 0
        self.capacity = capacity
        self.arr = [None]
    
    def retrieve(self):
        for i in range(self.size):
            print(self.arr[i], end = " ")
        print()
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def at(self, index):
        if index < 0 or index >= self.size:
            return "Index out of bounds"
        return self.arr[index]
    # private method
    def __resize(self, new_capacity):
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity
    
    def push(self, item):
        if self.is_full():
            self.__resize(self.capacity * 2)
        self.arr[self.size] = item
        self.size+=1
        
    def insert(self, index, item):
        if self.is_full():
            self.__resize(self.capacity * 2)
        if index < 0 or index >= self.size:
            return "Index out of bounds"
        for i in range (self.size, index, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[index] = item
        self.size+=1
    # remove from end, return value
    def pop(self):
        if self.is_empty():
            return "Array is empty"
        self.size-=1
        if self.size < self.capacity // 4:
            self.__resize(self.capacity // 2)
        return self.arr[self.size]
    # delete item at index, shifting all trailing elements left
    def delete(self, index):
        if self.is_empty():
            return "Array is empty"
        if index < 0 or index >= self.size:
            return "Index out of bounds"
        for i in range(index, self.size-1):
            self.arr[i] = self.arr[i+1]
        self.size-=1
    # looks for value and removes index holding it (even if in multiple places)
    def remove(self, item):
        if self.is_empty():
            return "Array is empty"
        i = 0
        while i < self.size:
            if self.arr[i] == item:
                self.delete(i)
                # don't increment i here, since the next item may also be the same
            else:
                i += 1
        
    # looks for value and returns first index with that value, -1 if not found
    def find(self, item):
        if self.is_empty():
            return "Array is empty"
        for i in range(self.size):
            if self.arr[i] == item:
                return i
        return -1
    
    
# "============================================="
# "================= TESTING ==================="
# "============================================="
# arr = DynamicArray()
# print(arr.size)
# print(arr.capacity)
# print(arr.is_empty())
# arr.push(5)
# arr.push(4)
# print(arr.capacity)
# print(arr.is_full())
# arr.push(7)
# print(arr.capacity)
# print(arr.is_full())
# arr.retrieve()
# arr.insert(1, 6)
# arr.retrieve()
# arr.insert(3, 64)
# arr.retrieve()
# arr.pop()
# arr.retrieve()
# assert (arr.at(4) == "Index out of bounds") 
# arr.delete(0)
# arr.retrieve()
# arr.push(3)
# arr.push(3)
# arr.push(3)
# arr.retrieve()
# arr.remove(3)
# arr.retrieve()
# print(arr.find(3))
# print(arr.find(6))
