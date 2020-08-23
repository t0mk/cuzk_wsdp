#!/usr/bin/env python3

import requests


data = """<soapenv:Envelope
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:typ="http://katastr.cuzk.cz/vyhledat/types/v2.8">
<soapenv:Header>
<wsse:Security
soapenv:mustUnderstand="0"
open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
xmlns:wsse="http://docs.oasis-
xmlns:wsu="http://docs.oasis-
<wsse:UsernameToken wsu:Id="UsernameToken-2">
<wsse:Username>WSTEST</wsse:Username>
<wsse:Password
Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-
username-token-profile-1.0#PasswordText">WSHESLO</wsse:Password>
</wsse:UsernameToken>
</wsse:Security>
</soapenv:Header>
<soapenv:Body>
<typ:NajdiParceluRequest>
<typ:katastrUzemiKod>693936</typ:katastrUzemiKod>
<typ:kmenoveCislo>76</typ:kmenoveCislo>
<typ:poddeleni>2</typ:poddeleni>
</typ:NajdiParceluRequest>
</soapenv:Body>
</soapenv:Envelope>
"""


#us =  "https://wsdptrial.cuzk.cz/trial/ws/wsdp/2.8/sestavy"
url = "https://wsdptrial.cuzk.cz/trial/ws/wsdp/2.8/vyhledat"

r = requests.post(url, data=data)

print(r.status_code)
print(r.text)
