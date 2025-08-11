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
#   po želji lahko več (npr. 1500).
# vsaka skladba je svoj spletni naslov, zato mora program poklicati 1126
#   posameznih naslovov, kar traja cca. 5 min.
for x in range(1, 1126 + 1):
    print(x)
    url = f"https://www.bach-digital.de/receive/BachDigitalWork_work_0000{url_stevilo(x)}?lang=en"
    odziv = requests.get(url, headers=headers)
    with open(f"skladba{x}.html", "w", encoding="utf-8") as dat:
        dat.write(odziv.text)

# vzorci za regularne izraze ter podatki, ki bodo izlusčeni.
# SPREMENI BWV VZOREC, NAJ IŠČE V NASLOVU
vzorci = {
    "naslov": r'<span class="worktitle">(?P<naslov>.+?)</span>',
    "BWV": r"<title>Bach digital - .+? BWV (?P<BWV>.*?)</title>",
    "zanr": r'<dt class="col-sm-3">Genre</dt>\n<dd class="col-sm-9">(?P<zanr>.+?)</dd>',
    "citati_biblije": r'<dt class="col-sm-3">Proper</dt>',
    "psalm": r'<dd class="col-sm-9">Psalm: .*?>(?P<psalm>.+?)</a>',
    "pismo": r"<br>Epistel: .*?>(?P<pismo>.+?)</a>",
    "evangelij": r"<br>Gospel: .*?>(?P<evangelij>.+?)</a>",
    "aranzma": r'"Scoring":\["(?P<aranzma>.*?)"\]',
    "nastanek": r'"Date of origin":"(?P<nastanek>\d+?)"',
    "povezave": r"is part of.*?>(?P<povezave>.+?)</a>",
}
# Bach-Werke-Verzeichnis">BWV&nbsp;(?P<BWV>\d+?)</abbr>


# iz surovega html izlušči podatke. Za vsako skladbo ustvari slovar,
#   in nato slovarje shrani v seznam
podatki = []
for x in range(1, 1126 + 1):
    with open(f"skladba{x}.html", encoding="utf-8") as dat:
        skladba = {}
        besedilo = dat.read()
        skladba.update({"sifra": x})
        for vzorec in vzorci:
            podatek = re.findall(vzorci[vzorec], besedilo)
            if vzorec == "citati_biblije":
                if podatek == ['<dt class="col-sm-3">Proper</dt>']:
                    podatek = ["DA"]
                else:
                    podatek = ["NE"]
                skladba.update({vzorec: podatek[0]})
            elif len(podatek) == 0:
                skladba.update({vzorec: "NA"})
            else:
                skladba.update({vzorec: podatek[0]})
        podatki.append(skladba)

# Seznam s slovarji pretvori v CSV datoteko
with open("podatki.csv", "w", newline="", encoding="utf-8") as dat:
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
            "aranzma",
            "nastanek",
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
                skladba["aranzma"],
                skladba["nastanek"],
                skladba["povezave"],
            ]
        )
