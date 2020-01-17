from collections import namedtuple
from datetime import datetime
from operator import attrgetter, itemgetter

Book = namedtuple('Book', 'title authors pages published')

books = [
    Book(title="Python Interviews",
         authors="Michael Driscoll",
         pages=366,
         published="2018-02-28"),
    Book(title="Python Cookbook",
         authors="David Beazley, Brian K. Jones",
         pages=706,
         published="2013-05-10"),
    Book(title="The Quick Python Book",
         authors="Naomi Ceder",
         pages=362,
         published="2010-01-15"),
    Book(title="Fluent Python",
         authors="Luciano Ramalho",
         pages=792,
         published="2015-07-30"),
    Book(title="Automate the Boring Stuff with Python",
         authors="Al Sweigart",
         pages=504,
         published="2015-04-14"),
]

# all functions return books sorted in ascending order.


def sort_books_by_len_of_title(books=books):
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    books.sort(key=lambda x: len(x.title))
    return books


def sort_books_by_first_authors_last_name(books=books):
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    return sorted(books, key=lambda x: x.authors.split(',')[0].split()[-1])


def sort_books_by_number_of_page(books=books):
    """
    Expected last book in list:
    Fluent Python
    """
    return sorted(books, key=attrgetter("pages"))


def sort_books_by_published_date(books=books):
    """
    Expected last book in list:
    Python Interviews
    """
    return sorted(books, key=lambda x: datetime.strptime(x.published,"%Y-%m-%d"))
