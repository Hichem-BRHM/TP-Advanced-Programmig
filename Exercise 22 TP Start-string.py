
# cas 1 : affichage verticallement

caractere = input("Please type in a string: ") # string par defaut

# Iterate over each character in the string
for char in caractere:
    print(char)  
    print("*")      
    
       
# cas 2 : affichage horizentallement :


user_input = input("Please type in a string: ")

# Create a new string with each character followed by a star
resultat = ""
for char in user_input:
    resultat += char + " * "  # Add character and a star to the result string

# Print the result
print(resultat)
