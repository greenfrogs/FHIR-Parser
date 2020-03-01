from fhir_parser import FHIR

fhir = FHIR()
patients = fhir.get_all_patients()

ages = []
for patient in patients:
    ages.append(patient.age())

print(sum(ages)/len(ages))