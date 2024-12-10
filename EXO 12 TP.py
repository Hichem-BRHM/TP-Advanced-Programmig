def AFFICHAGE_RECTANGLE():
    # saisir/demander la largeur et la hauteur
    width = int(input("Width: "))
    height = int(input("Height: "))
    
    # Afficher un rectangle de '#' en fonction de la largeur et de la hauteur
    for _ in range(height):
        print("#" * width)

if __name__ == "__main__":
    AFFICHAGE_RECTANGLE()
