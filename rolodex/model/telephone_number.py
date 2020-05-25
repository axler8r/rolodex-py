from enum import IntEnum
from dataclasses import dataclass

from rolodex import logger


class TelephoneNumberKind(IntEnum):
    """ Kind of telephone number """
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
        area_code: str,
        number: str,
        kind=TelephoneNumberKind.Unspecified,
        **kwargs
) -> TelephoneNumber:
    """Create a new telephone number.

    Args:
        area_code (str): Area code.
        number (str): Telephone number.
        kind (TelephoneNumberKind, optional): Kind of telephone number.
            Defaults to TelephoneNumberKind.Unspecified.

    Raises:
        ValueError if area_code or number is None.

    Returns:
        TelephoneNumber: A newly created telephone number.
    """
    country_code = kwargs.get('country_code', None)
    extension = kwargs.get('extension', None)

    logger.trace('{country_code=}', country_code)
    logger.trace('{area_code=}', area_code)
    logger.trace('{number=}', number)
    logger.trace('{extension=}', extension)
    logger.trace('{kind=}', kind)

    if not area_code:
        raise ValueError('Invalid value ({area_code=}).')
    if not number:
        raise ValueError('Invalid value ({number=}).')

    result = TelephoneNumber(
        country_code=country_code,
        area_code=area_code,
        number=number,
        extension=extension,
        kind=kind)
    logger.trace('{result=}', result)
    return result
