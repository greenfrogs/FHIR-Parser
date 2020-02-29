"""
FHIR
====
The primary component of the FHIR parser with the FHIR class for handling all FHIR endpoint calls
"""

import urllib.parse
from typing import List

import requests

from fhir_parser.observation import Observation
from fhir_parser.parser import str_to_patient, str_to_error, str_to_patients, str_to_observation, str_to_observations
from fhir_parser.patient import Patient


class FHIR:
    """Create the FHIR endpoint to retrieve patient and observation data"""
    def __init__(self, endpoint: str = 'https://localhost:5001/api/', verify_ssl: bool = False):
        self.endpoint = endpoint
        self.verify_ssl = verify_ssl
        if not self.verify_ssl:
            # noinspection PyUnresolvedReferences
            from requests.packages.urllib3.exceptions import InsecureRequestWarning
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def _error_response(self, response):
        if response.text == '' or response.status_code != 200:
            raise ConnectionError('Status code: {}'.format(response.status_code))
        if str_to_error(response.text) is not None:
            raise ConnectionError(str_to_error(response.text))

    def get_all_patients(self) -> List[Patient]:
        """
        Returns: A list of patients

        """
        response = requests.get(urllib.parse.urljoin(self.endpoint, 'Patient/'), verify=self.verify_ssl)
        self._error_response(response)
        try:
            return str_to_patients(response.text)
        except KeyError:
            raise AttributeError('Patient data is corrupt')

    def get_patient_page(self, page: int) -> List[Patient]:
        """
        Args:
            page: Page number int

        Returns: A list of patients up to the specified page

        """
        response = requests.get(urllib.parse.urljoin(self.endpoint, 'Patient/pages/' + str(page)),
                                verify=self.verify_ssl)
        self._error_response(response)
        try:
            return str_to_patients(response.text)
        except KeyError:
            raise AttributeError('Patient data is corrupt')

    def get_patient(self, id: str) -> Patient:
        """
        Args:
            id: Patient ID or UUID string

        Returns: A single patient

        """
        response = requests.get(urllib.parse.urljoin(self.endpoint, 'Patient/' + str(id)), verify=self.verify_ssl)
        self._error_response(response)
        try:
            return str_to_patient(response.text)
        except KeyError:
            raise AttributeError('Patient data is corrupt')

    def get_observation(self, id: str) -> Observation:
        """
        Args:
            id: Observation ID or UUID string

        Returns: A single observation

        """
        response = requests.get(urllib.parse.urljoin(self.endpoint, 'Observation/single/' + str(id)), verify=self.verify_ssl)
        self._error_response(response)
        try:
            return str_to_observation(response.text)
        except KeyError:
            raise AttributeError('Observation data is corrupt')

    def get_patient_observations(self, id: str) -> List[Observation]:
        """
        Args:
            id: Patient ID or UUID string

        Returns: A list of observations for a patient

        """
        response = requests.get(urllib.parse.urljoin(self.endpoint, 'Observation/' + str(id)),
                                verify=self.verify_ssl)
        self._error_response(response)
        try:
            return str_to_observations(response.text)
        except KeyError:
            raise AttributeError('Observation data from patient is corrupt')

    def get_patient_observations_page(self, id: str, page: int) -> List[Observation]:
        """
        Args:
            id: Patient ID or UUID string
            page: Page number int

        Returns: A list of observations for a patient up to the specified page

        """
        response = requests.get(urllib.parse.urljoin(self.endpoint, 'Observation/pages/' + str(page) + '/' + str(id)),
                                verify=self.verify_ssl)
        self._error_response(response)
        try:
            return str_to_observations(response.text)
        except KeyError:
            raise AttributeError('Observation data from patient is corrupt')
