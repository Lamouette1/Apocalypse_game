# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")

image base = "base_world.png"
image chemical = "chemical_world.png"
image boiling = "boiling_world.png"
image filtration = "filtration_world.png"
image council = "council.png"
# Le jeu commence ici

label start:

    scene base

    menu:
        "Commencer":
            "Me" "Hello? Is anyone there?"

            "?" "Hello! Who is this? I'm Sylvie."

            "Me" "I'm John. I'm from the future. I need your help."

            "Sylvie" "What do you need help with?"

            "Me" "I need you to change the past in order for the future to have celan water, we are dying here."

            "Sylvie" "I'm sorry, I don't understand."

            "Me" "I'll tell you what to do."

            label main:
                menu:
                    "Boil the water.":
                        scene boiling
                        play sound "loseVoice.mp3"
                        "Me" "Oh no! It seems they're is no more trees anymore! The excessive use of wood depletes forest resources, leading to fewer trees."
                        "You Lost"
                        scene base
                        jump main

                    "Use a chemical purifier.":
                        scene chemical
                        play sound "loseVoice.mp3"
                        "el" "Oh no! There are mutants now. The long-term exposure to the chemicals mutated the population."
                        "You Lost"
                        scene base
                        jump main

                    "Build a filtration system.":
                        scene filtration
                        play sound "successVoice.mp3"
                        "Me" "Everything seems to be working fine now."
                        
                        "Sylvie" "I'm glad I could help. I hope the future is better now."

                        "Me" "For now, it is. Thank you for your help."

                        "2 month later"

                        "Me" "Hello Sylvie, I need your help again."

                        "Sylvie" "What do you need help with?"

                        "Me" "I need you to"

                        menu:

                            "Promote fair distribution through councils":
                                scene council
                                play sound "successVoice.mp3"
                                "Me" "Yes it worked! The council has been established and the water is now distributed fairly."
                                return

                            "Support expansion into new territories":
                                return
                                scene base
                                play sound "loseVoice.mp3"
                                "Me" "Oh no! The expansion has caused the water to be contaminated."

                        return

        "Quitter":
            return

    "The player hears from a group of people in the past that their water source is contaminated, and they are unsure of how to purify it."

    "Me" "Good..."

    "Sylvie" "I can't bring myself to admit that it all went in one ear and out the other."

    "Me" "Are you going home now? Wanna walk back with me?"

    "Sylvie" "Sure!"

    return
