
n = input("Please enter a positive integer: ")

# Check if the input is a chiffre and positive
if n.isdigit():
    n = int(n)  # Convert to integer
    if n > 0:
        print(f"Please enter a positive integer: {n}") 
        for num in range(-n, n + 1):
            if num != 0:  # 0 noon inclus 
                print(num)
    else:
        print("The number must be positive.")
else:
    print("Invalid input. Please enter a positive integer.")
