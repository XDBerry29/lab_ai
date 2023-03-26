"""
Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate din coordonatele 
a 2 căsuțe din matrice ((p,q) și (r,s)), să se calculeze suma elementelor din sub-matricile identificate de fieare pereche.

De ex, pt matricea
[[0, 2, 5, 4, 1],
[4, 8, 2, 3, 7],
[6, 3, 4, 6, 2],
[7, 3, 1, 8, 3],
[1, 5, 7, 9, 4]]
și lista de perechi ((1, 1) și (3, 3)), ((2, 2) și (4, 4)), 
suma elementelor din prima sub-matrice este 38, iar suma elementelor din a 2-a sub-matrice este 44.

"""

#Folosim un altogritm de sume partiale pe matirce

def mat_sum_partiala(matrice):

    n = len(matrice)
    m = len(matrice[0])

    # construim matricea sumelor partiala
    #initializam cu 0
    suma_partiala = [[0 for j in range(m)] for i in range(n)]

    #construim primul rand si prima coloana
    suma_partiala[0][0] = matrice[0][0]
    for i in range(1, n):
        suma_partiala[i][0] = suma_partiala[i-1][0] + matrice[i][0]
    for j in range(1, m):
        suma_partiala[0][j] = suma_partiala[0][j-1] + matrice[0][j]

   #construim restul matrici     
    for i in range(1, n):
        for j in range(1, m):
            suma_partiala[i][j] = suma_partiala[i-1][j] + suma_partiala[i][j-1] - suma_partiala[i-1][j-1] + matrice[i][j]

    return suma_partiala


#in matricea de sume pariale valoarea din (i,j) reprezinta suma tuturor elementelor din matricea de coordonate (0,0) (i,j)

def suma_submatricii(matrice, perechi):

    suma_partiala =mat_sum_partiala(matrice)

    rez = []
    for pereche in perechi:
        (p, q), (r, s) = pereche
        #calculam suma din matricea de coordonate (p, q), (r, s) cu ajutorul matricei de sume partiale
        suma = suma_partiala[r][s] - suma_partiala[r][q-1] - suma_partiala[p-1][s] + suma_partiala[p-1][q-1]
        rez.append(suma)
    return rez


def test_suma_submatricii():
    matrice = [[0, 2, 5, 4, 1], [4, 8, 2, 3, 7], [6, 3, 4, 6, 2], [7, 3, 1, 8, 3], [1, 5, 7, 9, 4]]
    perechi = [((1, 1), (3, 3)), ((2, 2), (4, 4))]
    assert suma_submatricii(matrice, perechi) == [19, 23]
    print("All tests passed!")


