from abc import ABC, abstractmethod

class Printable(ABC):

    @abstractmethod
    def area(self):
        pass

class Book(Printable):
    def __init__(self, title, author):
        self.title=title
        self.author=author

    def print_info(self):
        print(f"book: {self.title} by {self.author}")

book = Book("The great Gatsby", "F. Scott")
book.print_info()