input_broj = int(input("Unesite pozitivan ceo broj: "))

faktorijel = 1
for i in range(1, input_broj+1):
    faktorijel *= i

print(f"Faktorijel broja {input_broj} je: {faktorijel}")
