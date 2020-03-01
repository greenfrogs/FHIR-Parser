"""
Observations
============
The Observation and ObservationComponent objects
"""

import datetime
from typing import List, Union, Optional


class ObservationComponent:
    """An observation component object containing the details of a part of the observation"""
    def __init__(self, system: str, code: str, display: str, value: Optional[Union[str, float]], unit: Optional[str]):
        self.system: str = system
        self.code: str = code
        self.display: str = display
        self.value: float = value
        self.unit: str = unit

    def quantity(self) -> str:
        """ Pretty print of the value and unit for an observation
        Returns: Value and unit, '76.0 mm[Hg]'

        """
        return str(self.value if self.value is not None else 'N/A') + (self.unit if self.unit is not None else '')

    def __eq__(self, o: object) -> bool:
        if type(o) != ObservationComponent:
            return False
        return self.__dict__ == o.__dict__

    def __str__(self) -> str:
        return self.display + ': ' + str(self.value if self.value is not None else 'N/A') + (self.unit if self.unit is not None else '')


class Observation:
    """An observation object holding either one or more observation components"""
    def __init__(self, uuid: str, type: str, status: str, patient_uuid: str, encounter_uuid: str,
                 effective_datetime: datetime.datetime, issued_datetime: datetime.datetime,
                 components: List[ObservationComponent]):
        self.uuid: str = uuid
        self.type: str = type
        self.status: str = status
        self.patient_uuid: str = patient_uuid
        self.encounter_uuid: str = encounter_uuid
        self.effective_datetime: datetime.datetime = effective_datetime
        self.issued_datetime: datetime.datetime = issued_datetime
        self.components: List[ObservationComponent] = components

    def __str__(self) -> str:
        return ' | '.join(map(str, [self.uuid, self.type, self.status, self.effective_datetime, self.issued_datetime, '[' + ', '.join(map(str, self.components)) + ']']))


