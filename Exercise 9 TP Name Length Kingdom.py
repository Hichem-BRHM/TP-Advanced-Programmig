a = True
cities = []  # Liste pour stocker les noms de villes
    
while a == True:
    city = input("Enter the name of a city (or type 'stop' to finish): ")    
    if city.lower() == 'stop':
            break
    else:
        cities.append(city)

    # Trier les villes en fonction de la longueur de leurs noms (ordre décroissant)
    cities.sort(key=len, reverse=True)
    
# Affichage du resultat de traitement juste aprés de saisir 'stop'
print("\n Liste triée selon les populations (longeurs des villes):")
for city in cities:
    population = len(city) * 1000000
    print(f"The city {city} has {len(city)} letters , it's population is {population:,} citizens")