#!/usr/bin/env python3

from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.wsse.username import UsernameToken


from pprint import pprint

wsdl = "https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/vyhledat_v28.wsdl"
transport = Transport(cache=SqliteCache())
client = Client(wsdl, transport=transport, wsse=UsernameToken("WSTEST","WSHESLO"))

print(client)


def parseElements(elements):
    all_elements = {}
    for name, element in elements:
        all_elements[name] = {}
        all_elements[name]['optional'] = element.is_optional
        if hasattr(element.type, 'elements'):
            all_elements[name]['type'] = parseElements(
                element.type.elements)
        else:
            all_elements[name]['type'] = str(element.type)

    return all_elements


interface = {}
for service in client.wsdl.services.values():
    interface[service.name] = {}
    for port in service.ports.values():
        interface[service.name][port.name] = {}
        operations = {}
        for operation in port.binding._operations.values():
            operations[operation.name] = {}
            operations[operation.name]['input'] = {}
            elements = operation.input.body.type.elements
            operations[operation.name]['input'] = parseElements(elements)
        interface[service.name][port.name]['operations'] = operations


#pprint(interface)

resp = client.service.najdiParcelu(
    katastrUzemiKod='34234',
    kmenoveCislo='76',
    poddeleni='2',
)

print(resp)
