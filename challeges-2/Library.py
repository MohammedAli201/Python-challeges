import Book


class Library :
    def __init__(self):
        self.books =[]

    def add_book(self,book):
        self.books.append(book)
    
    def list_books(self):
        if not self.books:
            return f"NO books in the libarary"
        