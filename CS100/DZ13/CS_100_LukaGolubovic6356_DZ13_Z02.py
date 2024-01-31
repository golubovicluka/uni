import getpass


def proveri_korisnika():
    ispravno_korisnicko_ime = "luka1995"
    ispravna_lozinka = "ovonijemojapravalozinka123"

    uneseno_korisnicko_ime = input("Unesite korisnicko ime: ")

    unesena_lozinka = getpass.getpass("Unesite lozinku: ")

    if uneseno_korisnicko_ime == ispravno_korisnicko_ime and unesena_lozinka == ispravna_lozinka:
        print("Prijavljivanje uspešno!")
    else:
        print("Pogrešno korisničko ime ili lozinka. Pokušajte ponovo.")


proveri_korisnika()
