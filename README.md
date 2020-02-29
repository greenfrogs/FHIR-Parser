FHIR Parser
=======================================
**FHIR Parser** is an elegant and simple FHIR library for Python, built for human beings.


[![CircleCI](https://circleci.com/gh/greenfrogs/FHIR-Parser.svg?style=svg&circle-token=a3f7a6daaa0540154190ba8de23f91950ff4d4c2)](https://circleci.com/gh/greenfrogs/FHIR-Parser)
[![Documentation Status](https://readthedocs.org/projects/fhir-parser/badge/?version=latest)](https://fhir-parser.readthedocs.io/en/latest/?badge=latest)

-------------------

**The power of the FHIR Parser**::

    >> fhir = FHIR('https://localhost:5001/api/', verify_ssl=false)
    >> patient = fhir.get_patient('8f789d0b-3145-4cf2-8504-13159edaa747')
    >> patient.full_name
    'Ms. Abby752 Beatty507'
    >> patient.marital_status
    'Never Married'
    >> patient.age()
    21.514

    >> observation = fhir.get_observation('4a064229-2a40-45f4-a259-f4eedcfd525a')
    >> observation.type
    'vital-signs'
    >> observation.components[1].display
    'Diastolic Blood Pressure'
    >> observation.components[1].quantity()
    '76.0 mm[Hg]'