letter1 = input("Enter first letter: ").lower()
letter2 = input("Enter second letter: ").lower()
letter3 = input("Enter third letter: ").lower()

list = [letter1, letter2, letter3]
list.sort()  # Trie la liste alphabétiquement premier au dernier 

# La lettre du milieu sera maintenant à l'index 1 après le tri 


print(f"The middle letter is {list[1]}")
