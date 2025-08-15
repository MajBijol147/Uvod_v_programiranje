import requests
import csv
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}


# ustrezna oblika števila, za vpis v url
def url_stevilo(st):
    if len(str(st)) == 4:
        return st
    else:
        return url_stevilo("0" + str(st))


# pobiranje surovih HTML podatkov. Default nastavitve pobere do vključno 1126,
# po želji lahko več (npr. 1500).
def poberi_html():
    for x in range(1, 1126 + 1):
        print(f"skladba: {x}")
        url = f"https://www.bach-digital.de/receive/BachDigitalWork_work_0000{url_stevilo(x)}?lang=en"
        odziv = requests.get(url, headers=headers)
        with open(f"skladba{x}.html", "w", encoding="utf-8") as dat:
            dat.write(odziv.text)


vzorci = {
    "naslov": r'<span class="worktitle">(?P<naslov>.+?)(?:(?:\n<br)|(?:</span>))',
    "BWV": r"<title>Bach digital - .+? BWV (?P<BWV>.*?)</title>",
    "zanr": r'<dt class="col-sm-3">Genre</dt>\n<dd class="col-sm-9">(?P<zanr>.+?)</dd>',
    "citati_biblije": r'<dt class="col-sm-3">Proper</dt>',
    "psalm": r'<dd class="col-sm-9">Psalm: .*?>(?P<psalm>.+?)</a>',
    "pismo": r"<br>Epistel: .*?>(?P<pismo>.+?)</a>",
    "evangelij": r"<br>Gospel: .*?>(?P<evangelij>.+?)</a>",
    "zasedba": r'"Scoring":\["(?P<zasedba>.*?)"\]',
    "leto": r'"Date of origin":".*?(?P<leto>\d{4}).*?",',
    "povezave": r"is part of.*?>(?P<povezave>.+?)</a>",
}
podatki = []


# iz surovega html izlušči podatke. Za vsako skladbo ustvari slovar,
# in nato slovarje shrani v seznam
def izlusci_podatke():
    for x in range(1, 1126 + 1):
        with open(f"skladba{x}.html", encoding="utf-8") as dat:
            skladba = {}
            besedilo = dat.read()
            skladba.update({"sifra": x})
            for vzorec in vzorci:
                podatek = re.findall(vzorci[vzorec], besedilo, flags=re.DOTALL)
                if vzorec == "citati_biblije":
                    if podatek == ['<dt class="col-sm-3">Proper</dt>']:
                        podatek = ["DA"]
                    else:
                        podatek = ["NE"]
                    skladba.update({vzorec: podatek[0]})
                elif len(podatek) == 0:
                    skladba.update({vzorec: "NA"})
                elif vzorec == "BWV":
                    if podatek[0].replace(".", "", 1).isnumeric() == False:
                        skladba.update({vzorec: "NA"})
                    else:
                        skladba.update({vzorec: podatek[0]})
                elif vzorec == "leto":
                    if len(podatek) > 1:
                        skladba.update({vzorec: podatek[1]})
                    else:
                        skladba.update({vzorec: podatek[0]})
                else:
                    skladba.update({vzorec: podatek[0]})
            podatki.append(skladba)


# Seznam s slovarji pretvori v CSV datoteko
def shrani_csv():
    with open("podatki_bach.csv", "w", newline="", encoding="utf-8") as dat:
        writer = csv.writer(dat)
        writer.writerow(
            [
                "sifra",
                "naslov",
                "BWV",
                "zanr",
                "citati_biblije",
                "psalm",
                "pismo",
                "evangelij",
                "zasedba",
                "leto",
                "povezave",
            ]
        )
        for skladba in podatki:
            writer.writerow(
                [
                    skladba["sifra"],
                    skladba["naslov"],
                    skladba["BWV"],
                    skladba["zanr"],
                    skladba["citati_biblije"],
                    skladba["psalm"],
                    skladba["pismo"],
                    skladba["evangelij"],
                    skladba["zasedba"],
                    skladba["leto"],
                    skladba["povezave"],
                ]
            )
