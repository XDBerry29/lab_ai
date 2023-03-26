"""
Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii, să se identifice indexul liniei care conține cele mai multe elemente de 1.

De ex. în matricea
[[0,0,0,1,1],
[0,1,1,1,1],
[0,0,1,1,1]]
a doua linie conține cele mai multe elemente 1.
"""
#!!Ai problema facuta in C++ pe leetcode

#folosim cautarea binara

def linie_mare_1(matrice):
    n = len(matrice)
    m = len(matrice[0])
    max_1 = 0
    max_linie = 0

    stanga = 0
    dreapta = m - 1
    index_1 = -1
    #cautam pe prima linie
    while stanga <= dreapta:
            mijloc = (stanga + dreapta) // 2
            if matrice[0][mijloc] == 1:
                index_1 = mijloc
                dreapta = mijloc - 1
            else:
                stanga = mijloc + 1

    #parcurg matricea in jos pe coaloana maximala, daca gasesc un rand mai mare reconfigurez
    for i in range(1,n):
         if matrice[i][index_1] == 1:
            stanga=0
            dreapta=index_1
            while stanga <= dreapta:
                mijloc = (stanga + dreapta) // 2
                if matrice[0][mijloc] == 1:
                    index_1 = mijloc
                    dreapta = mijloc - 1
                else:
                    stanga = mijloc + 1
            max_linie=i

    return max_linie


def test():
    matrice1 = [[0,0,0,1,1],[0,1,1,1,1],[0,0,1,1,1]]
    assert linie_mare_1(matrice1) == 2
    matrice2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1]]
    assert linie_mare_1(matrice2) == 4
    print("All tests passed!")

test()