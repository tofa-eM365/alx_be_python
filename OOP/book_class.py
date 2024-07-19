class Book:
    """A class to represent a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Initialize a new Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to handle the deletion of a Book instance."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a user-friendly string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a string that would recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
