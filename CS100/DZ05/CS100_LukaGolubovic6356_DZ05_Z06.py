def najmanji_broj_novcica(iznos, novcici):
    novcici.sort(reverse=True)
    
    broj_novcica = 0
    resenje = []

    for novcic in novcici:
        broj_trenutnih_novcica = iznos // novcic
        broj_novcica += broj_trenutnih_novcica
        iznos %= novcic
        resenje.extend([novcic] * broj_trenutnih_novcica)
    
    if iznos == 0:
        return broj_novcica, resenje
    else:
        return -1, []

iznos = int(input("Unesite iznos u centima: "))
novcici = [25, 10, 5, 1]

rezultat, kombinacija = najmanji_broj_novcica(iznos, novcici)

if rezultat != -1:
    print(f"Najmanji broj novčića potrebnih za iznos od {iznos} centi je {rezultat}.")
    print(f"Kombinacija novčića: {kombinacija}")
else:
    print(f"Nije moguće sastaviti iznos od {iznos} centi koristeći zadate novčiće.")
