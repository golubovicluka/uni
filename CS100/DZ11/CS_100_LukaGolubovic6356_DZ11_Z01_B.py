# b) Napisati program koji od korisnika zahteva da unese ključeve u rečniku. Nakon toga korisniku prikazivati
# ključeve iz rečnika i tražiti od korisnika da unese vrednosti koje imaju ti ključevi. Na kraju prikazati ceo rečnik.

def unos_recnika():
    recnik = {}
    broj_kljuceva = int(input("Unesite broj ključeva u rečniku: "))

    for _ in range(broj_kljuceva):
        kljuc = input("Unesite kljuc: ")
        vrednost = input(f"Unesite vrednost za kljuc '{kljuc}': ")
        recnik[kljuc] = vrednost

    return recnik


kreirani_recnik = unos_recnika()

print("\nUneti ključevi i vrednosti u rečniku su:")
for kljuc, vrednost in kreirani_recnik.items():
    print(f"{kljuc}: {vrednost}")
