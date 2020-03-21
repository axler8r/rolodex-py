from enum import IntEnum
from dataclasses import dataclass


class TelephoneNumberKind(IntEnum):
    ''' Kind of telepohone number '''
    Unspecified = 0
    Home = 10
    Office = 20
    Mobile = 30
    Fax = 40


@dataclass(order=True, frozen=True)
class TelephoneNumber:
    country_code: str
    area_code: str
    number: str
    extension: str
    kind: TelephoneNumberKind = TelephoneNumberKind.Unspecified
