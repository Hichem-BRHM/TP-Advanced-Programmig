name = input("Please enter your name: ")

if name=="VIP" :
  print("Enjoy the show for free!")
else :
  tikets = int(input("How many tickets would you like to buy? "))
  total = tikets * 15.50
  print(f"The total cost is: {total} ")
  print("Enjoy the show for free!")