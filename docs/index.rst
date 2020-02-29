FHIR Parser
=======================================
**FHIR Parser** is an elegant and simple FHIR library for Python, built for human beings.

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


Getting started
---------------

Many core ideas & API calls are explained in the tutorial/getting-started
document:

.. toctree::
    :maxdepth: 2

    getting-started


API
---

Know what you're looking for & just need API details? View our auto-generated
API documentation:

.. toctree::
    :maxdepth: 1
    :glob:

    api/*