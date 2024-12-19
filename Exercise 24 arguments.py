def anagrams(word1, word2):
    
    # d'abord Vérifiez si les deux chaînes ont la même longueur
    if len(word1) != len(word2):
        return False
    
    # Triez les caractères des deux mots
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    
    # Comparez les deux listes triées
    return sorted_word1 == sorted_word2



# Test 

# Demander à l'utilisateur de saisir deux mots
word1 = input("Entrez le premier mot : ")
word2 = input("Entrez le deuxième mot : ")

# Vérifier si les mots sont des anagrammes en appelant la fonction
if anagrams(word1, word2):
    print(f"'{word1}' et '{word2}' sont des anagrammes.")
else:
    print(f"'{word1}' et '{word2}' ne sont pas des anagrammes.")
