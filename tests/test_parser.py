import datetime
from typing import List
import os

import pytest

from fhir_parser.observation import Observation, ObservationComponent
from fhir_parser.parser import str_to_patient, str_to_error, str_to_patients, str_to_observation, str_to_observations
from fhir_parser.patient import Patient, Extension, Identifier


@pytest.fixture(scope='module')
def patient():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_patient.json'), 'r') as patient_file:
        patient_data = patient_file.read().replace('\n', '')
    assert patient_data is not None
    patient: Patient = str_to_patient(patient_data)
    yield patient
    del patient, patient_data


@pytest.fixture(scope='module')
def patients():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_patients.json'), 'r') as patients_file:
        patients_data = patients_file.read().replace('\n', '')
    assert patients_data is not None
    patients: List[Patient] = str_to_patients(patients_data)
    yield patients
    del patients, patients_data


@pytest.fixture(scope='module')
def observation():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_observation.json'), 'r') as observation_file:
        observation_data = observation_file.read().replace('\n', '')
    assert observation_data is not None
    observation: Observation = str_to_observation(observation_data)
    yield observation
    del observation, observation_data

@pytest.fixture(scope='module')
def observations():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_observations.json'), 'r') as observations_file:
        observations_data = observations_file.read().replace('\n', '')
    assert observations_data is not None
    observations: List[Observation] = str_to_observations(observations_data)
    yield observations
    del observations, observations_data

@pytest.fixture(scope='module')
def error():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_error.json'), 'r') as error_file:
        error_data = error_file.read().replace('\n', '')
    assert error_data is not None
    error: str = str_to_error(error_data)
    yield error
    del error, error_data


def test_patient_parser(patient):
    assert patient.uuid == '8f789d0b-3145-4cf2-8504-13159edaa747'
    assert patient.name.full_name == 'Ms. Abby752 Beatty507'

    assert len(patient.telecoms) == 1
    assert patient.telecoms[0].system == 'phone'
    assert patient.telecoms[0].number == '555-118-9003'
    assert patient.telecoms[0].use == 'home'

    assert patient.gender == 'female'
    assert patient.birth_date == datetime.date(year=1998, month=8, day=25)

    assert len(patient.addresses) == 1
    assert patient.addresses[0].full_address == '506 Herzog Byway Apt 99\nBarre, Massachusetts\n01005, US'

    assert patient.marital_status.marital_status == 'S'
    assert str(patient.marital_status) == 'Never Married'

    assert patient.communications.languages == ['English']
    assert patient.communications.codes == ['en-US']

    assert len(patient.extensions) == 7
    assert Extension('us-core-race', 'White') in patient.extensions
    assert Extension('us-core-ethnicity', 'Not Hispanic or Latino') in patient.extensions
    assert Extension('patient-mothersMaidenName', 'Tisa11 Quitzon246') in patient.extensions
    assert Extension('us-core-birthsex', 'F') in patient.extensions
    assert Extension('patient-birthPlace', 'Braintree, Massachusetts, US') in patient.extensions
    assert Extension('disability-adjusted-life-years', 0.0082221553734000332) in patient.extensions
    assert Extension('quality-adjusted-life-years', 20.9917778446266) in patient.extensions

    assert len(patient.identifiers) == 5
    assert Identifier('https://github.com/synthetichealth/synthea', '', '',
                      '8f789d0b-3145-4cf2-8504-13159edaa747') in patient.identifiers
    assert Identifier('http://hospital.smarthealthit.org', 'MR', 'Medical Record Number',
                      '8f789d0b-3145-4cf2-8504-13159edaa747') in patient.identifiers
    assert Identifier('http://hl7.org/fhir/sid/us-ssn', 'SS', 'Social Security Number',
                      '999-58-8677') in patient.identifiers
    assert Identifier('urn:oid:2.16.840.1.113883.4.3.25', 'DL', 'Driver\'s License', 'S99995899') in patient.identifiers
    assert Identifier('http://standardhealthrecord.org/fhir/StructureDefinition/passportNumber', 'PPN',
                      'Passport Number', 'X80142477X') in patient.identifiers


def test_patients_parser(patients):
    assert len(patients) == 10
    test_patient_parser(patients[0])


def test_error_parser(error):
    assert error == 'Resource type \'Patient\' with id \'8f789d0b-3145-4cf2-8504-13159edaa757\' couldn\'t be found.'


def test_observation_parser(observation):
    assert observation.uuid == '4a064229-2a40-45f4-a259-f4eedcfd525a'
    assert observation.type == 'vital-signs'
    assert observation.status == 'final'
    assert observation.patient_uuid == '8f789d0b-3145-4cf2-8504-13159edaa747'
    assert observation.encounter_uuid == '04090f8c-076e-4af1-9582-98d8cae66764'
    assert observation.effective_datatime == datetime.datetime(year=2011, month=9, day=20, hour=21, minute=27, second=12, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)))
    assert observation.issued_datatime == datetime.datetime(year=2011, month=9, day=20, hour=21, minute=27, second=12, microsecond=215000, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)))

    assert len(observation.components) == 3
    assert ObservationComponent('http://loinc.org', '85354-9', 'Blood Pressure', None, None)
    assert ObservationComponent('http://loinc.org', '8462-4', 'Diastolic Blood Pressure', 76.0, 'mm[HG]')
    assert ObservationComponent('http://loinc.org', '8480-6', 'Systolic Blood Pressure', 118.0, 'mm[Hg]')

def test_observations_parser(observations):
    assert len(observations) == 83
    test_observation_parser(observations[78])