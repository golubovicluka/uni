def upisi_brojeve_u_datoteku(ime_datoteke, n):
    datoteka = open(ime_datoteke, 'w')
    for i in range(n):
        datoteka.write(str(i) + '\n')
    datoteka.close()


def izracunaj_zbir(ime_datoteke):
    datoteka = open(ime_datoteke, 'r')
    linije = datoteka.readlines()
    datoteka.close()

    for i in range(len(linije) - 1):
        broj1 = int(linije[i].strip())
        broj2 = int(linije[i + 1].strip())
        zbir = broj1 + broj2
        print(zbir)


ime_datoteke = 'sabiranje_brojeva.txt'
n = 10

upisi_brojeve_u_datoteku(ime_datoteke, n)
izracunaj_zbir(ime_datoteke)
