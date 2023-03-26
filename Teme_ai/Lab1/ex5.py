"""
Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} 
astfel încât o singură valoare se repetă de două ori, să se identifice acea valoare care se repetă. 
De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.
"""

#Cum numerele sunt aiartin unui sir de la 1 la n-1 putem folosii suma gaus pt a det nr duplicat (n-1)*n/2


def nrdup(sir):
    n=len(sir)
    suma_gaus=n*(n-1)//2 #suma elementelor unice pana la n-1
    suma_sir=sum(sir) #suma totala a el din sir
    return suma_sir-suma_gaus


def test_nrdup():
    assert nrdup([1, 2, 3, 4, 2]) == 2
    assert nrdup([1, 2, 3, 4, 4]) == 4
    print("All tests passed!")

test_nrdup()



sir = list(map(int, input("Dati sirul: ").split()))

dup=nrdup(sir)

print(f"Nr. duplicat din sirul {sir} este {dup}.")

