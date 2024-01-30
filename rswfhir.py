import requests
from jwt import JWT
import base64
from fhir.resources.R4B.bundle import Bundle
from fhir.resources.R4B.operationoutcome import OperationOutcome
from fhir.resources.R4B.operationoutcome import OperationOutcome
from fhir.resources.R4B.immunization import Immunization

class rswfhir:
    _url_base = 'https://accproxy.reseausantewallon.be/fhir/careset/'
    _app_identifier = 'Sosltisse'
    _bearer = ''

    def __init__(self,bearer):
        self._bearer = bearer

    def call(self,request,data):
        request_url = self._url_base + request
        headers = {"Application_identifier": self._app_identifier,"Authorization": "Bearer " + self._bearer}
        if isinstance(data,str):
            headers['Content-Type'] = 'application/json'
        result = requests.post(request_url, headers=headers, data=data, timeout=30)
        print (result)
        result_json = result.json()
        result_type = self._resource_type(result_json)
        if result_type == False:
            return False
        if result_type == 'Bundle':
            return Bundle(**result_json)
        if result_type == 'OperationOutcome':
            return OperationOutcome(**result_json)
        if result_type == 'Immunization':
            return Immunization(**result_json)
        return False
    
    def _resource_type(self,response_json):
        if 'resourceType' not in response_json.keys():
            return False
        return response_json['resourceType']
