class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")


my_library = Library()
my_book_1 = Book("To Kill a Mockingbirg", "Harper Lee")
my_book_2 = Book("Silent Spring", "Rachel Carson")
my_library.add_book(my_book_1)
my_library.add_book(my_book_2)
my_library.list_books()