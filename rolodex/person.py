from enum import IntEnum
from dataclasses import dataclass
from typing import Set
from rolodex.email_address import EmailAddress
from rolodex.address import Address
from rolodex.telphone_number import TelephoneNumber
from rolodex.handle import Handle

import arrow


class Gender(IntEnum):
    Unspecified = 0
    Female = 10
    Male = 20


@dataclass(order=True, frozen=True)
class Person:
    given_names: list = []
    family_name: str = ""
    #birth_date: arrow 
    gender: Gender = Gender.Unspecified
    email_addresses: Set[EmailAddress]
    telephone_number: Set[TelephoneNumber]
    handles: Set[Handle]
    addresses: Set[Address]
