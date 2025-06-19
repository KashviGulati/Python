from datetime import datetime, timedelta

class Book:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.available = True

class Customer:
    def __init__(self, name):
        self.name = name
        self.borrowed = None
        self.borrow_date = None
        self.due_date = None

    def borrow_book(self, book):
        if book.available:
            self.borrowed = book
            self.borrow_date = datetime.now()
            self.due_date = self.borrow_date + timedelta(days=10)
            book.available = False
            print(f"{self.name} borrowed '{book.title}', due on {self.due_date.date()}")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self):
        if self.borrowed:
            return_date = datetime.now()
            delay = (return_date - self.due_date).days
            fine = 10 * max(0, delay)
            print(f"{self.name} returned '{self.borrowed.title}'. Fine: ₹{fine}")
            self.borrowed.available = True
            self.borrowed = None
            self.borrow_date = None
            self.due_date = None
        else:
            print("No book to return.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, genre):
        book = Book(title, genre)
        self.books.append(book)
        print(f"Added '{title}' under genre '{genre}'.")

    def list_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} ({book.genre})")


library = Library()
library.add_book("The diary of a young girl", "Auto Biography")
library.add_book("Anxious People", "Fiction")
library.add_book("Pride and prejudice", "Literary Fiction")
library.add_book("The immortals of Meluha", "Historical Fiction")

library.list_books()
