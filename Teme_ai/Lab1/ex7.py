"""
Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n). 
De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.
"""

#Sortez sirul descrescator si returnez al k-1 el

def kcelmaimare(lst,k):
    lst.sort(reverse=True)
    return lst[k-1]

def test_kcelmaimare():
    assert kcelmaimare([1, 2, 3, 4, 5], 3) == 3
    assert kcelmaimare([10, 2, 8, 4, 5], 1) == 10
    assert kcelmaimare([1, 1, 2, 3, 3, 3], 2) == 3
    assert kcelmaimare([5], 1) == 5
    print("All tests passed!")

test_kcelmaimare() 

lista = list(map(int, input("Dati sirul: ").split()))
k = int(input("Dati k:"))

rez = kcelmaimare(lista,k)


print(f"Al k-lea cel mai mare el al sirului: {lista} este {rez}")
