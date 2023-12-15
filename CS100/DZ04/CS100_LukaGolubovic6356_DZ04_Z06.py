milja_u_kilometrima = 1.603943
pocetne_milje = 10
zavrsne_milje = 80
razmak_u_miljama = 10

print("Milje   -   Kilometri")
print("----------------------")

for milja in range(pocetne_milje, zavrsne_milje + 1, razmak_u_miljama):
    kilometri = round(milja * milja_u_kilometrima, 2)
    print(f"{milja} milja - {kilometri} km")

print("----------------------")
