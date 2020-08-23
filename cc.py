#!/usr/bin/env python3

from zeep import Client, Settings
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.wsse.username import UsernameToken

KUID = '693936'
PS = [
    [KUID, '76', '2'],
    [KUID, '41', '1'],
    [KUID, '104', ''],
    [KUID, '127', ''],
    [KUID, '129', ''],
    [KUID, '130', ''],
    [KUID, '1191', ''],
    [KUID, '1192', ''],
    [KUID, '1362', ''],
    [KUID, '1385', '8'],
    [KUID, '1385', '9'],
    [KUID, '1385', '11'],
    [KUID, '2275', '1'],
] 

trialWsdls = {
    "vyhledat": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/vyhledat_v28.wsdl",
    "informace": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/informace_v28.wsdl",
    "sestavy": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/sestavy_v28.wsdl",
    "ciselnik": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/ciselnik_v28.wsdl",
    "ucet": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/ucet_v28.wsdl",
}


def TrialClient(wsdl):
    transport = Transport(cache=SqliteCache())
    settings = Settings(raw_response=False, strict=False, xml_huge_tree=True)
    settings = Settings(strict=False, xml_huge_tree=True)

    return Client(trialWsdls[wsdl],
        transport=transport,
        wsse=UsernameToken("WSTEST","WSHESLO"),
        settings=settings,
    )



def pp(kuk, kc, pd):
    c = TrialClient("vyhledat")
    print(kuk, kc, pd)
    args = {
        "katastrUzemiKod": kuk,
        "kmenoveCislo": kc,
    }
    if pd:
        args['poddeleni'] = pd
    resp = c.service.najdiParcelu(**args)
    return resp

    #dom = xml.dom.minidom.parseString(out)
    #print(dom.toprettyxml())
    #print(out)

def test_pp():
    for p in PS:
        r = pp(p[0], p[1], p[2])
        print(r)

if __name__ == "__main__":
    test_pp()
