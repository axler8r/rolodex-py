from dataclasses import dataclass
from enum import IntEnum

from rolodex import logger


class AddressKind(IntEnum):
    """ Kind of telephone number """
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
        street_number: str,
        street: str,
        city: str,
        code: str,
        kind: AddressKind = AddressKind.Unspecified,
        **kwargs
) -> Address:
    unit_number: str = kwargs.get('unit_number', None)
    unit: str = kwargs.get('unit', None)
    suburb: str = kwargs.get('suburb', None)
    country: str = kwargs.get('country', None)

    logger.trace("unit_number={}", unit_number)
    logger.trace("unit={}", unit)
    logger.trace("street_number={}",  street_number)
    logger.trace("street={}", street)
    logger.trace("suburb={}", suburb)
    logger.trace("city={}", city)
    logger.trace("code={}", code)
    logger.trace("country={}", country)
    logger.trace("kind={}", kind)

    result = Address(unit_number, unit, street_number, street,
                     suburb, city, code, country, kind)
    logger.trace("result={}", result)
    return result
