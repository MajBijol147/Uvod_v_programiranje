zanka, zaustavitveni pogoj = abs((priblizek) ** 2 - n) < eps,  

če št. zaporednih oklepajev (oklepajev brez vmesnega zaklepaja) = št. zaporednih zaklepajev => True

vzame 0 indeks in nato vsak tretji indeks (indeks % k == 0) in vse znake da v en niz

{
1. najde indeks najmanjše teže, 
2. če je edina, vstavi v seznam Zajec(teza[indeks], starost[indeks]), 
3. če ni edini, najde najmanjšo izmed starosti z indeksi enakih tež
4. vstavi v seznam najmanjšega zajca izmed enakih tež
}