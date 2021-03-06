"""
dataclass_csv
~~~~~~~~~~~~~

The dataclass_csv is a library that parses every row of a CSV file into
`dataclasses`. It takes advantage of `dataclasses` features to perform
data validation and type conversion.

Basic Usage:

    >>> from dataclasses import dataclass
    >>> from dataclass_csv import DataclassReader


    >>> @dataclass
    >>> class User:
    >>>    firstname: str
    >>>    lastname: str
    >>>    age: int

    >>> with open('users.csv') as f:
    >>>    reader = DataclassReader(f, User)
    >>>    users = list(reader)
    >>>    print(users)
    [
        User(firstname='User1', lastname='Test', age=23),
        User(firstname='User2', lastname='Test', age=34)
    ]


:copyright: (c) 2018 by Daniel Furtado.
:license: BSD, see LICENSE for more details.
"""


from .dataclass_reader import DataclassReader
from .decorators import dateformat, accept_whitespaces
from .exceptions import CsvValueError


__all__ = [
    'DataclassReader',
    'dateformat',
    'accept_whitespaces',
    'CsvValueError',
]
