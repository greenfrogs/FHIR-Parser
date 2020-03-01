import datetime
import dateutil.parser
import json
from typing import List, Optional, Union

from fhir_parser.observation import Observation, ObservationComponent
from fhir_parser.patient import Patient, Name, Telecom, Address, Extension, MaritalStatus, Communications, Identifier


def str_to_patient(input: str) -> Patient:
    input = json.loads(input)
    # Verify resource type
    if not input['resourceType'] == 'Patient':
        raise AssertionError('Not a patient resource type')

    uuid: str = input['id']
    name: Name = Name(input['name'][0]['family'], input['name'][0]['given'], input['name'][0]['prefix'] if 'prefix' in input['name'][0] else '')
    telecoms: List[Telecom] = [Telecom(x['system'], x['value'], x['use']) for x in input['telecom']]
    gender: str = input['gender']
    birth_date: datetime.date = dateutil.parser.isoparse(input['birthDate']).date()
    addresses: List[Address] = [Address(x['line'], x['city'], x['state'], x['postalCode'] if 'postalCode' in x else '', x['country'],
                                        [Extension(y['url'], y['valueDecimal']) for y in
                                         x['extension'][0]['extension']])
                                for x in input['address']]
    marital_status: MaritalStatus = MaritalStatus(input['maritalStatus']['coding'][0]['code'])
    multiple_birth: bool = input['multipleBirthBoolean'] if 'multipleBirthBoolean' in input else False
    communications: Communications = Communications(
        [(x['language']['coding'][0]['code'], x['language']['coding'][0]['display']) for x in input['communication']])

    extensions: List[Extension] = []
    for extension in input['extension']:
        url: str = extension['url'].split('/')[-1]
        value: str = ''
        if 'valueString' in extension:
            value = extension['valueString']
        elif 'valueCode' in extension:
            value = extension['valueCode']
        elif 'valueDecimal' in extension:
            value = extension['valueDecimal']
        elif 'valueAddress' in extension:
            value = ', '.join(extension['valueAddress'].values())
        elif 'extension' in extension:
            for e in extension['extension']:
                if 'valueString' in e:
                    value = e['valueString']
                    break
        extensions.append(Extension(url, value))

    identifiers: List[Identifier] = []
    for identifier in input['identifier']:
        identifiers.append(
            Identifier(identifier['system'], identifier['type']['coding'][0]['code'] if 'type' in identifier else '',
                       identifier['type']['text'] if 'type' in identifier else '',
                       identifier['value']))

    return Patient(uuid, name, telecoms, gender, birth_date, addresses, marital_status, multiple_birth, communications,
                   extensions, identifiers)


def str_to_patients(input: str) -> List[Patient]:
    input = json.loads(input)

    patients: List[Patient] = []
    for i in input:
        for p in i['entry']:
            patients.append(str_to_patient(json.dumps(p['resource'])))
    return patients

def str_to_error(input: str) -> Optional[str]:
    input = json.loads(input)
    if 'resourceType' in input and input['resourceType'] == 'OperationOutcome' and 'issue' in input:
        return input['issue'][0]['diagnostics']
    return None


def json_to_observation_component(input) -> ObservationComponent:
    system: str = input['code']['coding'][0]['system']
    code: str = input['code']['coding'][0]['code']
    display: str = input['code']['coding'][0]['display']
    value: Optional[Union[str, float]] = None
    unit: Optional[str] = None

    if 'valueQuantity' in input:
        value = input['valueQuantity']['value']
        unit = input['valueQuantity']['unit']

    return ObservationComponent(system, code, display, value, unit)


def str_to_observation(input: str) -> Observation:
    input = json.loads(input)

    if not input['resourceType'] == 'Observation':
        raise AssertionError('Not an observation resource type')

    uuid: str = input['id']
    status: str = input['status']
    type: str = input['category'][0]['coding'][0]['code']
    patient_uuid: str = input['subject']['reference'].split('/')[1]
    encounter_uuid: str = input['encounter']['reference'].split('/')[1]
    effective_datetime: datetime.datetime = dateutil.parser.isoparse(input['effectiveDateTime'])
    issued_datetime: datetime.datetime = dateutil.parser.isoparse(input['issued'])

    components: List[ObservationComponent] = []
    if 'code' in input:
        components.append(json_to_observation_component(input))

    if 'component' in input:
        for c in input['component']:
            components.append(json_to_observation_component(c))

    return Observation(uuid, type, status, patient_uuid, encounter_uuid, effective_datetime, issued_datetime, components)


def str_to_observations(input: str) -> List[Observation]:
    input = json.loads(input)

    observations: List[Observation] = []
    for i in input:
        if 'entry' in i:
            for p in i['entry']:
                observations.append(str_to_observation(json.dumps(p['resource'])))
    return observations