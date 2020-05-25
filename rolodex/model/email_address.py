from enum import IntEnum
from dataclasses import dataclass

from rolodex import logger


class EmailAddressKind(IntEnum):
    """ Kind of email address """
    Unspecified = 0
    Home = 10
    Office = 20


@dataclass(order=True, frozen=True)
class EmailAddress:
    address: str
    kind: EmailAddressKind = EmailAddressKind.Unspecified


def create(
        address: str,
        kind: EmailAddressKind = EmailAddressKind.Unspecified
) -> EmailAddress:
    """EmailAddress factory.

    Keyword Arguments:
        address (str): Email address.
        kind (EmailAddressKind, optional): Kind of email address.
             Defaults to TelephoneNumberKind.Unspecified.

    Returns:
        EmailAddress: Newly created EmailAddress.
    """
    logger.trace("{address=}", address)
    logger.trace("{kind=}", kind)

    if not address:
        raise ValueError('Invalid value ({address=}).')

    result = EmailAddress(address=address, kind=kind)
    logger.trace("{result=}", result)
    return result
