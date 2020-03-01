===============
Examples
===============

Welcome! THis collection of examples helps to highlight FHIR Parser's core features; for further details,
see the getting started guide, or the documentation index which has links to the API doc sections.

Average Patient Age
===================
Calculate the average age of all patients in the FHIR database

.. literalinclude:: ../examples/average_patient_age.py


Most Common Patient Observations
================================
Calculate the most common patient observations, a single observation comprises of multiple observation components
which is normally the actual investigation (the observation might be vital-signs which consists of two observation
components for blood pressure tests).

.. literalinclude:: ../examples/most_common_observations.py


=================
Graphing
=================

The following examples use MatPlotLib to graph FHIR data.

Marital Status
==============
A bar chart of the marital status of the dataset.

.. literalinclude:: ../examples/graph_marital_status.py


Languages Spoken
================
A bar chart of all languges spoken in the dataset.

.. literalinclude:: ../examples/graph_languages_spoken.py
