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
# vsaka skladba je svoja spletna stran, zato mora program poklicati 1126
#   posameznih strani, kar je časovno zamudno
def pobiranje_html():
    for x in range(1, 1126 + 1):
        print(x)
        pravo_st = url_stevilo(x)
        url = f"""https://www.bach-digital.de/receive/BachDigitalWork_work_0000
                {pravo_st}?lang=en"""
        odziv = requests.get(url, timeout=5, headers=headers)
        # timeout je bugfix
        with open(f"skladba{pravo_st}.html", "w", encoding="utf-8") as dat:
            dat.write(odziv.text)
