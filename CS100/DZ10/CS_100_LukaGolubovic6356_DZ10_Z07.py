# Zadatak #7
# Napišite funkciju koja broji koliko puta se svaka reč pojavljuje u datom tekstu. 
# Funkcija treba da vrati listu gde su vrednosti broj ponavljanja reči, poredjani po broju
# ponavljanja u opadajućem redosledu

from collections import Counter

def broj_ponavljanja_reci(tekst):
    reci = tekst.split()
    brojac_reci = Counter(reci)
    brojevi_ponavljanja = list(brojac_reci.values())
    brojevi_ponavljanja.sort(reverse=True)
    return brojevi_ponavljanja

tekst = "Ovo je samo primer teksta gde se ponavljaju neke reci. Ovo je samo primer, nije prava recenica. Sluzi samo za testiranje."

rezultat = broj_ponavljanja_reci(tekst)
print(rezultat)

