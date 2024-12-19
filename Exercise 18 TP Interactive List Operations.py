# Initialisation de la liste
numbers = [1, 2, 3, 4, 5]

def afficher_menu():
    print("\nMenu :")
    print("1. Append (ajouter un élément à la fin)")
    print("2. Insert (ajouter un élément à une position spécifique)")
    print("3. Pop (supprimer le dernier élément)")
    print("4. Remove (supprimer un élément spécifique)")
    print("5. Quit (quitter le programme)")

while True:
    print("\nListe actuelle :", numbers)
    afficher_menu()

    choix = int(input("Choisissez une option : "))

    if choix == 1:
        # Append
        valeur = input("Entrez une valeur à ajouter : ")
        
        # Verifier si la valeur est un entier sinon un new message pour entrer une nouvelle valeur 
        if not valeur.isdigit():
            print("Invalid value. Please enter an integer in next operation")
            continue# Verifier si la valeur est un entier sinon un new message pour entrer une nouvelle valeur 
        
        numbers.append(valeur)
        print("Valeur ajoutée.")
        

    elif choix == 2:
        # Insert
        valeur = int(input("Entrez une valeur à insérer : "))
        index = int(input("Entrez l'index : "))


        if 0 <= index <= len(numbers):
            numbers.insert(index, valeur)
            print("Valeur insérée.")
        else:
            print("Index hors limite.")

    elif choix == 3:
        # Pop
        if numbers:
            valeur_supprimee = numbers.pop()
            print(f"Valeur supprimée : {valeur_supprimee}")
        else:
            print("La liste est vide, impossible de supprimer.")

    elif choix == 4:
        # Remove
        valeur = int(input("Entrez la valeur à supprimer : "))

        if valeur in numbers:
            numbers.remove(valeur)
            print("Valeur supprimée.")
        else:
            print("Valeur non trouvée dans la liste.")

    elif choix == 5:
        # Quit
        print("Programme terminé.")
        break

    else:
        print("Option invalide. Veuillez choisir une option entre 1 et 5.")
