import fhir.resources.BE.STU1
from fhir.resources.BE.STU1.organization import BeOrganization
from fhir.resources.BE.STU1.address import BeAddress
from fhir.resources.BE.STU1.vaccination import BeVaccination
from fhir.resources.BE.STU1.patient import BePatient
from fhir.resources.R4B.address import Address
from fhir.resources.R4B.reference import Reference
import json
import dateutil.parser

def DecodeDateTime(empDict):
   if 'occurrenceDateTime' in empDict or 'recorded' in empDict:
      empDict["occurrenceDateTime"] = dateutil.parser.parse(empDict["occurrenceDateTime"])
      empDict["recorded"] = dateutil.parser.parse(empDict["recorded"])
      return empDict

data = {
    "id": "f001",
    "active": True,
    "name": "Acme Corporation",
    "address": [{"country": "Switzerland"}],
    "type" : [
        {
            "coding" : [
                {
                "system" : "https://www.ehealth.fgov.be/standards/fhir/core/CodeSystem/cd-hcparty",
                "code" : "orghospital"
                }
            ]
        }
    ]
}
org = BeOrganization(**data)
print (org.resource_type == "BeOrganization")
print (isinstance(org.address[0], BeAddress))
print (org.address[0].country == "Switzerland")
print (org.dict()['active'] is True)

print (json.dumps(org.dict()))

immunization = {
  "id" : "aymeric-rota1",
  "meta" : {
    "profile" : [
      "https://www.ehealth.fgov.be/standards/fhir/vaccination/StructureDefinition/be-vaccination"
    ]
  },
  "text" : {
    "status" : "extensions",
    "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: Immunization</b><a name=\"aymeric-rota1\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource Immunization &quot;aymeric-rota1&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-be-vaccination.html\">BeVaccination</a></p></div><p><b>BeExtRecorder</b>: <a href=\"Organization-org-regional-child-care-agency.html\">Organization/org-regional-child-care-agency</a> &quot;Regional Child Care Agency&quot;</p><p><b>status</b>: completed</p><p><b>vaccineCode</b>: Rotavirus vaccine <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"https://browser.ihtsdotools.org/\">SNOMED CT</a>#871761004)</span></p><p><b>patient</b>: <span/></p><p><b>occurrence</b>: 2020-04-06</p><p><b>recorded</b>: 2020-04-06</p><p><b>doseQuantity</b>: 1</p><h3>Performers</h3><table class=\"grid\"><tr><td>-</td><td><b>Actor</b></td></tr><tr><td>*</td><td><span/></td></tr></table></div>"
  },
  "extension" : [
    {
      "url" : "https://www.ehealth.fgov.be/standards/fhir/core/StructureDefinition/be-ext-recorder",
      "valueReference" : {
        "reference" : "Organization/org-regional-child-care-agency"
      }
    }
  ],
  "status" : "completed",
  "vaccineCode" : {
    "coding" : [
      {
        "system" : "http://snomed.info/sct",
        "code" : "871761004"
      }
    ]
  },
  "patient" : {
    "identifier" : {
      "system" : "https://www.ehealth.fgov.be/standards/fhir/core/NamingSystem/ssin",
      "value" : "20020142173"
    }
  },
  "occurrenceDateTime" : "2020-04-06",
  "recorded" : "2020-04-06",
  "doseQuantity" : {
    "value" : 1
  },
  "performer" : [
    {
      "actor" : {
        "identifier" : {
          "system" : "https://www.ehealth.fgov.be/standards/fhir/core/NamingSystem/nihdi-professional",
          "value" : "10829059"
        }
      }
    }
  ]    
}

vaccine = BeVaccination(**immunization)

print (vaccine.resource_type == "BeVaccination")
print (isinstance(vaccine.patient, Reference))
print (json.dumps(vaccine.dict(),default=str))
