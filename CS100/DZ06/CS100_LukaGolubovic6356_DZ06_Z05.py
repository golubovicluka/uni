def kopiraj_blok_po_blok(ulazna_datoteka, izlazna_datoteka, velicina_bloka):
    if velicina_bloka not in [1024, 2048, 4096, 8192]:
        print("Uneta velicina bloka nije validna.")
        return
    
    with open(ulazna_datoteka, 'rb') as ulaz:
        with open(izlazna_datoteka, 'wb') as izlaz:
            while True:
                blok = ulaz.read(velicina_bloka)
                if not blok:
                    break
                izlaz.write(blok)

    print("Kopiranje binarne datoteke uspesno zavrseno.")

velicina_bloka = int(input("Unesite velicinu bloka (1024, 2048, 4096, 8192): "))
if velicina_bloka not in [1024, 2048, 4096, 8192]:
    print("Uneta velicina bloka nije validna.")
else:
    ulazna_datoteka = input("Unesite ime ulazne binarne datoteke: ")
    izlazna_datoteka = input("Unesite ime izlazne binarne datoteke: ")

    kopiraj_blok_po_blok(ulazna_datoteka, izlazna_datoteka, velicina_bloka)

