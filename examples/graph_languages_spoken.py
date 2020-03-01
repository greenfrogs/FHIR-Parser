import matplotlib.pyplot as plt
from fhir_parser import FHIR

fhir = FHIR()
patients = fhir.get_all_patients()

languages = {}
for patient in patients:
    for language in patient.communications.languages:
        languages.update({language: languages.get(language, 0) + 1})


plt.bar(range(len(languages)), list(languages.values()), align='center')
plt.xticks(range(len(languages)), list(languages.keys()), rotation='vertical')
plt.show()