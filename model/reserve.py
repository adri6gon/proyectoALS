#!/usr/bin/env python


from google.appengine.ext import ndb
import model.book as book_mgt

class Reserve(ndb.Model):
    email = ndb.TextProperty(indexed=True)
    isbn = ndb.IntegerProperty()


def create_empty_reserve():
    """Used when there the user is not important."""
    return Reserve(isbn=0, email="")

@ndb.transactional
def update(reserve):
    """Updates a reserve.

        :param reserve: The reserve to update.
        :return: The key of the record.
    """
    return reserve.put()


def retrieve(book):
    """Reads the user info from the database.
    """
    toret = None
    found_reserve = Reserve.query(Reserve.isbn == book)

    if (found_reserve.count() != 0):
        toret = found_reserve.iter().next()
    return toret


def getReserves(email):
    reserves = Reserve.query(Reserve.email == email)
    toret = list(reserves)
    return toret

def getBooks(email):

    toret = []
    isbns = Reserve.query(Reserve.email == email)
    isbns = list(isbns)

    for el in isbns:
        book = book_mgt.getBook(el.isbn)
        toret.append(book)

    return toret