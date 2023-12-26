def je_palindrom(broj):
    if not isinstance(broj, int) or broj <= 0 or broj < 100:
        print("Uneti broj mora biti pozitivan ceo broj sa namanje tri cifre")
        return False
    
    broj_str = str(broj)

    if broj_str == broj_str[::-1]:
        print(f"{broj} je palindrom.")
        return True
    else:
        print(f"{broj} nije palindrom.")
        return False

input_broj = int(input("Unesite pozitivan trocifreni broj (minimalno trocifreni): "))
je_palindrom(input_broj)
