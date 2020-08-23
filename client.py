#!/usr/bin/env python3

from zeep import Client, Settings
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.wsse.username import UsernameToken

import sys

TRIAL = True

LVID = 674644306
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

PIDS = [
    2850900306,
    2850879306,
    2850920306,
    62570648010,
    62570653010,
    62570658010,
    3168567306,
    3168568306,
    2851102306,
    3370798306,
    3370799306,
    3370801306,
    2851326306,
]

trialWsdls = {
    "vyhledat": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/vyhledat_v28.wsdl",
    "informace": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/informace_v28.wsdl",
    "sestavy": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/sestavy_v28.wsdl",
    "ciselnik": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/ciselnik_v28.wsdl",
    "ctios": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/ctios/ctios_v28.wsdl",
    "ucet": "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/ucet_v28.wsdl",
}

prodWsdls = {
    "sestavy": "https://katastr.cuzk.cz/dokumentace/ws28/wsdp/sestavy_v28.wsdl",
    "ciselnik": "https://katastr.cuzk.cz/dokumentace/ws28/wsdp/ciselnik_v28.wsdl",
    "vyhledat": "https://katastr.cuzk.cz/dokumentace/ws28/wsdp/vyhledat_v28.wsdl",
    "informace": "https://katastr.cuzk.cz/dokumentace/ws28/wsdp/informace_v28.wsdl",
    "ucet": "https://katastr.cuzk.cz/dokumentace/ws28/wsdp/ucet_v28.wsdl",
    "ctios": "https://katastr.cuzk.cz/dokumentace/ws28/wsdp/ctios_v28.wsdl",
}


def CUZKClient(wsdl):
    transport = Transport(cache=SqliteCache())
    settings = Settings(raw_response=False, strict=False, xml_huge_tree=True)
    settings = Settings(strict=False, xml_huge_tree=True)
    relevantWsdls = prodWsdls
    creds = None
    if TRIAL:
        relevantWsdls = trialWsdls
        creds = ["WSTEST", "WSHESLO"]
    if not creds[0] and not creds[1]:
        print("Nastavte creds ve funkci CUZKClient")
        sys.exit(0)
        
    return Client(relevantWsdls[wsdl],
        transport=transport,
        wsse=UsernameToken(*creds),
        settings=settings,
    )

def parArgs(kuk, kc, pd):
    args = {
        "katastrUzemiKod": kuk,
        "kmenoveCislo": kc,
    }
    if pd:
        args['poddeleni'] = pd
    return args

####### OPS

def mbrp(pid):
    c = CUZKClient("informace")
    resp = c.service.dejMBRParcel(pid)
    return resp

def gip(kuk, kc, pd):
    args = parArgs(kuk,kc,pd)
    args['format'] = 'xml'
    return CUZKClient("sestavy").service.generujInfoOParcelach(**args)

def pp(kuk, kc, pd):
    args = parArgs(kuk,kc,pd)
    return CUZKClient("vyhledat").service.najdiParcelu(**args)

def nlv(lvid):
    return CUZKClient("informace").service.dejNahledLV(lvId=lvid)

###### tests

def test_pp():
    for p in PS:
        r = pp(p[0], p[1], p[2])
        #print(r['ParcelaList']['Parcela'][0]['idParcely'])
        print(r)

def test_mbrp():
    p = PIDS[3]
    r = mbrp(p)
    print(r)





if __name__ == "__main__":
    #r = gip(*PS[4])
    #print(r)
    #test_pp()
    #test_mbrp()
    print(nlv(LVID))
    
    #dom = xml.dom.minidom.parseString(out)
    #print(dom.toprettyxml())
    #print(out)
