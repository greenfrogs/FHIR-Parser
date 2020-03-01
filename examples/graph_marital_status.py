import matplotlib.pyplot as plt
from fhir_parser import FHIR

fhir = FHIR()
patients = fhir.get_all_patients()

marital_status = {}
for patient in patients:
    if str(patient.marital_status) in marital_status:
        marital_status[str(patient.marital_status)] += 1
    else:
        marital_status[str(patient.marital_status)] = 1


plt.bar(range(len(marital_status)), list(marital_status.values()), align='center')
plt.xticks(range(len(marital_status)), list(marital_status.keys()))
plt.show()