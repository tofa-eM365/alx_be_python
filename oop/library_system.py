class Book:
    """Base class for a book."""

    def __init__(self, title, author):
        """Initialize a new Book instance."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class for an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize a new EBook instance."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class for a printed book."""

    def __init__(self, title, author, page_count):
        """Initialize a new PrintBook instance."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class to manage a collection of books."""

    def __init__(self):
        """Initialize the Library with an empty book list."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
