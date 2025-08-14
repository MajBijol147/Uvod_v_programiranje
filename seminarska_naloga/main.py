from pobiranje_podatkov import poberi_html, izlusci_podatke, shrani_csv


def main():
    html = poberi_html()
    podatki = izlusci_podatke()
    csv = shrani_csv()


if __name__ == "__main__":
    main()
