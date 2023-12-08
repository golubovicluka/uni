# Pitati korisnika da unese dva broja
prvi_broj = float(input("Unesite prvi broj: "))
drugi_broj = float(input("Unesite drugi broj: "))

# Zamena mesta brojeva
temp = prvi_broj
prvi_broj = drugi_broj
drugi_broj = temp

# Prikaz brojeva
print(prvi_broj)
print(drugi_broj)
