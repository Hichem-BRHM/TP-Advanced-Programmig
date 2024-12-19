def length(lst):
    
    #Retourne le nombre d'éléments dans la liste.
    
    if not isinstance(lst, list):
        raise ValueError("L'entrée doit être une list.")
    return len(lst)


def mean(lst):
    
    #Calcule la moyenne arithmétique des éléments de la liste.
    if not isinstance(lst, list):
        raise ValueError("L'entrée doit être une list.")
    if not lst:
        raise ValueError("list vide.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Tous les éléments de la liste doivent être numérique et pas alphétique.")
    return sum(lst) / len(lst)  # expression de la moyenne 


def range_of_list(lst):
    
    # return le range qui est : la différence entre la valeur maximale et la valeur minimale de la liste.
    
    if not isinstance(lst, list):
        raise ValueError("L'entrée doit être une liste.")
    if not lst:
        raise ValueError("La list est vide.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Tous les éléments de la liste doivent être numériques.")
    return max(lst) - min(lst)


def median(lst):
    
    # Calcule la médiane des éléments de la liste.
    
    if not isinstance(lst, list):
        raise ValueError("L'entrée doit être une liste.")
    if not lst:
        raise ValueError("La liste est vide.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Tous les éléments de la liste doivent être numériques.")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:  # cas1. nombre impair / longueur list impair
        return sorted_lst[n // 2]
    else:  # 2. nombre pair / longueur list pair
        mid1, mid2 = sorted_lst[n // 2 - 1], sorted_lst[n // 2]
        return (mid1 + mid2) / 2


def standard_deviation(lst):
    
    # Calcule l'écart-type des éléments de la liste.
    
    if not isinstance(lst, list):
        raise ValueError("L'entrée doit être une liste.")
    if not lst:
        raise ValueError("La liste est vide.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Tous les éléments de la liste doivent être numériques.")
    m = mean(lst)
    squared_differences = [(x - m) ** 2 for x in lst]
    variance = sum(squared_differences) / len(lst)
    return variance ** 0.5


def list_statistics(lst):
    
    # Retourne un dictionnaire contenant toutes les statistiques calculées 
    
    return {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst)
    }


# Tests avec différentes listes

# 1. test d'une list connu 'positif_entier'
numbers = [1, 2, 3, 4, 5]
print("Liste :", numbers)
print("Longueur :", length(numbers))
print("Moyenne :", mean(numbers))
print("Étendue :", range_of_list(numbers))
print("Médiane :", median(numbers))
print("Écart-type :", standard_deviation(numbers))
print("Statistiques complètes :", list_statistics(numbers))

# print("\nListe avec des nombres positifs_entiers :", list_statistics(numbers))       .......affichage total dans une ligne 


# 2. test des Cas particuliers
empty_list = []

try:
    print("\nListe vide :", list_statistics(empty_list))
except ValueError as e:
    print("Erreur :", e)
    
    
one_element_list = [42]
print("\nListe avec un seul élément :", list_statistics(one_element_list))

negative_numbers = [-5, -2, -8, -1]
print("\nListe avec des nombres entier négatifs :", list_statistics(negative_numbers))

floating_numbers = [1.2, 3.4, 5.6, 7.8]
print("\nListe avec des nombres flottants :", list_statistics(floating_numbers))
