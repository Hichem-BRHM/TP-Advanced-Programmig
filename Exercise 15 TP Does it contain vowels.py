def CHERCHE_Voyelle():
    # Demander une chaîne de caractères en minuscules
    user_string = input("Entrer une chaine : ")
    
    # Liste des voyelles à vérifier
    vowels = ['a', 'e', 'o']
    
    # Vérifier chaque voyelle et afficher si elle est trouvée ou non
    for vowel in vowels:
        if vowel in user_string:
            print(f"{vowel} found")
        else:
            print(f"{vowel} not found")

if __name__ == "__main__":
    CHERCHE_Voyelle()
