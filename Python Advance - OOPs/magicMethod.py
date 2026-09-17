# Magic methods = Dunder methods (double underscore) __init__, str, __eq__
#                 They are automatically called by many of Python's built-in operations.
# They allow developens to define or customize the behaviour of objects


class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author} "

    def __eq__(self, other):  #equal
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):  #less than
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages}"

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
# book2 = Book("The Hobbit", "J.R.R. Tolkien", 319)
book2 = Book("Harry Potter and The Philsopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)


# print(book1)  # It will give the memory address

print(book1 == book2) #It checks all the parameters whether they are equal or not
# we can customize using magic method of __eq__ and disregard the num_pages values

print(book2 < book3)

print(book1 + book3)

print("Rowling" in book2)

print(book3['author'])
print(book2['audio'])

