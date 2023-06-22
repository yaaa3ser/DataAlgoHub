class HashTable:
    def __init__(self):
        self.slots = 10
        self.load_factor = 0.75 
        self.length = 0
        self.table = [None] * self.slots


    def add(self,key,value):
        self.length += 1
        index = key % self.slots # the hash function.
        while self.table[index] is not None:
            if self.table[index] == key: # if the key already exists, update the value
                self.length -= 1
                return
            index = (index+1) % self.slots
        tuple = (key,value)
        self.table[index] = tuple
        if self.length / float(self.slots) >= self.load_factor: # if the length of the table is greater than .75 of the slots, resize the table
            self.resize()


    def get(self,key):
        index = self.find_item(key)
        return self.table[index][1]


    def remove(self,key):
        index = self.find_item(key)
        self.table[index] = "Deleted" # mark the item as deleted instead of removing it to avoid breaking the search


    def resize(self):
        self.slots *= 2
        self.length = 0
        old_table = self.table
        self.table = [None] * self.slots
        for tuple in old_table:
            if tuple is not None:
                self[tuple[0]] = tuple[1]


    def find_item(self,key):
        index = key % self.slots # the hash function.
        if self.table[index] == None:
            raise KeyError
        if self.table[index][0] != key: # if the key is not in the hashed index, search the next index
            original_key = index
            while self.table[index][0] != key:
                index = (index+1) % self.slots
                if self.table[index] is None:
                    raise KeyError
                if index == original_key: # if the key remains the same after wrapping around the table
                    raise KeyError
        return index
    
    
# Test
dic = HashTable()
dic.add(1,1)
dic.add(4,2)
dic.add(3,3)
dic.add(14,4)
dic.add(24,5)
print(dic.find_item(24))

