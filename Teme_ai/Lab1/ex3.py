"""
Să se determine produsul scalar a doi vectori rari care conțin numere reale.
 Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea oricâte dimensiuni.
 De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.

"""
def produs_scalar(vector1, vector2):
    if len(vector1) != len(vector2):
        print("Cele doua liste nu au aceeasi lungime!")
        return None
    else:
        produs_scalar_vectori = 0
        for elem1, elem2 in zip(vector1, vector2):
            produs_scalar_vectori += elem1 * elem2
        return produs_scalar_vectori

def test_produs_scalar():
    # Test 1
    vector1 = [1, 0, 2, 0, 3]
    vector2 = [1, 2, 0, 3, 1]
    assert produs_scalar(vector1, vector2) == 4

    # Test 2
    vector1 = [0, 1, 0, 1]
    vector2 = [0, 1, 0, 1]
    assert produs_scalar(vector1, vector2) == 2

    print("All tests passed!")

test_produs_scalar()