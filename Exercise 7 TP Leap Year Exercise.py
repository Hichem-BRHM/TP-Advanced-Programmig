print("Input:")
year = int(input("Please type in a year: "))
if year % 4 == 0 :
   
    if year % 100 != 0 :
        print("Output :")
        print("that year is leap year") 
    elif year % 400 == 0 :
        print("Output :")
        print("that year is leap year")
    else :
        print("Output :")
        print("That year is not a leap year")
else :
    print("Output :")
    print("That year is not a leap year")