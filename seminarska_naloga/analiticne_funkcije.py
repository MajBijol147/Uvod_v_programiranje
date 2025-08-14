import pandas as pd
import numpy as np

bach = pd.read_csv("podatki_bach.csv", index_col="sifra")
pd.options.display.max_rows = 20


# Skladba z največ različicami
def najvec_razlicic():
    return bach.BWV.dropna().astype(int).mode()


# največje število različic in povprečno število različic po žanru
def razlicice_zanri():
    bach_BWVzanr = pd.DataFrame(bach.BWV)
    bach_BWVzanr["zanr"] = bach.zanr.values.tolist()
    bach_BWVzanr_dropna = bach_BWVzanr.dropna()
    bach_BWV_dropna = bach_BWVzanr_dropna.BWV.astype(int)
    bach_BWVzanr_dropna["BWV"] = bach_BWVzanr_dropna.BWV.astype(int).values.tolist()
    bach_BWVzanr_dropna_modes = bach_BWVzanr_dropna.groupby("zanr").agg(pd.Series.mode)
    modes = list()
    for BWV in (
        bach_BWVzanr_dropna.groupby("zanr").agg(pd.Series.mode).BWV.values.tolist()
    ):
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
    return bach_BWVzanr_dropna_modes  # type:ignore


# število skladb po žanrih
def skladbe_po_zanri():
    bach_BWVzanr = pd.DataFrame(bach.BWV)
    bach_BWVzanr["zanr"] = bach.zanr.values.tolist()
    bach_BWVzanr_po_zanr = bach_BWVzanr.dropna().groupby("zanr")
    return bach_BWVzanr_po_zanr.size()


# najpogostejši žanr
def najpogostejsi_zanr():
    return bach.zanr.mode()


# število del z citati biblije
def skladbe_z_citati():
    return bach[bach.citati_biblije == "DA"].naslov.count()


# razmerje del z bibličnimi citati glede na žanr
def razmerje_citati_po_zanri_plot():
    bach_zanrbiblija = pd.DataFrame(bach.zanr)
    bach_zanrbiblija["citati biblije"] = bach.citati_biblije.values.tolist()
    a = (
        bach_zanrbiblija.groupby("zanr")
        .value_counts(normalize=True)
        .unstack()
        .dropna()
        .plot(kind="barh", title="pogostost citatov biblije glede na žanr")
        .legend(loc="upper right")
    )
    return a


def razmerje_citati_po_zanri():
    bach_zanrbiblija = pd.DataFrame(bach.zanr)
    bach_zanrbiblija["citati biblije"] = bach.citati_biblije.values.tolist()
    return bach_zanrbiblija.groupby("zanr").value_counts(normalize=True).unstack()


# število skladb po žanrih in njihovi deleži
def delezi_zanrov_plot():
    bach_zanri = pd.DataFrame(bach.zanr)
    glavni_zanri = bach_zanri.value_counts(normalize=True) > 0.03
    bach_glavni_zanri = bach_zanri.value_counts(normalize=True)[glavni_zanri]
    other = pd.Series(data={"(Other)": 0.038}, index=["(Other)"])
    a = pd.concat([bach_glavni_zanri, other]).plot(
        kind="pie", title="deleži glavnih žanrov", autopct="%1.1f%%"
    )
    return a


def delezi_zanrov():
    bach_zanri = pd.DataFrame(bach.zanr)
    return bach_zanri.value_counts()


# najpogosteje skupaj dani biblični odlomki
def modus_odlomki_skupaj():
    odlomki = pd.DataFrame(bach.psalm)
    odlomki["pismo"] = bach.pismo.values.tolist()
    odlomki["evanglij"] = bach.evangelij.values.tolist()
    return odlomki.mode()


# najpogostešji posamezni biblični odlomki
def modus_odlomki_posebej():
    posamezni_odlomki_mode = pd.DataFrame(bach.psalm.mode())
    posamezni_odlomki_mode["pismo"] = bach.pismo.mode().values.tolist()
    posamezni_odlomki_mode["evangelij"] = bach.evangelij.mode().values.tolist()
    return posamezni_odlomki_mode  # type: ignore


# najpogostejši odlomki glede na žanr
def modus_odlomki_po_zanru():
    odlomki = pd.DataFrame(bach.psalm)
    odlomki["pismo"] = bach.pismo.values.tolist()
    odlomki["evanglij"] = bach.evangelij.values.tolist()
    odlomki["zanr"] = bach.zanr.values.tolist()
    return odlomki.dropna().groupby("zanr").agg(pd.Series.mode)


# najpogostejši odlomki glede na leto
def modus_odlomki_po_letu():
    odlomki = pd.DataFrame(bach.psalm)
    odlomki["pismo"] = bach.pismo.values.tolist()
    odlomki["evanglij"] = bach.evangelij.values.tolist()
    odlomki["nastanek"] = bach.nastanek.values.tolist()
    return odlomki.dropna().groupby("nastanek").agg(pd.Series.mode).drop([0])


# najpogostejša zasedba
def modus_zasedba():
    return bach.zasedba.mode()


# 5 najpogostejših zasedb
def modus_5_zasedb():
    return bach.zasedba.value_counts().iloc[0:6]


# število in število pojavitev posameznih glasbil
def posamezna_glasbila_pojavitve_plot():
    glasbila = {}
    for zasedba in bach.zasedba.values.tolist():
        if type(zasedba) is str:
            for glasbilo in zasedba.split(", "):
                if glasbilo not in glasbila:
                    glasbila.update({glasbilo: 1})
                else:
                    glasbila[glasbilo] = glasbila[glasbilo] + 1
        else:
            if zasedba not in glasbila:
                glasbila.update({zasedba: 1})
            else:
                glasbila[zasedba] = glasbila[zasedba] + 1
    glasbila_pojavitve = pd.DataFrame(
        {"glasbilo": glasbila.keys(), "pojavitve": glasbila.values()},
        index=list(glasbila.keys()),
    )
    glasbila_pojavitve_urejeno = glasbila_pojavitve.sort_values(
        "pojavitve", ascending=False
    )
    return glasbila_pojavitve_urejeno.plot(kind="bar", figsize=(20, 5))


def posamezna_glasbila_pojavitve():
    glasbila = {}
    for zasedba in bach.zasedba.values.tolist():
        if type(zasedba) is str:
            for glasbilo in zasedba.split(", "):
                if glasbilo not in glasbila:
                    glasbila.update({glasbilo: 1})
                else:
                    glasbila[glasbilo] = glasbila[glasbilo] + 1
        else:
            if zasedba not in glasbila:
                glasbila.update({zasedba: 1})
            else:
                glasbila[zasedba] = glasbila[zasedba] + 1
    glasbila_pojavitve = pd.DataFrame(
        {"glasbilo": glasbila.keys(), "pojavitve": glasbila.values()},
        index=list(glasbila.keys()),
    )
    glasbila_pojavitve_urejeno = glasbila_pojavitve.sort_values(
        "pojavitve", ascending=False
    )
    return glasbila_pojavitve_urejeno


# skladba z največjo zasedbo (+ velikost in zasedba)
def skladba_najvecja_zasedba():
    naslov_zasedba = pd.DataFrame(bach.naslov)
    naslov_zasedba["zasedba"] = bach.zasedba.values.tolist()
    naslov_zasedba = naslov_zasedba.dropna()
    velikost = 0
    instrumenti = ""
    dolzine = []
    for zasedba in naslov_zasedba.zasedba.tolist():
        dolzina = len(zasedba.split(","))
        dolzine.append(dolzina)
        if velikost < dolzina:
            velikost = dolzina
            instrumenti = zasedba
    naslov_zasedba["velikost"] = dolzine
    i = naslov_zasedba.index[naslov_zasedba["zasedba"] == instrumenti]
    return naslov_zasedba.loc[i]


# povprečna velikost zasedbe po žanru
def povprecna_velikost_zasedbe_po_zanru_plot():
    velikost_zasedbe_po_zanru = pd.DataFrame(bach.zasedba)
    velikost_zasedbe_po_zanru["zanr"] = bach.zanr.values.tolist()
    velikost_zasedbe_po_zanru = velikost_zasedbe_po_zanru.dropna()
    velikost = []
    for zasedba in velikost_zasedbe_po_zanru.zasedba.values.tolist():
        velikost.append(len(zasedba.split(",")))
    velikost_zasedbe_po_zanru["povprečje"] = velikost
    povp_zasedbe_po_zanru = (
        velikost_zasedbe_po_zanru[["zanr", "povprečje"]]
        .groupby("zanr")
        .agg(pd.Series.mean)
    )
    return povp_zasedbe_po_zanru.plot(kind="barh")


def povprecna_velikost_zasedbe_po_zanru():
    velikost_zasedbe_po_zanru = pd.DataFrame(bach.zasedba)
    velikost_zasedbe_po_zanru["zanr"] = bach.zanr.values.tolist()
    velikost_zasedbe_po_zanru = velikost_zasedbe_po_zanru.dropna()
    velikost = []
    for zasedba in velikost_zasedbe_po_zanru.zasedba.values.tolist():
        velikost.append(len(zasedba.split(",")))
    velikost_zasedbe_po_zanru["povprečje"] = velikost
    povp_zasedbe_po_zanru = (
        velikost_zasedbe_po_zanru[["zanr", "povprečje"]]
        .groupby("zanr")
        .agg(pd.Series.mean)
    )
    return povp_zasedbe_po_zanru


# povprečna velikost zasedbe na leto
def povprecna_velikost_zasedbe_po_letu():
    zasedba_po_letu = pd.DataFrame(bach.zasedba)
    zasedba_po_letu["leto"] = bach.leto.values.tolist()
    zasedba_po_letu = zasedba_po_letu[zasedba_po_letu.leto != 0000].dropna()
    velikost = []
    for zasedba in zasedba_po_letu.zasedba.values.tolist():
        velikost.append(len(zasedba.split(",")))
    zasedba_po_letu["povprečna velikost"] = velikost
    return (
        zasedba_po_letu[["leto", "povprečna velikost"]]
        .groupby("leto")
        .agg(pd.Series.mean)
        .plot(kind="line")
    )


# število skladb na leto
def skladbe_na_leto():
    return (
        bach.leto[bach.leto != 0000]
        .dropna()
        .value_counts()
        .sort_index()
        .plot(kind="line")
    )


# najpogostejše povezave
def najpogostejse_povezave():
    return bach.povezave.value_counts()[:10]


# največje število povezav in skladbe z največ povezavami
def skladbe_najvec_povezav():
    povezave = pd.DataFrame(bach.naslov)
    povezave["povezave"] = bach.povezave.values.tolist()
    povezave = povezave.dropna()
    največ_povezav = 0
    št_povezav = []
    for povezava in povezave.povezave.values.tolist():
        št_povezav.append(len(povezava.split(",")))
        if len(povezava.split(",")) > največ_povezav:
            največ_povezav = len(povezava.split(","))
    povezave["število povezav"] = št_povezav
    print(f"Največ povezav: {največ_povezav}")
    return bach.loc[
        povezave.index[povezave["število povezav"] == max(št_povezav)].tolist()
    ][["naslov", "BWV"]]


# najdaljši in najkrajši naslov
def najdalsi_najkrajsi_naslov():
    naslov = pd.DataFrame(bach.naslov)
    naslov = naslov.dropna()
    najdaljši_naslov = 0
    najkrajši_naslov = 100
    dolžine = []
    for ime in naslov.values.tolist():
        dolžina = len(ime[0])
        dolžine.append(dolžina)
        if dolžina > najdaljši_naslov:
            najdaljši_naslov = dolžina
        if dolžina < najkrajši_naslov:
            najkrajši_naslov = dolžina
    naslov["dolžine"] = dolžine
    naslov1 = naslov.loc[naslov.index[naslov["dolžine"] == najdaljši_naslov]]
    naslov2 = naslov.loc[naslov.index[naslov["dolžine"] == najkrajši_naslov]]
    return pd.concat([naslov1, naslov2])
