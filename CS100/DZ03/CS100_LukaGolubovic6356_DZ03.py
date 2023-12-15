temperatura_vode = float(input("Unesite temperature vode: "))

if temperatura_vode > 0 and temperatura_vode < 100:
    print("Agregatno stanje je tečno")
elif temperatura_vode >= 100:
    print("Agregatno stanje je gasovito")
else:
    print("Agregatno stanje je čvrsto")
