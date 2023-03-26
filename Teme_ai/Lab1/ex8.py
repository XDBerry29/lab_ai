"""
Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n. De ex. dacă n = 4, numerele sunt: 1, 10, 11, 10
"""

#generam numerele de la 1 la n si apoi le convertim in in binar cu ajutorul fuctiei bin
#metoda este eficienta deoarece bin folosete doar operati logice si de deplasare pe biti


def generare_nr_bin(n):
    sir_binar=[]
    for i in range(1, n+1):
        sir_binar.append(bin(i)[2:]) #folosim [2:] pentru a inlatura "0b" de la inceputul reprezentarii

    return sir_binar

def test_generare_nr_bin():
    assert generare_nr_bin(5) == ['1', '10', '11', '100', '101']
    assert generare_nr_bin(2) == ['1', '10']
    assert generare_nr_bin(1) == ['1']
    assert generare_nr_bin(0) == []
    print("All tests passed!")

test_generare_nr_bin()

n =int(input("Dati n:"))

rez=generare_nr_bin(n)

print(f"Lista numerelor de la 1 la {n} reprezentate binar este: {rez}")
