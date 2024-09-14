nb_essais = 0
intervalle_min = 0
intervalle_max = 1000

def calculer_proposition(min, max):
    """
    Retourne la proposition de nombre
        Parameters:
            min (int): Intervalle minimal inclus
            max (int): Intervalle maximal inclus
        Returns:
            (int) la proposition de nombre pour l'utilisateur
    """
    return (min + max) // 2

def afficher_proposition(nb_propose, nb_essais):
    print(f"Proposition {nb_essais}: {nb_propose}")
    print("""Choisissez une des options suivante:
    = Si le chiffre proposé est correct
    < Si le chiffre proposé est petit
    > Si le chiffre proposé est grand""")
    
def prendre_en_compte_la_reponse_utilisateur(nb_propose):
    while True:
        option_choisie = input("Entrez la bonne option: ")
        match option_choisie:
            case "=":
                return None
            case "<":
                return (nb_propose+1, intervalle_max)
            case ">":
                return (intervalle_min, nb_propose-1)
            case _:
                print("""Option invalide.
Veuillez saisire une option valide""")


while True:
    nb_essais += 1
    nouvelle_proposition = calculer_proposition(intervalle_min, intervalle_max)
    afficher_proposition(nouvelle_proposition, nb_essais)
    nouvelle_intervalle = prendre_en_compte_la_reponse_utilisateur(nouvelle_proposition)
    if nouvelle_intervalle:
        (intervalle_min, intervalle_max) = nouvelle_intervalle
    else:
        break


print(f"Le chiffre {nouvelle_proposition} a été trouvé au bout de {nb_essais} essais")