import pandas as pd
import random

# Liste de noms fictifs
prenoms = ["Jade", "Louise", "Ambre", "Alba", "Emma", "Rose", "Alice", "Romy", "Anna", "Lina", "Léna", "Mia", "Lou", "Julia", "Chloé", "Alma", "Agathe", "Iris", "Inaya", "Charlie", "Juliette", "Léa", "Victoire", "Luna", "Giulia", "Adèle", "Jeanne", "Nina", "Eva", "Olivia", "Zoé", "Léonie", "Romane", "Victoria", "Nour", "Lya", "Inès", "Lucie", "Lyana", "Lola", "Alix", "Charlotte", "Mila", "Sofia", "Louna", "Margaux", "Ava", "Elena", "Emy", "Mya", "Gabriel", "Léo", "Raphaël", "Maël", "Louis", "Noah", "Jules", "Arthur", "Adam", "Lucas", "Liam", "Sacha", "Isaac", "Gabin", "Eden", "Hugo", "Naël", "Aaron", "Mohamed", "Léon", "Paul", "Noé", "Marceau", "Ethan", "Nathan", "Théo", "Tom", "Nino", "Marius", "Ayden", "Malo", "Mathis", "Gaspard", "Martin", "Lyam", "Victor", "Rayan", "Elio", "Timéo", "Eliott", "Milo", "Robin", "Tiago", "Valentin", "Ibrahim", "Axel", "Augustin", "Amir", "Enzo", "Imran"]

noms = ["Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Laurent", "Simon", "Michel", "Lefebvre", "Leroy", "Roux", "David", "Bertrand", "Morel", "Fournier", "Girard", "Bonnet", "Dupont", "Lambert", "Fontaine", "Rousseau", "Vincent", "Muller", "Lefevre", "Faure", "Andre", "Mercier", "Blanc", "Guerin", "Boyer", "Garnier", "Chevalier", "Francois", "Legrand", "Gauthier", "Garcia", "Perrin", "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Gautier", "Masson", "Marchand", "Duval", "Denis", "Dumont", "Marie", "Lemaire", "Noel", "Meyer", "Dufour", "Meunier", "Brun", "Blanchard", "Giraud", "Joly", "Riviere", "Lucas", "Brunet", "Gaillard", "Barbier", "Arnaud", "Martinez", "Gerard", "Roche", "Renard", "Schmitt", "Roy", "Leroux", "Colin", "Vidal", "Caron", "Picard", "Roger", "Fabre", "Aubert", "Lemoine", "Renaud", "Dumas", "Lacroix", "Olivier", "Philippe", "Bourgeois", "Pierre", "Benoit", "Rey", "Leclerc", "Payet", "Rolland", "Leclercq", "Guillaume", "Lecomte"]

# Liste d'activités sportives
activites = ['Football', 'Basketball', 'Tennis', 'Natation', 'Cyclisme', 'Course', 'Escalade', 'Judo', 'Karaté', 'Handball', 'Golf']

def generer_dataframe(nb_lignes: int):
    # Génération des données fictives
    data = {
        'Prenom': [random.choice(prenoms) for _ in range(nb_lignes)],
        'Nom': [random.choice(noms) for _ in range(nb_lignes)],
        'Age': [random.randint(18, 65) for _ in range(nb_lignes)],  # Âge entre 18 et 65 ans
        'Activite': [random.choice(activites) for _ in range(nb_lignes)],  # Activités aléatoires
        'Inscription': [random.choice([True, False]) for _ in range(nb_lignes)]  # Statut d'inscription aléatoire
    }

    return pd.DataFrame(data)
