x = float(input("entrer premier nombre entier ou réel: "))
y = float(input("entrer un deuxiéme nombre entier ou réel: "))

char = input("choisis l'un des operatons arithmethique siuvant: ('+' '/' '*' '-') ")

while char != '+' and char != '-' and char != '/' and char != '*' :
    char = input("choisis l'un des operatons arithmethique siuvant: ('+' '/' '*' '-') ")
    
if char == '+' :
    print(f"{x} + {y} = {x+y}")
elif char == '-' :
    print(f"{x} - {y} = {x-y}")
elif char == '*' :
    print(f"{x} * {y} = {x*y}")
else: 
    print(f"{x} / {y} = {x/y}")

    