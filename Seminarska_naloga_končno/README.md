# Podatkovna analiza skladb Johanna Sebastiana Bacha

Namen seminarske naloge je zajem in analiza podatkov o skladbah Johanna Sebastiana Bacha.  

Vir podatkov je najbolj uporabljen katalog Bachovih del *Bach-Werke-Verzeichnis* oziroma BWV. Celoten katalog je dostopen na spletni domeni `https://www.bach-digital.de`, kjer je vsako delo arhivirano kot svoj spletni naslov.  
Skripta zajeme vse skladbe vsebovane v 1998 izdaji kataloga, t.j. prvih 1126 skladb.

**Opomba: Skripta mora za zajem podatkov poklicati 1126 posameznih spletnih naslovov, kar traja cca. 5 min.**

`https://www.bach-digital.de` nima povsod konsistentnega html zapisa in podatki so zahtevni za podatkovno analizo (npr. čas nastanka je pogosto napisan kot "pred 1725"). Zato niso zajeti vsi ponujeni podatki in nekateri so lahko nepopolni oziroma nenatančni. Komentarji analize opozorijo na take primere.

## Knjižnice

Skripta uporabi naslednje knjižnice:
- requests
- re
- csv
- pandas
- numpy

## Zagon

Uporabnik naj požene datoteko `main.py` in lahko prične z analizo v `analiza_podatkov.ipynb`.
