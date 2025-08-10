import requests
import os
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

# število kompozicij v BWV leta 1998
stevilo_kompozicij = 1126


# ustrezna oblika števila, za vpis v url
def url_stevilo(st):
    if len(str(st)) == 4:
        return st
    else:
        return url_stevilo("0" + str(st))


# pobiranje surovih HTML podatkov. Default nastavitve pobere do vključno 1126,
#   po želji lahko več (npr. 1500)
# vsaka skladba je svoj spletni naslov, zato mora program poklicati 1126
#   posameznih naslovov, kar je časovno zamudno
def pobiranje_html():
    for x in range(1, 1126 + 1):
        print(x)
        pravo_st = url_stevilo(x)
        url = f"https://www.bach-digital.de/receive/BachDigitalWork_work_0000{pravo_st}?lang=en"
        odziv = requests.get(url, timeout=5, headers=headers)
        # timeout je bugfix
        with open(f"skladba{pravo_st}.html", "w", encoding="utf-8") as dat:
            dat.write(odziv.text)


naslov = r'<span class="worktitle">(?P<naslov>.+?)</span>'
katalog = r'Bach-Werke-Verzeichnis">BWV&nbsp;(?P<katalog>\d+?)</abbr>'
zanr = r'<dt class="col-sm-3">Genre</dt>\n<dd class="col-sm-9">(?P<zanr>.+?)</dd>'
citati_biblije = r'<dt class="col-sm-3">Proper</dt>'
psalm = r'<dd class="col-sm-9">Psalm: .*?(?P<psalm>.+?)</a>'
pismo = r"<br>Epistel: .*?(?P<pismo>.+?)</a>"
evangelij = r"<br>Gospel: .*?(?P<evangelij>.+?)</a>"
#aranzma_seznam = r'<dt class="col-sm-3">Scoring</dt>\n<dd class="col-sm-9">(?P<aranzma_poved>.+?)</dd>'
#aranzma_okrajsava = r'<abbr title="(?P<aranzma_okrajsava>.+?)">\w</abbr>'
aranzma = r'"Scoring":\["(?P<aranzma>.*?)"\]'
nastanek = r'"Date of origin":"(?P<nastanek>\d+?)"'
je_del = r'is part of.*?>(?P<je_del>.+?)</a>'

def repo():
    with open("skladba0001.html", encoding="utf-8") as dat:
        besedilo = dat.read()
        return re.findall(je_del, besedilo)
