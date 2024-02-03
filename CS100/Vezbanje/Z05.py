ime = input("Unesite svo ime: ")
prezime = input("Unesite svo prezime: ")
broj_indeksa = int(input("Unesite svo broj indeksa: "))
smer_studija = input("Unesite smer studija: ")

moguci_smerovi = ["IT", "SE", "RI"]

if broj_indeksa < 0 or len(str(broj_indeksa)) > 5 or smer_studija not in moguci_smerovi:
    print("Broj indeksa mora biti pozitivan, mora biti jedan od IT/SE/RI i sadržati najviše pet znakova.")
else:
    print("Uspesno ste se prijavili!")

if smer_studija == "IT":
    print(f"{ime} {prezime} \n{broj_indeksa} \nInformacione Tehnologije")
elif smer_studija == "SE":
    print(f"{ime} {prezime} \n{broj_indeksa} \nSoftversko inzenjerstvo")
else:
    print(f"{ime} {prezime} \n{broj_indeksa} \nRacunarske igre")

