from fhir_parser.fhir import FHIR

fhir = FHIR()
fhir.get_patient('8f789d0b-3145-4cf2-8504-13159edaa747').age()