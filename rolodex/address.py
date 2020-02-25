from enum import IntEnum
from dataclasses import dataclass


class AddressKind(IntEnum):
    ''' Kind of telepohone number '''
    Unspecified = 0
    Home = 10
    Office = 20
    Post = 30


@dataclass(order=True, frozen=True)
class Address:
    unit_number: str = None
    unint: str = None
    street_number: str
    street: str
    suburb: str = None
    city: str
    code: str
    country: str = None
    kind: AddressKind = AddressKind.Unspecified
