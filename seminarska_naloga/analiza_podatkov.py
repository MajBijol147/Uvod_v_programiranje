import pandas as pd
import numpy as np

bach = pd.read_csv("podatki_bach.csv", index_col="sifra")

#Skladba z največ različicami
bach.BWV.dropna().astype(int).mode()

#največje število različic in povprečno število različic po žanru
bach_BWVzanr = pd.DataFrame(bach.BWV)
bach_BWVzanr["zanr"] = bach.zanr.values.tolist()
bach_BWVzanr_dropna = bach_BWVzanr.dropna()
bach_BWV_dropna = bach_BWVzanr_dropna.BWV.astype(int)
bach_BWVzanr_dropna["BWV"] = bach_BWVzanr_dropna.BWV.astype(int).values.tolist()
bach_BWVzanr_dropna_modes = bach_BWVzanr_dropna.groupby("zanr").agg(pd.Series.mode)
modes = list()
for BWV in bach_BWVzanr_dropna.groupby("zanr").agg(pd.Series.mode).BWV.values.tolist():
    if type(BWV) is np.ndarray:
        modes.append(list(BWV)[0])
    else:
        modes.append(BWV)
razlicice = list()
for mode in modes:
    razlicice.append(bach_BWV_dropna.value_counts()[mode])
bach_BWVzanr_dropna_modes["max. različic"] = razlicice
bach_BWVzanr_dropna_counts = bach_BWVzanr_dropna.groupby("zanr").agg(
    pd.Series.value_counts
)
povprecja = list()
for BWV in bach_BWVzanr_dropna_counts.BWV.values.tolist():
    if type(BWV) is np.ndarray:
        povprecja.append(BWV.mean())
    else:
        povprecja.append(BWV)
bach_BWVzanr_dropna_modes["povprečje različic"] = povprecja
bach_BWVzanr_dropna_modes  # type:ignore

#število skladb po žanrih
bach_BWVzanr['zanr'] = bach.zanr.values.tolist()
bach_BWVzanr_po_zanr = bach_BWVzanr.dropna().groupby('zanr')
bach_BWVzanr_po_zanr.size()
