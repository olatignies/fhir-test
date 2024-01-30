import requests

class rswfhir:
    _url_base = 'https://accproxy.reseausantewallon.be/fhir/careset/'
    _app_identifier = 'Sosltisse'
    _bearer = ''

    def __init__(self,bearer):
        self._bearer = bearer

    def call(self,request,data):
        request_url = self._url_base + request
        headers = {"Application_identifier": self._app_identifier,"Authorization": "Bearer " + self._bearer}
        return requests.post(request_url, headers=headers, data=data, timeout=30)