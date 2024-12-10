num = int(input("entrer un nombre entier :"))

if num % 3 == 0  and num % 5 == 0 :
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0 :
    print("Buzz")
else:
    print("No Output !")
    