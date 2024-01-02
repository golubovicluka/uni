# 7. Korisnik unosi niz od 10 brojeva i upisuje ih u fajl. Napisati funkciju koja učitava niz iz fajla i pravi novi
# niz koji sadrži kvadrate svakog broja iz originalnog niza. Zatim, funkcija treba da upiše rezultujući niz u drugi
# fajl. Nakon toga, napisati funkciju koja učitava novi niz i prikazuje linijski dijagram koji prikazuje kvadrate
# originalnih brojeva.

import numpy as np
import matplotlib.pyplot as plt


def upisi_brojeve_u_fajl(brojevi, ime_fajla):
    with open(ime_fajla, 'w') as file:
        for broj in brojevi:
            file.write(str(broj) + '\n')


def ucitaj_brojeve_iz_fajla(ime_fajla):
    with open(ime_fajla, 'r') as file:
        brojevi = [float(linija.strip()) for linija in file]
    return np.array(brojevi)


def kvadriraj_brojeve_i_upisi_u_fajl(ulazni_fajl, izlazni_fajl):
    originalni_brojevi = ucitaj_brojeve_iz_fajla(ulazni_fajl)
    kvadrirani_brojevi = np.square(originalni_brojevi)
    upisi_brojeve_u_fajl(kvadrirani_brojevi, izlazni_fajl)


def prikazi_dijagram_kvadratnih_brojeva(izlazni_fajl):
    kvadrirani_brojevi = ucitaj_brojeve_iz_fajla(izlazni_fajl)

    plt.plot(kvadrirani_brojevi, marker='o')
    plt.title('Kvadriranje brojeva')
    plt.xlabel('Indeks')
    plt.ylabel('Vrednost na kvadrat')
    plt.show()


ime_ulaznog_fajla = 'ulazni_brojevi.txt'
ime_izlaznog_fajla = 'kvadrirani_brojevi.txt'

korisnicki_brojevi = [float(input(f"Unesite broj {i + 1}: ")) for i in range(10)]

upisi_brojeve_u_fajl(korisnicki_brojevi, ime_ulaznog_fajla)

kvadriraj_brojeve_i_upisi_u_fajl(ime_ulaznog_fajla, ime_izlaznog_fajla)

prikazi_dijagram_kvadratnih_brojeva(ime_izlaznog_fajla)
