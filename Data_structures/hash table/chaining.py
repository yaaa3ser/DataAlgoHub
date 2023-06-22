
class ListNode:
    def __init__(self, key=None, val=None):
        self.pair = (key,val)
        self.next = None


class HashTable:
    def __init__(self):
        self.slots = 10
        self.head = [None] * self.slots

    def add(self, key, value):
        index = key % self.slots  # the hash function.
        if self.head[index] == None:  # if the hashed index is empty
            self.head[index] = ListNode(key, value)
            return
        
        current_index = self.head[index]
        while True:
            if current_index.pair[0] == key:  # if the key already exists, update the value
                current_index.pair = (key,value)
                return
            if current_index.next == None: # if the key does not exist, add it to the end of the list
                break
            current_index = current_index.next
        current_index.next = ListNode(key,value)


    def get(self,key):
        index = key%self.slots
        current_index = self.head[index]
        while current_index:
            if current_index.pair[0] == key:
                return current_index.pair[1]
            current_index=current_index.next

        return -1

    def remove(self,key):
        index = key%self.slots
        current_index = prev = self.head[index]  # prev is the previous node of current_index
        if current_index == None:
            return
        if current_index.pair[0] == key: # if the key is the first element in the list
            self.head[index] = current_index.next
        else:
            current_index = current_index.next
            while current_index:
                if current_index.pair[0] == key:
                    prev.next = current_index.next
                    break

                else:
                    current_index,prev = current_index.next,prev.next



dic = HashTable()
dic.add(1,1)
dic.add(4,2)
dic.add(3,3)
dic.add(14,4)
dic.add(24,5)
print(dic.get(14))