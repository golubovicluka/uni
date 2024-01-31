def ponavljanje(rec, tekst):
    if not tekst:
        return 0

    if tekst.startswith(rec):
        return 1 + ponavljanje(rec, tekst[len(rec):])
    else:
        return ponavljanje(rec, tekst[1:])


rec = "test"
tekst = "testiranje test test test, tekst test"

rezultat = ponavljanje(rec, tekst.lower())
print(f"Rec '{rec}' se pojavljuje {rezultat} puta u tekstu.")
