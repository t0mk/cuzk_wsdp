# CUZK klient pro dalkovy pristup v Pythonu

Tohle je prakticka ukazka dalkoveho pristupu k webovym sluzbam z CUZK, popsanych na
https://www.cuzk.cz/Katastr-nemovitosti/Poskytovani-udaju-z-KN/Dalkovy-pristup.aspx

kod pouziva endpointy "na zkousku":
https://www.cuzk.cz/Katastr-nemovitosti/Poskytovani-udaju-z-KN/Dalkovy-pristup/Webove-sluzby-DP-na-zkousku.aspx

V addr popisy_sluzeb jsou vygenerovane dokumentace k jednotlivym WSDP. Nejzajimavejsi v tech souborech je klic "Service", kde jsou vyjmenovane operace s typy pro vstup a vystup.

## generovat info o webove sluzbe z WSDL

`python3 -m zeep https://wsdptrial.cuzk.cz/trial/dokumentace/ws28/wsdp/sestavy_v28.wsdl > sestavy.txt`

## deps

`pip3 install --user --upgrade "zeep[xmlsec]"`

## Zpoplatneni

Vyhlaska: https://www.zakonyprolidi.cz/cs/2013-358

Cenik: https://www.cuzk.cz/Katastr-nemovitosti/Poskytovani-udaju-z-KN/Dalkovy-pristup/Uctovani-vystupu-z-KN-poskytovanych-DP-A-WSDP.aspx

z [WSDP_Popis_webovych_sluzeb_pro_uzivatele.pdf](WSDP_Popis_webovych_sluzeb_pro_uzivatele.pdf) strana 42

> 5. Zpoplatnění poskytovaných výstupů
>
> Pro zpoplatnění PDF sestav platí stejná pravidla jako v interaktivním DP, včetně specifické odlišnosti pro
> ověřovací účty. Služby vyhledávaní, správa účtu, číselníky a práce se sestavami jsou poskytovány
> bezúplatně.
>
> Způsob zpoplatnění ve formátu XML je podrobně popsán ve vyhlášce č. 358/2013 Sb., o poskytování údajů
> z katastru nemovitostí.


