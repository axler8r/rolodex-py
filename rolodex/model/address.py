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
    """Address factory.

    Args:
        street_number (str): Number of the street.
        street (str): Street name.
        city (str): City.
        code (str): Post or Zip code.
        kind (AddressKind, optional): Kind of address.
            Defaults to AddressKind.Unspecified.

    Kwargs:
        unit_number (str): Number of an industrial section business unit.
        unit (str): Name of an industrial section business unit.
        suburb (str): Suburb.
        country (str): Country.

    Returns:
        Address: A newly created address.
    """
    unit_number: str = kwargs.get('unit_number', None)
    unit: str = kwargs.get('unit', None)
    suburb: str = kwargs.get('suburb', None)
    country: str = kwargs.get('country', None)

    logger.trace("{unit_number=}", unit_number)
    logger.trace("{unit=}", unit)
    logger.trace("{street_number=}",  street_number)
    logger.trace("{street=}", street)
    logger.trace("{suburb=}", suburb)
    logger.trace("{city=}", city)
    logger.trace("{code=}", code)
    logger.trace("{country=}", country)
    logger.trace("{kind=}", kind)

    if not street_number:
        raise ValueError('Invalid value ({street_number=}).')
    if not street:
        raise ValueError('Invalid value ({street=}).')
    if not city:
        raise ValueError('Invalid value ({city=}).')
    if not code:
        raise ValueError('Invalid value ({code=}).')
    if kind == AddressKind.Unspecified:
        raise ValueError('Invalid value ({kind=}).')

    result = Address(
        unit_number=unit_number,
        unit=unit,
        street_number=street_number,
        street=street,
        suburb=suburb,
        city=city,
        code=code,
        country=country,
        kind=kind)
    logger.trace("{result=}", result)
    return result
