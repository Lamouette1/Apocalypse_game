# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")

image base = "base_world.png"
image chemical = "chemical_world.png"
image boiling = "boiling_world.png"
image filtration = "filtration_world.png"

# Le jeu commence ici

label start:

    scene base

    menu:
        "Commencer":
            "Me" "Hello? Is anyone there?"

            "?" "Hello! Who is this?"

            "Me" "I'm John. I'm from the future. I need your help."

            "?" "What do you need help with?"

            "Me" "I need you to change the past in order for the future to have celan water, we are dying here."

            "?" "I'm sorry, I don't understand."

            "Me" "I'll tell you what to do."

            menu:
                "Boil the water.":
                    scene boiling
                    "Me" "Oh no! It seems they're is no more trees anymore!."
                    return

                "Use a chemical purifier.":
                    scene chemical
                    "el" "Oh no! There are mutants now."
                    return

                "Build a filtration system.":
                    scene filtration
                    "Me" "Everything seems to be working fine now."
                    return

        "Quitter":
            return

    "The player hears from a group of people in the past that their water source is contaminated, and they are unsure of how to purify it."

    "Me" "Good..."

    "Sylvie" "I can't bring myself to admit that it all went in one ear and out the other."

    "Me" "Are you going home now? Wanna walk back with me?"

    "Sylvie" "Sure!"

    return
