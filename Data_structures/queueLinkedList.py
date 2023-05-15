from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        self.queue.push_back(value)

    def dequeue(self):
        return self.queue.pop_front()

    def is_empty(self):
        return self.queue.head is None


# "============================================="
# "================= TESTING ==================="
# "============================================="

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
print(q.dequeue())
q.enqueue(7)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

