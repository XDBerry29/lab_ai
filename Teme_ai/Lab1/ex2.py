"""
Să se determine distanța Euclideană între două locații identificate prin perechi de numere. 
De ex. distanța între (1,5) și (4,1) este 5.0
"""

import math


import math

def distanta(x1, y1, x2, y2):
    d = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2) , 2)
    return d

def test_distanta():
    x1, y1, x2, y2 = 1, 5, 4, 1
    expected1 = 5.0
    assert distanta(x1, y1, x2, y2) == 5.0

    x1, y1, x2, y2 = 1, 1, 1, 1
    assert distanta(x1, y1, x2, y2) == 0.0

    print("All tests passed!")



test_distanta()

x1, y1 = map(float, input("Introduceti coordonatele primului punct: ").split())
x2, y2 = map(float, input("Introduceti coordonatele celui de-al doilea punct: ").split())

#calculam dinstanta dintre cele 2 punte

#d = round (d, 2)

print("Distanta intre cele 2 punte este: ",distanta(x1, y1, x2, y2))