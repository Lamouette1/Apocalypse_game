# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")
image logo = "post_apocalyptic.jpg"
# Le jeu commence ici
label start:
    scene logo
    "Sylvie" "Hi there! How was class?"

    "Me" "Good..."

    "Sylvie" "I can't bring myself to admit that it all went in one ear and out the other."

    "Me" "Are you going home now? Wanna walk back with me?"

    "Sylvie" "Sure!"

    return
