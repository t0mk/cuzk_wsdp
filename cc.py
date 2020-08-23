#!/usr/bin/env python3

from zeep import Client, Settings
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.wsse.username import UsernameToken
import xml.dom.minidom

wsdl = "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/vyhledat_v28.wsdl"
transport = Transport(cache=SqliteCache())


settings = Settings(raw_response=False, strict=False, xml_huge_tree=True)
settings = Settings(strict=False, xml_huge_tree=True)

client = Client(wsdl,
    transport=transport,
    wsse=UsernameToken("WSTEST","WSHESLO"),
    settings=settings,
)


kuid = '693936'
ps = [
    [kuid, '76', '2'],
    [kuid, '41', '1'],
    [kuid, '1192', ''],
    [kuid, '104', ''],
    [kuid, '127', ''],
    [kuid, '129', ''],
    [kuid, '130', ''],
] 

def pp(kuk, kc, pd):
    print(kuk, kc, pd)
    if pd:
        resp = client.service.najdiParcelu(
            katastrUzemiKod=kuk,
            kmenoveCislo=kc,
            poddeleni=pd,
        )
    else:
        resp = client.service.najdiParcelu(
            katastrUzemiKod=kuk,
            kmenoveCislo=kc,
        )
    return resp

    #dom = xml.dom.minidom.parseString(out)
    #print(dom.toprettyxml())
    #print(out)

for p in ps:
    r = pp(p[0], p[1], p[2])
    print(r)
