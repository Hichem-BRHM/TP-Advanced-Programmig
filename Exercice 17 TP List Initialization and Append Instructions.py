# 2 list vide 
numbers = []
shoe_sizes = []

# Ajout des éléments à la liste "numbers" avec append
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

# Ajout des éléments à la liste "shoe_sizes" avec append
shoe_sizes.append(8)
shoe_sizes.append(9)
shoe_sizes.append(10)
shoe_sizes.append(11)
shoe_sizes.append(12)

# coté Affichage 
print("Liste des nombres :", numbers)
print("Liste des tailles de chaussures :", shoe_sizes)

# Bonus     GESTION DOUBLONS 
# cas1 : accepter doublons ......où Ajout de doublons dans numbers
numbers.append(3)
numbers.append(5)
print("\nListe numbers avec doublons :", numbers)

# cas 2 : Suppression des doublons dans numbers
numbers = list(set(numbers))
print("Liste nombers sans doublons :", numbers)

# Bonus : Utilisation d'une boucle pour remplir shoe_sizes au lieu d'écrire "append" n-fois
shoe_sizes = []  
for size in range(8, 13):
    shoe_sizes.append(size)
print("\nListe des tailles de chaussures:", shoe_sizes)

# Bonus : Création d'une troisième liste qui concatine/combine numbers et shoe_sizes
list = numbers + shoe_sizes  # ou bien......list = shoe_sizes + numbers
print("\nListe combinée :", list)
