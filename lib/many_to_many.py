from datetime import datetime

class Book:
    _all_books = []

    def __init__(self, title):
        self._title = title
        Book._all_books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title should be a string!")
        self._title = value

    @classmethod
    def all_books(cls):
        return cls._all_books

    def contracts(self):
        return [contract for contract in Contract.all_contracts() if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})

class Author:
    _all_authors = []

    def __init__(self, name):
        self._name = name
        Author._all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name should be a string!")
        self._name = value

    def contracts(self):
        return [contract for contract in Contract.all_contracts() if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise Exception("Invalid data provided for signing a contract.")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    @classmethod
    def all_authors(cls):
        return cls._all_authors

class Contract:
    _all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author) or not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise Exception("Invalid data provided for creating a contract.")
        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties
        Contract._all_contracts.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @classmethod
    def contracts_by_date(cls, date=None):
        if date:
            return [contract for contract in cls._all_contracts if contract.date == date]
        else:
            # Sort contracts by date in 'DD/MM/YYYY' format
            return sorted(cls._all_contracts, key=lambda contract: datetime.strptime(contract.date, '%d/%m/%Y'))

    @classmethod
    def all_contracts(cls):
        return cls._all_contracts
