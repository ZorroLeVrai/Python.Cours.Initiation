def estDivisible(numerateur, denominateur):
    return (numerateur % denominateur == 0)

def transformer_nombre(nombre):
    resultat = ""
    if estDivisible(nombre, 3):
        resultat += "Fizz"
    if estDivisible(nombre, 5):
        resultat += "Buzz"

    if resultat == "":
        return str(nombre)
    return resultat
    
def generer_fizz_buzz(nombre_max):
    liste_resultat = []
    for nombre in range(1, nombre_max+1):
        liste_resultat.append(transformer_nombre(nombre))
    
    return liste_resultat

def generer_fizz_buzz2(nombre_max):
    liste_nombres = list(range(1, nombre_max+1))
    liste_resultat = list(map(transformer_nombre, liste_nombres))
    return liste_resultat


liste_resultat = generer_fizz_buzz(30)
print(liste_resultat)

#print("\n".join(liste_resultat))
