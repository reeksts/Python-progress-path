class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book ('{self.name}', '{self.book_type}', weighing {self.weight})>"

    @classmethod
    def hardcover(cls, name, book_weight):
        return cls(name, cls.TYPES[0], book_weight+100)

    def paperback(cls, name, book_weight):
        return cls(name, cls.TYPES[1], book_weight+100)

book1 = Book("book", "nice", 100)
print(book1)

book2 = Book.hardcover("Harry", 1000)
print(book2)

book3 = Book.hardcover("Marry", 20)
print(book3)
