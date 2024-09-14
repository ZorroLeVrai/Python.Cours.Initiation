from calcul import add

def test_add():
    assert add(2, 3) == 5  # Vérifie que 2 + 3 donne bien 5
    assert add(-1, 1) == 0  # Vérifie que -1 + 1 donne bien 0
    assert add(0, 0) == 0   # Vérifie que 0 + 0 donne bien 0