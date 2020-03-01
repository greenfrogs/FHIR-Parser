===============
Getting Started
===============

Welcome! This tutorial highlights FHIR Parser's core features; for further details,
see the links within, or the documentation index which has links to conceptual
and API doc sections.

Imports
=======
The key class to import is FHIR inside fhir_parser.fhir.

.. code-block:: python
    :emphasize-lines: 1

    from fhir_parser import FHIR, Patient, Observation
    from fhir_parser.patient import Patient, Name, Telecom, Communications, Extension, Identifier
    from fhir_parser.observation import Observation, ObservationComponent


Patient Objects
===============
Patients can either be retrieved via their uuid (e.g. 8f789d0b-3145-4cf2-8504-13159edaa747)
or a full list of patients can be retrieved. Patients can also be requested one page at a time.

.. code-block:: python

    fhir = FHIR()
    patients = fhir.get_all_patients()
    specific_patient = fhir.get_patient('8f789d0b-3145-4cf2-8504-13159edaa747')
    first_page_patients = fhir.get_patient_page(1)

The patient object contains:

* `uuid`_ (str)
* `name`_ (patient.Name object)
* `telecoms`_ (list of patient.Telecom objects)
* `gender`_ (str)
* `birth_date`_ (datetime.date object)
* `addresses`_ (list of patient.Address objects)
* `marital_status`_ (patient.MaritalStatus object)
* `multiple_birth`_ (bool)
* `communications`_ or languages spoken (patient.Communications object)
* `extensions`_ (list of patient.Extension objects)
* `identifiers`_ (list of patient.Identifier objects)

.. _uuid:

UUID
----
The unique identifier for a patient.

.. code-block:: python

    > patient.uuid
    '8f789d0b-3145-4cf2-8504-13159edaa747'

Name
----
The name for a patient stored in a patient.Name object. The Name object
contains the full name as a string and a list of strings for given names
and prefixes. The full name can be accessed with the name.full_name property.

.. code-block:: python

    > name = patient.name
    > name.full_name
    'Mr. John Smith'
    > name.family
    'Smith'
    > name.given
    ['John']
    >name.prefix
    ['Mr.']


Telecoms
--------
The telecommunication method for a patient stored a list of patient.Telecom
objects.

.. code-block:: python

    > telecom = patient.telecoms
    > first_telecom = telecom[0]
    > first_telecom.system
    'phone'
    > first_telecom.number
    '555-118-9003'
    > first_telecom.use
    'home'

Gender
------
The gender string of the patient.

.. code-block:: python

    > patient.gender
    'female'


.. _birth_date:

Birth Date
----------
The birth date of the patient stored in a datetime.date object.

.. code-block:: python

    > patient.birth_date
    datetime.date(1967, 2, 25)


Addresses
---------
A list of addresses of a patient stored in a patient.Address object. If the
latitude and longitude of the location is known then it can be accessed with
the latitude and longitude properties. The full postal address can be retrieved
with the full_address property.

.. code-block:: python

    > address = patient.addresses[0]
    > address.full_address
    '''506 Herzog Byway Apt 99
    Barre, Massachusetts
    01005, US'''
    > address.lines
    ['506 Herzog Byway Apt 99']
    > address.city
    'Barre'
    > address.state
    'Massachusetts'
    > address.postal_code
    '01005'
    > address.country
    'US'
    > address.latitude
    42.459058557265024
    > address.longitude
    -72.081489014917324


.. _marital_status:

Marital Status
--------------
The marital status of a patient stored in the patient.MarialStatus object,
the str method can be used to convert the char into a meaningful string.

.. code-block:: python

    > marital = patient.marital_status
    > marital.martial_status
    'S'
    > str(marital)
    'Never Married'


.. _multiple_birth:

Multiple Birth
--------------
The multiple birth argument stored as a bool, defaults to false when not available.

.. code-block:: python

    > patient.multiple_birth
    False


Communications
--------------
The communication methods or languages spoken by the patient, stored in a single patient.Communications object.

.. code-block:: python

    > communications = patient.communications
    > communications.languages
    ['English']
    > communications.codes
    ['en-US']

Extensions
----------
The extensions available for a patient, most commonly: us-core-race, us-core-ethnicity,
patient-mothersMaidenName, us-core-birthsex, patient-birthPlace, disability-adjusted-life-years, and
quality-adjusted-life-years. They can be accessed directly by retrieving the list of patient.Extension objects or
more easily by using the get_extension method.

.. code-block:: python

    > patient.get_extension('us-core-ethnicity')
    'Not Hispanic or Latino'
    > patient.extensions
    ['us-core-race: White', 'us-core-ethnicity: Not Hispanic or Latino', ...]


Identifiers
-----------
The identifiers available for a patient, most commonly: Medical Record Number (MR), Social Security Number (SS),
and Driver's License (DL). They can be accessed directly by retrieving the list of patient.Identifier objects or
more easily by using the get_identifier method.

.. code-block:: python

    > patient.get_identifier('DL')
    'S99995899'
    > patient.identifiers
    ['Driver\'s License: S99995899', 'Social Security Number: 999-58-8677', ...]


Observation Objects
===================
A single observation can be retrieved with the it's uuid or a list of observations for a single patient. Observations
for a patient can also be retrieved one page at a time.

.. code-block:: python

    fhir = FHIR()
    observations = fhir.get_patient_observations('8f789d0b-3145-4cf2-8504-13159edaa747')
    specific_observation  = fhir.get_observation('4a064229-2a40-45f4-a259-f4eedcfd525a')
    first_page_observations = fhir.get_patient_observations_page('8f789d0b-3145-4cf2-8504-13159edaa747', 1)

The patient object contains:

* :ref:`uuid<observation_uuid>` (str)
* `type`_ (str)
* `status`_ (str)
* `patient_uuid`_ (str)
* `encounter_uuid`_ (str)
* `effective_datetime`_ (datetime.datetime object)
* `issued_datetime`_ (datetime.datetime object)
* `components`_ (list of observation.ObservationComponents)

.. _observation_uuid:

UUID
----
The unique identifier for an observation.

.. code-block:: python

    > observation.uuid
    '4a064229-2a40-45f4-a259-f4eedcfd525a'

Type
----
The type of the investigation, typically: vital-signs, survey, or laboratory.

.. code-block:: python

    > observation.type
    'vital-signs'


Status
------
The status of the investigation.

.. code-block:: python

    > observation.status
    'final'

.. _patient_uuid:

Patient UUID
------------
The unique identifier of the patient tied to the observation.

.. code-block:: python

    > observation.patient_uuid
    '8f789d0b-3145-4cf2-8504-13159edaa747'

.. _encounter_uuid:

Encounter UUID
--------------
The unique identifier of the encounter tied to the observation.

.. code-block:: python

    > observation.encounter_uuid
    '04090f8c-076e-4af1-9582-98d8cae66764'

.. _effective_datetime:

Effective Datetime
------------------
The effective datetime of the observation returned as a datetime.datetime object.

.. code-block:: python

    > observation.effective_datetime
    datetime.datetime(2011, 9, 20, 21, 27, 12, tzinfo=tzoffset(None, 3600))

.. _issued_datetime:

Issued Datetime
---------------
The issued datetime of the observation returned as a datetime.datetime object.

.. code-block:: python

    > observation.effective_datatime
    datetime.datetime(2011, 9, 20, 21, 27, 12, 215000, tzinfo=tzoffset(None, 3600))


Components
----------
Each observation consists of multiple observation components, for example 'Diastolic Blood Pressure' and
'Systolic Blood Pressure' as part of a 'Blood Pressure' vital signs observation. Stored as a list of
observation.ObservationComponent objects.

.. code-block:: python

    > component = observation.components[0]
    > component.system
    'http://loinc.org'
    > component.code
    '8462-4'
    > component.display
    'Diastolic Blood Pressure'
    > component.value
    76.0
    > component.unit
    mm[Hg]
    > component.quantity()
    '76.0 mm[Hg]'