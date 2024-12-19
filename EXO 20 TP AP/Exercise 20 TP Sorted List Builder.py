import statistics

# Initialisation de la liste vide
user_list = []

# Charger la liste depuis un fichier si elle existe
try:
    with open("user_list.txt", "r") as fichier:
        # Lire les lignes et les convertir en entiers
        user_list = [int(ligne.strip()) for ligne in fichier.readlines()]
        print("Liste chargée depuis le fichier.")
except FileNotFoundError:
    print("Aucun fichier trouvé, démarrage avec une liste vide.")

# Demander à l'utilisateur d'entrer des nombres
while True:
    user_input = input("Entrez un nombre (ou 0 pour arrêter) : ")

    # Vérifier si l'entrée est un nombre entier
    try:
        number = int(user_input)
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    # Si l'utilisateur entre 0, on arrête
    if number == 0:
        break

    # Ajouter le nombre à la liste
    user_list.append(number)

    # Afficher la liste actuelle
    print(f"Liste actuelle : {user_list}")

    # Afficher la liste triée par ordre croissant
    sorted_list = sorted(user_list)
    print(f"Liste triée (ordre croissant) : {sorted_list}")

# Afficher les statistiques sur la liste
if user_list:
    mean = statistics.mean(user_list)
    median = statistics.median(user_list)
    print(f"\nStatistiques de la liste :")
    print(f"Moyenne : {mean}")
    print(f"Médiane : {median}")

# Option pour enregistrer toute la liste dans le fichier
sauvegarder = input("Voulez-vous sauvegarder toute la liste dans un fichier ? (oui/non) ").strip().lower()

if sauvegarder == "oui":
    with open("user_list.txt", "w") as fichier:  # 'w' pour écraser et réécrire toute la liste
        fichier.write("\n".join(map(str, user_list)) + "\n")  # Sauvegarde toute la liste
    print("La liste complète a été sauvegardée dans le fichier 'user_list.txt'.")
