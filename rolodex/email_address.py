from enum import IntEnum
from dataclasses import dataclass

from loguru import logger


class EmailAddressKind(IntEnum):
    """ Kind of email address """
    Unspecified = 0
    Home = 10
    Office = 20


@dataclass(order=True, frozen=True)
class EmailAddress:
    address: str
    kind: EmailAddressKind = EmailAddressKind.Unspecified


# TODO: add validator
def create(
        address: str = None,
        kind: EmailAddressKind = EmailAddressKind.Unspecified
) -> EmailAddress:
    logger.trace("address={}", address)
    logger.trace("kind={}", kind)

    if not address:
        raise ValueError("address can not be empty to None")
    # TODO: validate the email address format (email validator)

    result = EmailAddress(address, kind)
    logger.trace("result={}", result)
    return result
