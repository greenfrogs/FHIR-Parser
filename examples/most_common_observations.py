from fhir_parser import FHIR

fhir = FHIR()
patients = fhir.get_all_patients()
observations = []

for patient in patients:
    observations.extend(fhir.get_patient_observations(patient.uuid))

print("Total of {} observations".format(len(observations)))

observation_types = [observation.type for observation in observations]
most_frequent_observation_type = max(set(observation_types), key=observation_types.count)
print("Most common observation type: {}".format(most_frequent_observation_type))

observation_components = []
for observation in observations:
    observation_components.extend(observation.components)

print("Total of {} observation components".format(len(observation_components)))

observation_component_types = [observation_component.display for observation_component in observation_components]
most_frequent_observation_component_type = max(set(observation_types), key=observation_types.count)
print("Most common observation component type: {}".format(most_frequent_observation_component_type))