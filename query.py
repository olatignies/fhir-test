''' Query tool for RWS FHIR services '''
import rswfhir
import json
from fhir.resources.R4B.bundle import Bundle
from fhir.resources.BE.STU1.patient import BePatient

# load bearer
BEARER = ''
with open('bearer.txt') as f:
    BEARER = f.read()
    print(BEARER)
RSW = rswfhir.rswfhir(BEARER)
result = RSW.call('Patient/_search',{'patient.identifier':'https://www.ehealth.fgov.be/standards/fhir/core/NamingSystem/ssin|69062100976'})
result_json = result.json()
bundle = Bundle(**result_json)
patient = bundle.entry[0].resource
print (json.dumps(patient.dict(), default=str))
