# Initialisation de l'ensemble pour les mots uniques
unique_words = set()
total_words = 0  # Compteur pour tous les mots saisis

def demander_mot():
    return input("Entrez un mot : ").strip().lower()  # Rendre insensible à la casse

while True:
    mot = demander_mot()
    total_words += 1  # Incrémenter le compteur total

    # Vérifier si le mot est déjà dans l'ensemble
    if mot in unique_words:
        print(f"Vous avez saisi {len(unique_words)} mots uniques.")
        print(f"Nombre total de mots saisis : {total_words}")
        break

    # Ajouter le mot à l'ensemble
    unique_words.add(mot)

# Bonus : Afficher les mots uniques dans l'ordre alphabétique
print("Mots uniques (par ordre alphabétique)  :", sorted(unique_words))

# Enregistrer les mots uniques dans un fichier
with open("mots_uniques.txt", "w") as fichier:
    fichier.write("\n".join(sorted(unique_words)))
print("Les mots uniques ont été enregistrés dans 'mots_uniques.txt'.")

