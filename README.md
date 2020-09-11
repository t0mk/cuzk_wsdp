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

z [WSDP_Popis_webovych_sluzeb_pro_uzivatele.pdf](WSDP_Popis_webovych_sluzeb_pro_uzivatele.pdf) strana 42

> 5. Zpoplatnění poskytovaných výstupů
>
> Pro zpoplatnění PDF sestav platí stejná pravidla jako v interaktivním DP, včetně specifické odlišnosti pro
> ověřovací účty. Služby vyhledávaní, správa účtu, číselníky a práce se sestavami jsou poskytovány
> bezúplatně.
>
> Způsob zpoplatnění ve formátu XML je podrobně popsán ve vyhlášce č. 358/2013 Sb., o poskytování údajů
> z katastru nemovitostí.

Vyhlaska 358/2013 Sb.: https://www.zakonyprolidi.cz/cs/2013-358

Katastralni zakon: https://www.zakonyprolidi.cz/cs/2013-256 

Souhrn Katastralniho zakona: https://cs.wikipedia.org/wiki/Katastr_nemovitostí_České_republiky#Katastrální_zákon

Cenik: https://www.cuzk.cz/Katastr-nemovitosti/Poskytovani-udaju-z-KN/Dalkovy-pristup/Uctovani-vystupu-z-KN-poskytovanych-DP-A-WSDP.aspx

Z tohoto vyplyva, ze jen "sestavy" jsou zpoplatnene podle toho ceniku (pdf je drazsi nez xml z nejakeho duvodu!?) a vsechny dotazy, co nejsou "sestavy", jsou "bezuplatne", tj. vsechny operace v souborech:

* [popisy_sluzeb/informace.txt.ops](popisy_sluzeb/informace.txt.ops)
* [popisy_sluzeb/vyhledat.txt.ops](popisy_sluzeb/vyhledat.txt.ops)
* [popisy_sluzeb/ctios.txt.ops](popisy_sluzeb/ctios.txt.ops)

.. by mely byt zdarma. Krome `dejNahledLV`, ktera je pristupna jen urednikum (ne platicim zakaznikum).

## Priklad vystupu

vystup z
 
```python
print(CUZKClient("informace").service.dejNahledLV(katuzeKod='693936', lvCislo=310))
```

```json
{
    "vysledek": {
        "zprava": [
            {
                "_value_1": "Požadovaná akce byla úspěšně provedena.",
                "kod": 0,
                "uroven": "INFORMACE"
            }
        ]
    },
    "LV": {
        "idLV": 674691306,
        "katastralniUzemi": {
            "kod": 693936,
            "nazev": "Jáma"
        },
        "lvCislo": 310
    },
    "OS": [
        {
            "idOS": 421450302,
            "nazev": None,
            "ico": None,
            "doplnekIco": None,
            "prijmeni": "Fus",
            "jmeno": "Karel",
            "titulPred": None,
            "titulZa": None,
            "rcZkracene": "980419",
            "ulice": None,
            "cisloDomovni": 129,
            "cisloOrientacni": None,
            "castObceNazev": "Odry",
            "obecNazev": "Odry",
            "mestskaCastNazev": None,
            "mestskyObvodNazev": None,
            "psc": 11000,
            "vlastnikTyp": "OFO",
            "typCpCe": "1",
            "statNazev": None,
            "okresNazev": None,
            "charOSType": 2,
            "partner1": None,
            "partner2": None
        },
        {
            "idOS": 414306306,
            "nazev": None,
            "ico": None,
            "doplnekIco": None,
            "prijmeni": "Fus",
            "jmeno": "Karel",
            "titulPred": None,
            "titulZa": None,
            "rcZkracene": "970419",
            "ulice": None,
            "cisloDomovni": 5,
            "cisloOrientacni": None,
            "castObceNazev": "Hošťálkovy",
            "obecNazev": "Hošťálkovy",
            "mestskaCastNazev": None,
            "mestskyObvodNazev": None,
            "psc": 11000,
            "vlastnikTyp": "OFO",
            "typCpCe": "1",
            "statNazev": None,
            "okresNazev": None,
            "charOSType": 2,
            "partner1": None,
            "partner2": None
        }
    ],
    "vlastnictvi": [
        {
            "idVlastnictvi": 1067155306,
            "lvId": 674691306,
            "podilCitatel": 1,
            "podilJmenovatel": 2,
            "typPravnihoVztahuKod": "30",
            "katuzeKod": 693936,
            "lvCislo": 310,
            "osId": 421450302,
            "parcelaId": None,
            "budovaId": None,
            "jednotkaId": None,
            "pravoStavbyId": None
        },
        {
            "idVlastnictvi": 1067156306,
            "lvId": 674691306,
            "podilCitatel": 1,
            "podilJmenovatel": 2,
            "typPravnihoVztahuKod": "30",
            "katuzeKod": 693936,
            "lvCislo": 310,
            "osId": 414306306,
            "parcelaId": None,
            "budovaId": None,
            "jednotkaId": None,
            "pravoStavbyId": None
        }
    ],
    "parcela": [
        {
            "idParcely": 3169359306,
            "parcelaType": "PKN",
            "katuzeKod": 693936,
            "katuzePuv": None,
            "kmenoveCislo": 2302,
            "poddeleniCisla": None,
            "dil": None,
            "zpUrVyKod": 0,
            "typZE": None,
            "drupozKod": 10,
            "zpuvypaKod": None,
            "typ": None,
            "vymera": 26,
            "lvId": 674691306,
            "druhCislovaniPar": "2",
            "stavba": None,
            "stavbaSoucastiParcely": "n",
            "pravoStavby": None
        }
    ],
    "stavba": [],
    "jednotka": [],
    "pravoStavby": []
}

```
