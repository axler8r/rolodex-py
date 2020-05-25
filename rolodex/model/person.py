from dataclasses import dataclass
from datetime import date
from enum import IntEnum
from typing import Set

import arrow

from rolodex import logger
from rolodex.model.email_address import EmailAddress
from rolodex.model.address import Address
from rolodex.model.telephone_number import TelephoneNumber
from rolodex.model.handle import Handle


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


def create(
        given_names: GivenNames,
        family_name: str,
        telephone_numbers: TelephoneNumbers,
        email_addresses: EmailAddresses,
        **kwargs
) -> Person:
    """Person factory.

    Args:
        given_names (GivenNames): A person given names.
        family_name (str): A person's family names.
        telephone_numbers (TelephoneNumbers): A set of TelephoneNumbers.
        email_addresses (EmailAddresses): A set of EmailAddresses.

    Kwargs:
        birth_date (str): Person's birth date.
        gender (Gender): A Person's gender.
        addresses (Addresses): Physical locations.
        handles (Handles): Social media identities.

    Returns:
        Person: A newly generated Person.
    """
    birth_date: str = kwargs.get('birth_date', None)
    gender: Gender = kwargs.get('gender', Gender.Unspecified)
    addresses: Addresses = kwargs.get('addresses', {})
    handles: Handles = kwargs.get('handles', {})

    logger.trace("{given_names=}", given_names)
    logger.trace("{family_name=}", family_name)
    logger.trace("{birth_date=}", birth_date)
    logger.trace("{gender=}", gender)
    logger.trace("{telephone_numbers=}", telephone_numbers)
    logger.trace("{email_addresses=}", email_addresses)
    logger.trace("{addresses=}", addresses)
    logger.trace("{hanldes=}", handles)

    if not given_names:
        raise ValueError('Invalid value ({given_names=}).')
    if not family_name:
        raise ValueError('Invalid value ({family_name=}).')
    if not telephone_numbers:
        raise ValueError('Invalid value ({telephone_numbers=}).')
    if not email_addresses:
        raise ValueError('Invalid value ({email_addresses=}).')

    result = Person(
        given_names=given_names,
        family_name=family_name,
        birth_date=_date(birth_date),
        gender=gender,
        telephone_numbers=telephone_numbers,
        email_addresses=email_addresses,
        addresses=addresses,
        handles=handles)
    logger.trace("{result=}")
    return result


def _date(date: str) -> date:
    logger.trace("date={}", date)

    if not date:
        raise ValueError("date cannot be empty or None")

    try:
        result = arrow.get(date).date()
    except ValueError as e:
        logger.exception(e)
        raise e
    logger.trace("result={}", result)
    return result
