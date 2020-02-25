from enum import IntEnum
from dataclasses import dataclass


class EmailAddressKind(IntEnum):
    ''' Kind of telepohone number '''
    Unspecified = 0
    Home = 10
    Office = 20


@dataclass(order=True, frozen=True)
class EmailAddress:
    address: str = ''
    kind: EmailAddressKind = EmailAddressKind.Unspecified
