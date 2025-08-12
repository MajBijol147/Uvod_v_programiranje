import pandas as pd

bach = pd.read_csv("podatki_bach.csv", index_col="sifra")

# Skladba z največ različicami
bach.BWV.dropna().astype(int).mode()

# Povprečno število različic po žanru
