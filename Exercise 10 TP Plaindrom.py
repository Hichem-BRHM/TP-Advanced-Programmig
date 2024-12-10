
 # palindrome negative indexing and loops.
    

def is_palindrome(mot):
   
    length = len(mot)
    for i in range(length // 2):  # Loop through the first half of the word
        if mot[i] != mot[-(i + 1)]:  # Compare caractere de debut et fin  
            return False
    return True

#le main pour tester la fonction
if __name__ == "__main__":
     
 mot = input("Enter a word to check if it's a palindrome: ").strip()  #strip pour supprimer les espaces blancs ou les caractères spéciaux au début et à la fin d'une chaîne de caractères

is_palindrome(mot) #appel de la fonction par son nom pour vérifier si palindrome ou pas
 
if is_palindrome(mot) == True :
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")


