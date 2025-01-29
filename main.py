class Book:
    def __init__(self, title, author, isbn, available=True):
        """
        This class represents a book in the library.
        
        :param title: The title of the book.
        :param author: The author of the book.
        :param isbn: The ISBN number of the book.
        :param available: Availability status of the book (True if available).
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"Book(title: '{self.title}', author: '{self.author}', ISBN: '{self.isbn}', available: {self.available})"


class User:
    def __init__(self, username, user_id):
        """
        This class represents a user of the library.
        
        :param username: The name of the user.
        :param user_id: The ID of the user.
        """
        self.username = username
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Allows the user to borrow a book if it's available.
        
        :param book: The book to borrow.
        :return: True if the book was borrowed successfully, otherwise False.
        """
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.username} borrowed '{book.title}' successfully.")
            return True
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")
            return False

    def return_book(self, book):
        """
        Allows the user to return a borrowed book.
        
        :param book: The book to return.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.username} returned '{book.title}' successfully.")
        else:
            print(f"{self.username} didn't borrow '{book.title}'.")

    def list_borrowed_books(self):
        """
        Lists all the books currently borrowed by the user.
        """
        if self.borrowed_books:
            print(f"{self.username} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.username} has not borrowed any books.")


class Library:
    def __init__(self):
        """
        This class represents the entire library.
        It contains a collection of books and users.
        """
        self.books = []
        self.users = []

    def add_book(self, book):
        """
        Adds a new book to the library's collection.
        
        :param book: The book to add.
        """
        self.books.append(book)
        print(f"'{book.title}' by {book.author} has been added to the library.")

    def register_user(self, user):
        """
        Registers a new user in the library system.
        
        :param user: The user to register.
        """
        self.users.append(user)
        print(f"User '{user.username}' has been registered.")

    def list_available_books(self):
        """
        Lists all the available books in the library.
        """
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books are currently available in the library.")

    def search_book_by_title(self, title):
        """
        Searches for a book by its title.
        
        :param title: The title of the book to search for.
        :return: The book if found, otherwise None.
        """
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        print(f"Book with title '{title}' not found.")
        return None

    def search_book_by_author(self, author):
        """
        Searches for books by a specific author.
        
        :param author: The author to search for.
        :return: List of books by the author.
        """
        books_by_author = [book for book in self.books if author.lower() in book.author.lower()]
        if books_by_author:
            print(f"Books by '{author}':")
            for book in books_by_author:
                print(f"- {book.title}")
        else:
            print(f"No books found by author '{author}'.")


# Example usage:

# Create a library
library = Library()

# Add books to the library
book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", isbn="9780743273565")
book2 = Book(title="1984", author="George Orwell", isbn="9780451524935")
book3 = Book(title="To Kill a Mockingbird", author="Harper Lee", isbn="9780061120084")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register users
user1 = User(username="john_doe", user_id=1)
user2 = User(username="jane_smith", user_id=2)

library.register_user(user1)
library.register_user(user2)

# List available books
library.list_available_books()

# User borrows a book
user1.borrow_book(book1)

# List borrowed books
user1.list_borrowed_books()

# User returns a book
user1.return_book(book1)

# List available books again
library.list_available_books()

# Search books by title
library.search_book_by_title("1984")

# Search books by author
library.search_book_by_author("Harper Lee")
