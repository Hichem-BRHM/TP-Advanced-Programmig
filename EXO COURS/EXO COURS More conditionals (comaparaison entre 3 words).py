# SOLUTION 1 ...........trouver/afficher le premier mot en ordre alphabétique...................................................................

# Demander à l'utilisateur de saisir trois mots
mot1 = input("Entrez le premier mot : ").lower()
mot2 = input("Entrez le deuxième mot : ").lower()
mot3 = input("Entrez le troisième mot : ").lower()

  # Trouver le mot qui vient en premier par ordre alphabétique
premier = min(mot1, mot2, mot3)


print("Le mot qui vient en premier par ordre alphabétique est :", premier)





# SOLUTION 2 ...........Trier/Afficher les 3 mots en ordre alphabétique.......................................................................
 
"""
 
 # saisir trois mots
mot1 = input("Entrez le premier mot : ").lower()
mot2 = input("Entrez le deuxième mot : ").lower()
mot3 = input("Entrez le troisième mot : ").lower()

# Placer les mots dans une liste
mots = [mot1, mot2, mot3]

# Trier la liste par ordre alphabétique
mots.sort()

print(f"Le mot qui vient en premier par ordre alphabétique est : {mots[0]}")
print(f"Le mot qui vient en deuxiéme par ordre alphabétique est : {mots[1]}")
print(f"Le mot qui vient en troisiéme par ordre alphabétique est : {mots[2]}")

"""