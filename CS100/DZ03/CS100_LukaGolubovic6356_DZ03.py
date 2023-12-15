temperatura_vode = float(input("Unesite temperature vode: "))

if temperatura_vode > 0 and temperatura_vode < 100:
    print(f"Na temperaturi {temperatura_vode} stepeni Celsiusa, agregatno stanje je tečno")
elif temperatura_vode >= 100:
    print(f"Na temperaturi {temperatura_vode} stepeni Celsiusa, agregatno stanje je gasovito")
else:
    print(f"Na temperaturi {temperatura_vode} stepeni Celsiusa, agregatno stanje je čvrsto")
