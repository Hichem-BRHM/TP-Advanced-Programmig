
prix = float(input("Please type in a price: "))

# Séparer les dinars (partie entière) et les centimes (partie décimale)
partie_entiere = int(prix)  # prendre juste Partie entière du prix
centimes = round((prix - partie_entiere) * 100)  # utiliser "round" pour limiter avoir 2 nombre aprés la virgule puis "*100" pour afficher la partie decimal comme un nmbre séparé de la partie entiére (comme demandé)

# Afficher les résultats
print(f"Dinars: {partie_entiere}")
print(f"Centimes: {centimes}")
