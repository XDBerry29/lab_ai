"""
Să se determine cuvintele unui text care apar exact o singură dată în acel text.
De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.
"""

def cuvinte_unice(text):
    cuvinte = text.split()
    aparitii = {}
    for cuvant in cuvinte:
        if cuvant in aparitii:
            aparitii[cuvant] += 1
        else:
            aparitii[cuvant] = 1
    cuvinte_unice = []
    for cuvant, numar_aparitii in aparitii.items():
        if numar_aparitii == 1:
            cuvinte_unice.append(cuvant)
    
    return cuvinte_unice


def test_cuvinte_unice():
    assert cuvinte_unice("ana are ana are mere rosii ana") == ['mere', 'rosii']
    assert cuvinte_unice("Ana are mere verzi si galbene dar are si mere rosii") == ['Ana','verzi', 'galbene', 'dar', 'rosii']
    assert cuvinte_unice("c c c") == []
    print("All tests passed!")


test_cuvinte_unice()