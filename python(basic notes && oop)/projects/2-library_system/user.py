class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def borrow(self, book):
        self.borrowed_books.append(book)

    def is_borrowed(self, book):
        for mybook in self.borrowed_books:
            if mybook.id == book.id:
                return True
        return False


    def return_book(self, book):
        for idx, mybook in enumerate(self.borrowed_books):
            if mybook.id == book.id:
                del self.borrowed_books[idx]
                break

    def simple_repr(self, is_detailed = False):
        ret = f'User name: {self.name:15} - id: {self.id}'
        if is_detailed and self.borrowed_books:
            ret += '\n\tBorrowed books:\n'
            for book in self.borrowed_books:
                ret += f'\t{str(book)}\n'
        return ret

    def __repr__(self):
        return self.simple_repr(True)
