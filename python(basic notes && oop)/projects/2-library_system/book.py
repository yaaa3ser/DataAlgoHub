class Book:
    def __init__(self, name, id, total_quantity):
        self.name = name
        self.id = id
        self.total_quantity = total_quantity
        self.total_borrowed = 0

    def borrow(self):
        if self.total_quantity == self.total_borrowed:
            return False
        self.total_borrowed += 1
        return True

    def return_copy(self):
        assert self.total_borrowed > 0
        self.total_borrowed -= 1

    def __repr__(self):
        return f'Book name: {self.name:20} - id: {self.id} - total quantity: {self.total_quantity} - ' \
               f'total borrowed: {self.total_borrowed}'
