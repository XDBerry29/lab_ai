"""
1.Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea într-un text care conține mai multe cuvinte
 separate prin ” ” (spațiu). De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".
"""

def last_word(text):
    cuvinte = text.split()
    cuvinte.sort()
    ultimul_cuvant = cuvinte[-1]
    return ultimul_cuvant


def test_last_word():
    text1 = "ana are mere"
    assert last_word(text1) == "mere"

    text2 = "Ana are mere rosii si galbene"
    assert last_word(text2) == "si"

    print("All tests passed!")

test_last_word()