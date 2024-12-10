# SOLUTION 1 ..................................................................................

""" temp = int(input("Please type in the temperature: "))

if temp < 0 :
    print("It's freezing!")
    print("It's cold!")
    print("It's cool!")
    print("Stay safe!")
    
if temp >= 0 and temp < 10 :
    print("It's cold!")
    print("It's cool!")
    print("Stay safe!")
    
if temp >= 10 and temp < 20 :
    print("It's cool!")
    print("Stay safe!")
    
if temp >= 20 :
    print("Stay safe!")
    
"""
  
# SOLUTION 2 .............................................................


temp = int(input("Please type in the temperature: "))

      # Check the temperature and print the corresponding messages
if temp < 0:
    print("It's freezing!")
if temp < 10:
    print("It's cold!")
if temp < 20:
    print("It's cool!")

# End with the "Stay safe!" message for all states
print("Stay safe!")
