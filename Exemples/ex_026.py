grille = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for ligne in grille:  # Première boucle pour chaque ligne
    for element in ligne:  # Boucle imbriquée pour chaque élément de la ligne
        print(element, end=" ")  # Afficher chaque élément sur la même ligne
    print()  # Sauter une ligne après chaque ligne de la grille