''' Query tool for RWS FHIR services '''
import rswfhir
import json
import uuid
from fhir.resources.R4B.bundle import Bundle
from fhir.resources.BE.STU1.patient import BePatient
from fhir.resources.BE.STU1.vaccination import BeVaccination
from fhir.resources.R4B.reference import Reference
from fhir.resources.R4B.immunization import Immunization

PATIENT_SSIN = '69062100976'
DOCTOR_NIDHI = '10840046004'
DOCTOR_SSIN = '69062100976'
SYSTEM_SSIN = 'https://www.ehealth.fgov.be/standards/fhir/core/NamingSystem/ssin'

# load bearer
BEARER = ''
with open('bearer.txt') as f:
    BEARER = f.read()
    print(BEARER)
# load vaccination
VACCINE_JSON = ''
with open('success.json') as f:
    VACCINE_JSON = f.read()
    print(VACCINE_JSON)

RSW = rswfhir.rswfhir(BEARER)
# request patient
result = RSW.call('Patient/_search',{'patient.identifier':'https://www.ehealth.fgov.be/standards/fhir/core/NamingSystem/ssin|' + PATIENT_SSIN})
print (json.dumps(result.dict(), default=str))

vaccine_data = json.loads(VACCINE_JSON)
vaccine = BeVaccination(**vaccine_data)
vaccine.identifier[0].value = str(uuid.uuid4())
vaccine.patient.identifier.value = PATIENT_SSIN
vaccine.patient.identifier.system = SYSTEM_SSIN
vaccine.performer[0].actor.identifier.value = DOCTOR_SSIN
vaccine.performer[0].actor.identifier.system = SYSTEM_SSIN
print (vaccine.resource_type == "BeVaccination")
print (isinstance(vaccine.patient, Reference))
print (json.dumps(vaccine.dict(),default=str))

result = RSW.call('Immunization',json.dumps(vaccine.dict(),default=str))
if result is False:
    print('Failed to call .... return values')
else:
    print (json.dumps(result.dict(), default=str))
