# CUZK klient pro dalkovy pristup v Pythonu

Tohle je prakticka ukazka dalkoveho pristupu k webovym sluzbam z CUZK, popsanych na
https://www.cuzk.cz/Katastr-nemovitosti/Poskytovani-udaju-z-KN/Dalkovy-pristup.aspx

kod pouziva endpointy "na zkousku":
https://www.cuzk.cz/Katastr-nemovitosti/Poskytovani-udaju-z-KN/Dalkovy-pristup/Webove-sluzby-DP-na-zkousku.aspx

## generovat info o webove sluzbe z WSDL

`python3 -m zeep https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/sestavy_v28.wsdl > sestavy.txt`

## deps

`pip3 install --user --upgrade "zeep[xmlsec]"`
