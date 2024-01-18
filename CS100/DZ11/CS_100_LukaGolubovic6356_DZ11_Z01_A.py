# a) Pronaći minimalnu i maksimalnu vrednost u skupu. Ukoliko su elementi skupa stringovi, minimalna vrednost je ona
# koja ima najkraći naziv, a maksimalna ona sa najdužim nazivom.

def min_max_vrednost(skup):
    if all(isinstance(element, str) for element in skup):
        min_vrednost = min(skup, key=len)
        max_vrednost = max(skup, key=len)
    else:
        min_vrednost = min(skup)
        max_vrednost = max(skup)

    return min_vrednost, max_vrednost


skup_stringova = {"jabuka", "banana", "kivi", "mandarina"}

min_v, max_v = min_max_vrednost(skup_stringova)
print(f"Minimalna vrednost: {min_v}")
print(f"Maksimalna vrednost: {max_v}")
