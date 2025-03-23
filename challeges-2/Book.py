

class Book :
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def borrow(self):
        if self.is_available:
            self.is_available =False
            return f"You have borrowed : {self.title}"
        return f" {self.title} is currently unavailable"
    
    def return_book(self):
        self.is_available =True
        return f"{self.title} has been retyrned and now is available"
    def display_info (self):
        status = "available " if self.is_available else "Not Available"
        return f"Book : {self.title} by {self.author} | status :{status}"


class Library :
    def __init__(self):
        self.books =[]

    def add_book(self,book):
        self.books.append(book)
    
    def list_books(self):
        if not self.books:
            return f"NO books in the libarary"
        return "\n".join(book.display_info() for book in self.books)

    def borrow_book (self, title):
        for book in self.books:
            if book.title.lower()== title.lower():
                return book.borrow()
        return f"Book {title} npt found in the libarary"
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f"Book '{title}' not found in the library."

# Creating the library
library = Library()

# Adding books to the library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Displaying all books
print("\nLibrary Books:")
print(library.list_books())

# Borrowing a book
print("\n" + library.borrow_book("1984"))

# Displaying books after borrowing
print("\nLibrary Books after borrowing '1984':")
print(library.list_books())

# Returning a book
print("\n" + library.return_book("1984"))

# Displaying books after returning
print("\nLibrary Books after returning '1984':")
print(library.list_books())
