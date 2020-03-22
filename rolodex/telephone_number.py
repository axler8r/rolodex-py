from enum import IntEnum
from dataclasses import dataclass

from rolodex import logger


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


def create(
        area_code=None,
        number=None,
        kind=TelephoneNumberKind.Unspecified,
        **kwargs
) -> TelephoneNumber:
    coutry_code = kwargs.get('country_code', None)
    extension = kwargs.get('extension', None)

    logger.debug('country_code={}', coutry_code)
    logger.debug('area_code={}', area_code)
    logger.debug('number={}', number)
    logger.debug('extension={}', extension)
    logger.debug('kine={}', kind)

    if not area_code:
        raise ValueError('area_code cannot be empty or None')

    if not number:
        raise ValueError('number cannot be empty or None')

    result: TelephoneNumber = TelephoneNumber(
        coutry_code, area_code, number, extension, kind)
    logger.debug('result={}', result)
    return result
