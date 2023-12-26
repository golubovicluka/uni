def proveri_broj(broj):
    if broj % 7 == 0:
        return True
    else:
        return False


def stampaj_broj(broj):
    if proveri_broj(broj):
        print("Broj je deljiv sa 7.")
    else:
        print("Broj nije deljiv sa 7.")


def unesi_broj():
    while True:
        try:
            broj = int(input("Unesite ceo broj: "))
            return broj
        except ValueError:
            print("Niste uneli ceo broj.")


broj = unesi_broj()
stampaj_broj(broj)
