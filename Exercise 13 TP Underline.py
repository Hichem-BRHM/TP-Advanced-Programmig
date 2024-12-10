def function():
    while True:
        # Demander une chaîne de caractères à l'utilisateur
        D = input("Enter une chaine que vous voullez : ")
        
        # Si l'entrée est vide, on termine la boucle
        if D == "": # condition exigé par vous
            break
        
        # Afficher la chaîne et son soulignement
        print(D)
        print("-" * len(D))  # Souligner avec autant de '-' que de caractères dans la chaîne comme dans votre exmple

if __name__ == "__main__":
    function()
