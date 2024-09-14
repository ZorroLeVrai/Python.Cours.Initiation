def inverser_chaine(texte):
    nombre_caracteres = len(texte)
    chaine_resultat = ""

    for index in range(nombre_caracteres-1, -1, -1):
        chaine_resultat += texte[index]

    return chaine_resultat


def inverser_chaine2(texte):
    chaine_resultat = ""

    for caractere in reversed(texte):
        chaine_resultat += caractere

    return chaine_resultat


def inverser_chaine3(texte):
    return "".join(reversed(texte))


def inverser_chaine4(texte):
    return texte[::-1]

print(inverser_chaine("Bonjour!"))
print(inverser_chaine2("Bonjour!"))
print(inverser_chaine3("Bonjour!"))
print(inverser_chaine4("Bonjour!"))