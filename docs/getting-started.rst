===============
Getting Started
===============

Welcome! This tutorial highlights FHIR Parser's core features; for further details,
see the links within, or the documentation index which has links to conceptual
and API doc sections.

Imports
=======
The key class to import is FHIR inside fhir_parser.fhir

.. code-block:: python
    :emphasize-lines: 1

    from fhir_parser.fhir import FHIR
    from fhir_parser.patient import Patient
    from fhir_parser.observation import Observation
