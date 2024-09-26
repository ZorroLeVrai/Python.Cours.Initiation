#def incrementer(x):
#    return x + 1

ma_liste = [2, 3, 5, 7, 11, 13, 17]

#lambda liste_de_parametres:valeur_retournée
resultat = map(lambda x: x+1, ma_liste)
print(list(resultat))

