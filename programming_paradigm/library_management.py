class Book:
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} - {'Available' if self.is_available else 'Checked Out'}"
    
    def check_out(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        return False
    
class Library:
    def __init__(self):
        self.books = []
        
        
    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def book_availability(self, title):
        book = self.find_book(title)
        if book:
            return book.is_available
        return None


    def list_available_books(self):
        for book in self.books:
            if book.is_available:
                print(book)


    def check_out_book(self, title):
        book = self.find_book(title)
        if book and book.is_available:
            book.is_available = False
            return True
        return False
    
    def return_book(self, title):
        for book in self.books:  # Assuming self.books is a list of Book instances
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print(f"Book '{title}' has been returned.")
                else:
                    print(f"Book '{title}' is already available.")
                return
        print(f"Book '{title}' not found in the library.")
