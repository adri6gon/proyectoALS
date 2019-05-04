#!/usr/bin/env python


from google.appengine.ext import ndb



class Book(ndb.Model):
    type = ndb.TextProperty(indexed= True)
    author = ndb.TextProperty(indexed= True)
    avaliable = ndb.IntegerProperty(indexed= True)
    isbn = ndb.IntegerProperty(indexed= True)
    title = ndb.TextProperty(indexed=True)


def create(book):
    """Creates a new user object, from GAE's user object.

        :param usr: The GAE user object.
        :param level: The desired level.
        :return: A new User object."""
    toret = Book()

    toret.author = book.author()
    toret.avaliable = book.avaliable()
    toret.isbn = book.isbn()
    toret.type = book.type()
    toret.title = book.title()

    return toret


def create_empty_book():
    """Used when there the user is not important."""
    return Book (author="", isbn=0, type="ebook", avaliable=0, title="")


@ndb.transactional
def update(book):
    """Updates a book.

        :param book: The book to update.
        :return: The key of the record.
    """
    return book.put()


def retrieve(book):
    """Reads the user info from the database.

    :param usr: The GAE user object.
    :return: The User retrieved, or a client created appropriately if not found.
    """
    toret = None

    if book:
        found_books = Book.query(Book.isbn == book.isbn)

        if (found_books.count() != 0):
            toret = found_books.iter().next()

    return toret


def getBook(isbn):

    toret = Book.query(Book.isbn == isbn).get()

    return toret
