from enum import IntEnum
from dataclasses import dataclass

from rolodex import logger


class AddressKind(IntEnum):
    ''' Kind of telepohone number '''
    Unspecified = 0
    Home = 10
    Office = 20
    Post = 30


@dataclass(order=True, frozen=True)
class Address:
    unit_number: str
    unit: str
    street_number: str
    street: str
    suburb: str
    city: str
    code: str
    country: str
    kind: AddressKind = AddressKind.Unspecified


def create(
        street_number: str = None,
        street: str = None,
        city: str = None,
        code: str = None,
        kind: AddressKind = AddressKind.Unspecified,
        **kwargs
) -> Address:
    unit_number: str = kwargs.get('unit_number', None)
    unit: str = kwargs.get('unit', None)
    suburb: str = kwargs.get('suburb', None)
    country: str = kwargs.get('country', None)

    logger.debug("unit_number={}", unit_number)
    logger.debug("unit={}", unit)
    logger.debug("street_number={}",  street_number)
    logger.debug("street={}", street)
    logger.debug("suburb={}", suburb)
    logger.debug("city={}", city)
    logger.debug("code={}", code)
    logger.debug("country={}", country)
    logger.debug("kind={}", kind)

    if not street_number:
        raise ValueError("street_number cannot be empty or None")

    if not street:
        raise ValueError("steet cannot be empty or None")

    if not city:
        raise ValueError("city cannot be empty or None")

    if not code:
        raise ValueError("code cannot be empty or None")

    result = Address(unit_number, unit, street_number, street,
                     suburb, city, code, country, kind)
    logger.debug("result={}", result)
    return result
