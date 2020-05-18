from dataclasses import dataclass
from datetime import date
from enum import IntEnum
from typing import Set
from loguru import logger

import arrow

from rolodex.email_address import EmailAddress
from rolodex.address import Address
from rolodex.telephone_number import TelephoneNumber
from rolodex.handle import Handle


GivenNames = Set[str]
TelephoneNumbers = Set[TelephoneNumber]
EmailAddresses = Set[EmailAddress]
Addresses = Set[Address]
Handles = Set[Handle]


class Gender(IntEnum):
    Unspecified = 0
    Female = 10
    Male = 20


@dataclass(order=True, frozen=True)
class Person:
    given_names: GivenNames
    family_name: str
    birth_date: date
    telephone_numbers: TelephoneNumbers
    email_addresses: EmailAddresses
    addresses: Addresses
    handles: Handles
    gender: Gender = Gender.Unspecified


# TODO: establish which paramaters are optional and move it into **kwargs
def create(
        given_names: GivenNames,
        family_name: str,
        birth_date: str,
        gender: Gender,
        telephone_numbers: TelephoneNumbers,
        email_addresses: EmailAddresses,
        addresses: Addresses,
        handles: Handles
) -> Person:
    logger.trace("given_names={}", given_names)
    logger.trace("family_name={}", family_name)
    logger.trace("birth_date={}", birth_date)
    logger.trace("gender={}", gender)
    logger.trace("telephone_numbers={}", telephone_numbers)
    logger.trace("email_addresses={}", email_addresses)
    logger.trace("addresses={}", addresses)
    logger.trace("hanldes={}", handles)

    result = Person(
        given_names=given_names,
        family_name=family_name,
        birth_date=_date(birth_date),
        gender=gender,
        telephone_numbers=telephone_numbers,
        email_addresses=email_addresses,
        addresses=addresses,
        handles=handles)
    logger.trace("result={}")
    return result


def _date(date: str) -> date:
    logger.trace("date={}", date)

    if not date:
        raise ValueError("date cannot be empty or None")

    # TODO: catch exception and return meaningful value
    try:
        result = arrow.get(date).date()
    except ValueError as e:
        logger.exception(e)
        raise e
    logger.trace("result={}", result)
    return result
