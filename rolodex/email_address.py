from enum import IntEnum
from dataclasses import dataclass


class EmailAddressKind(IntEnum):
    ''' Kind of email address '''
    Unspecified = 0
    Home = 10
    Office = 20


@dataclass(order=True, frozen=True)
class EmailAddress:
    address: str = ''
    kind: EmailAddressKind = EmailAddressKind.Unspecified


#TODO: add validator
def create(address: str, kind: EmailAddressKind) -> EmailAddress:
    return EmailAddress(address, kind)
