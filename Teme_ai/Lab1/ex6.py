"""
Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul majoritar (care apare de mai mult de n / 2 ori). 
De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].
"""

#folosim algoritmul Booyer-Moore (daca ni se garanteaza ca exita un el majoritar)

def BooyerMoore(lst):
    candidat=None
    contor=0
    for el in lst:
        if contor == 0:
            candidat = el
            contor = 1
        elif el == candidat:
            contor += 1
        else:
            contor -= 1
    
    return candidat

def test_BooyerMoore():
    assert BooyerMoore([1, 2, 2, 3, 2, 4, 2, 5, 2]) == 2
    assert BooyerMoore([1, 1, 1, 1]) == 1
    assert BooyerMoore([2,8,7,2,2,5,2,3,1,2,2]) == 2
    print("All tests passed!")


test_BooyerMoore()

lista = list(map(int, input("Dati sirul: ").split()))

el_maj = BooyerMoore(lista)

print(f"Elementul majoritar al sirului: {lista} este {el_maj}")

            
