total_amount = float(input("Total amount: "))
items = int(input("NUmber of itmes: "))
Day = input("Day of the week: ")

reduction_par_item = False

if (Day.lower() == "saturday") or (Day.lower() == "sunday") :
    prix1 = total_amount * 0.2
elif (Day.lower() =="monday")  or (Day.lower() =="tuesday") or (Day.lower() =="wednesday") or (Day.lower() =="thursday") or (Day.lower() =="friday") :
    prix1 = total_amount * 0.1
else :
    print("entrer un jour de semaine et non pas n'importe quel chaine de caractére")
    
    
if items > 5 :
    prix2 = total_amount * 0.05
    reduction_par_item = True 
    
if reduction_par_item == True : 
    total_amount = total_amount - prix1 - prix2
else:
    total_amount = total_amount - prix1
    
print(f"Total price after discount {total_amount} dinars")