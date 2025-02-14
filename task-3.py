class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Year Published: {self.year_published}\n")

book1 = Book("The Princess and the Pea", "Hans Christian Andersen", 1835)
book2 = Book("A Little Princess", "Frances Hodgson Burnett", 1905)
book3 = Book("Part Time Princess", "Deborah Underwood", 2013)

book1.describe()
book2.describe()
book3.describe()