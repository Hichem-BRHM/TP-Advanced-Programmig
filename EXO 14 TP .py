def function():
    # Demander un mot à l'utilisateur
    word = input("Word: ")
    
    # Largeur totale du cadre
    frame_width = 30
    
    # Calcul des espaces nécessaires de chaque côté
    total_padding = frame_width - len(word) - 2  # 2 pour les étoiles à gauche et à droite
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    
    # Impression du cadre
    print("*" * frame_width)  # Ligne supérieure
    print("*" + " " * left_padding + word + " " * right_padding + "*")  # Ligne avec le mot
    print("*" * frame_width)  # Ligne inférieure

if __name__ == "__main__":
    function()
