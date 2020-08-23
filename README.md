# CUZK klient pro dalkovy pristup v Python

## generovat info o webove sluzbe z WSDL

`python3 -m zeep https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/sestavy_v28.wsdl > sestavy.txt`

## deps

`pip3 install --user --upgrade "zeep[xmlsec]"`
