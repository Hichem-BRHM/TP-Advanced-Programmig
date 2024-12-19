# Initialize the list
list_number = [1, 2, 3, 4, 5]

while True:
   
        # Ask the user for the index
        index = int(input("Enter index (-1 to quit): "))
        if index == -1:
            print("Exiting operation soon ...")
            print("exit is done")
            break
         
          #   BONUS
        # Verification valeur index index
        if index < 0 or index >= len(list_number):
            print(f"Invalid index. Please enter a value between 0 and {len(list_number) - 1}.")
            continue

        # demander d'entrer une valeur
        val = input("Enter new value: ")
         
        #   BONUS 
        # Verifier si la valeur est un entier sinon un new message pour entrer une nouvelle valeur 
        if not val.isdigit():
            print("Invalid value. Please enter an integer.")
            continue

        # mise a jour de la list
        list_number[index] = int(val)
        print(list_number)

    


