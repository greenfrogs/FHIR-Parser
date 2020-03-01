"""
Patient
=======
The Patient object containing information about a specific patient
"""

import datetime
from typing import List, Union, Optional, Dict, Tuple


class Extension:
    """An extension consisting of a url and a value"""
    def __init__(self, url: str, value: Union[str, float]):
        self.url: str = url
        self.value: Union[str, float] = value

    def __eq__(self, o: object) -> bool:
        if type(o) != Extension:
            return False
        return self.__dict__ == o.__dict__

    def __str__(self) -> str:
        return self.url + ': ' + str(self.value)

class Identifier:
    """An identifier consiting of a system, code, display, and value"""
    def __init__(self, system: str, code: str, display: str, value: str):
        self.system: str = system
        self.code: str = code
        self.display: str = display
        self.value: str = value

    def __eq__(self, o: object) -> bool:
        if type(o) != Identifier:
            return False
        return self.__dict__ == o.__dict__

    def __str__(self) -> str:
        return self.display + ' ' + self.value


class Name:
    """The name consisting of family, given (can be multiple), and prefix (can be multiple)"""
    def __init__(self, family: str, given: List[str], prefix: List[str]):
        self.family: str = family
        self.given_list: List[str] = given
        self.prefix_list: List[str] = prefix

    @property
    def full_name(self) -> str:
        """
        Returns: The full name of a patient
        """
        return ' '.join(self.prefix_list) + ' ' + ' '.join(self.given_list) + ' ' + self.family

    @property
    def given(self) -> str:
        """
        Returns: The given names of a patient joined with a space

        """
        return ' '.join(self.given_list)

    @given.setter
    def given(self, value: str):
        self.given_list = value.split(' ')

    @property
    def prefix(self) -> str:
        """
        Returns: The prefix's of a patient joined with a space

        """
        return ' '.join(self.prefix_list)

    @prefix.setter
    def prefix(self, value: str):
        self.prefix_list = value.split(' ')

    def __str__(self) -> str:
        return self.full_name


class Telecom:
    """The telecommunication method consisting of the system, phone number, and use (for example home/work)"""
    def __init__(self, system: str, number: str, use: str):
        self.system: str = system
        self.number: str = number
        self.use: str = use

    def __str__(self) -> str:
        return self.use + ' ' + self.system + ': ' + self.number


class Address:
    """The address consisting of multiple lines, city, state, postal code, country, and if applicable an extension
    containing the latitude and longitude"""
    def __init__(self, lines: List[str], city: str, state: str, postal_code: str, country: str,
                 extensions: List[Extension]):
        self.lines: List[str] = lines
        self.city: str = city
        self.state: str = state
        self.postal_code: str = postal_code
        self.country: str = country
        self.extensions: List[Extension] = extensions

    @property
    def full_address(self) -> str:
        """
        Returns: The full postal address

        """
        return '\n'.join(
            self.lines) + '\n' + self.city + ', ' + self.state + '\n' + self.postal_code + ', ' + self.country

    @property
    def latitude(self) -> Optional[float]:
        """
        Returns: The latitude if available

        """
        matching_extensions = [extension for extension in self.extensions if extension.url == 'latitude']
        if len(matching_extensions) == 0:
            return None
        return matching_extensions[0].value

    @property
    def longitude(self) -> Optional[float]:
        """
        Returns: The longitude if available

        """
        matching_extensions = [extension for extension in self.extensions if extension.url == 'longitude']
        if len(matching_extensions) == 0:
            return None
        return matching_extensions[0].value

    def __str__(self) -> str:
        return self.full_address


class MaritalStatus:
    """The marital status, stored as a 1 length string, str() can be used to get the full definition"""
    def __init__(self, martial_status: str):
        self.marital_status: str = martial_status

    def __str__(self) -> str:
        lookup: Dict[str, str] = {
            'A': 'Annuled',
            'D': 'Divorced',
            'I': 'Interlocutory',
            'L': 'Legally Seperated',
            'M': 'Married',
            'P': 'Polygamous',
            'S': 'Never Married',
            'T': 'Domestic Partner',
            'U': 'Unmarried',
            'W': 'Widowed'
        }
        return lookup.get(self.marital_status, 'Unknown')


class Communications:
    """The known languages and communication methods"""
    def __init__(self, communication: List[Tuple[str, str]]):
        self.communication = communication

    @property
    def languages(self) -> List[str]:
        """
        Returns: A list of languages

        """
        return [l[1] for l in self.communication]

    @property
    def codes(self) -> List[str]:
        """
        Returns: A list of language codes

        """
        return [l[0] for l in self.communication]

    def __str__(self) -> str:
        return ', '.join(self.languages)


class Patient:
    """The patient object consisting of a uuid, name, telecoms, gender, birth_date, addresses, marial_status, multiple_birth, communications, extensions, and identifiers"""
    def __init__(self, uuid: str, name: Name, telecoms: List[Telecom], gender: str, birth_date: datetime.date,
                 addresses: List[Address], marital_status: MaritalStatus, multiple_birth: bool,
                 communications: Communications, extensions: List[Extension], identifiers: List[Identifier]):
        self.uuid: str = uuid
        self.name: Name = name
        self.telecoms: List[Telecom] = telecoms
        self.gender: str = gender
        self.birth_date: datetime.date = birth_date
        self.addresses: List[Address] = addresses
        self.marital_status: MaritalStatus = marital_status
        self.multiple_birth: bool = multiple_birth
        self.communications: Communications = communications
        self.extensions: List[Extension] = extensions
        self.identifiers: List[Identifier] = identifiers

    def full_name(self) -> str:
        """
        Returns: The full name for a patient

        """
        return self.name.full_name

    def age(self) -> float:
        """
        Returns: The age of a patient as a float

        """
        return (datetime.date.today() - self.birth_date).days / 365.25

    def get_extension(self, extension: str) -> Optional[Union[str, float]]:
        """ Gets an extension value (either str or float) based on the extension url, returns None if not available.
        Args:
            extension: url of the extension

        Returns: str or float of the extension or None if not found

        """
        for e in self.extensions:
            if e.url == extension:
                return e.value
        return None

    def get_identifier(self, identifier: str) -> Optional[Union[str, float]]:
        """ Gets an identifier value (str) based on the identifier code, returns None if not available.
        Args:
            identifier: code of the identifier

        Returns: str value of the or None if not found

        """
        for i in self.identifiers:
            if i.code == identifier:
                return i.value
        return None

    def __str__(self) -> str:
        return ' | '.join(map(str,
                              [self.uuid, self.name, self.gender, self.birth_date,
                               [str(a).replace('\n', ';') for a in self.addresses],
                               list(map(str, self.telecoms)), self.marital_status, self.multiple_birth, self.communications,
                               list(map(str, self.extensions)), list(map(str, self.identifiers))]))
