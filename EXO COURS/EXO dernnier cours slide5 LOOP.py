
n = input("Please enter a positive integer: ")

# Vérifier si l'entrée est un entier positif
if n.isdigit() and int(n) > 0:
    n = int(n)
    
    # Générer les multiplications
    for i in range(1, n + 1):  # Boucle pour le premier opérande
        for j in range(1, n + 1):  # Boucle pour le deuxième opérande
            print(f"{i} x {j} = {i * j}")
else:
    print("Invalid input. Please enter a positive integer.")
