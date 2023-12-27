# 12. Napisati funkciju koja prima dve liste brojeva iste dužine. U funkciji se kreira nova lista kod koje se svaki element kreira tako što se pomnože elementi na odgovarajućim pozicijama. Funkcija vraća novokreiranu listu.


def nova_lista(l1, l2):
    if len(l1) != len(l2):
        return None
    return [l1[i] * l2[i] for i in range(len(l1))]


print(nova_lista([1, 2, 3], [4, 5, 6]))
