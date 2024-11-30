# Vous pouvez placer le script de votre jeu dans ce fichier.

image base = "base_world.png"
image chemical = "chemical_world.png"
image boiling = "boiling_world.png"
image filtration = "filtration_world.png"
image council = "council.png"
image rationing = "rationing_austerity.png"
image expansion = "expansion.png"
image decentralized = "decentralized_energy.png"
image fossil = "fossil_fuels.png"
image renewable = "renewable_energy.png"
image final = "final.png"
# Le jeu commence ici

label start:

    scene base

    play music "mysterious.mp3" volume 0.2

    "Me" "Hello? Is anyone there?"

    "?" "Hello! Who's this? I'm Sylvie."

    "Me" "I'm John. I'm from the future, and I need your help."

    "Sylvie" "The future? What kind of help do you need?"

    "Me" "The future is in crisis. We’re running out of clean water. I need you to make critical decisions to fix things."

    "Sylvie" "This is overwhelming, but I'll do my best. What do I need to do?"

    label main:
        menu:
            "Boil the water.":
                scene boiling
                play sound "loseVoice.mp3" volume 1.0
                "Me" "Oh no! This method has depleted forests. The excessive use of wood for boiling has destroyed ecosystems."
                "Game Over: This path leads to environmental collapse."
                scene base
                jump main

            "Use a chemical purifier.":
                scene chemical
                play sound "loseVoice.mp3" volume 1.0
                "Me" "Oh no! The chemicals have caused long-term health issues and mutations in the population."
                "Game Over: The cure turned out to be worse than the disease."
                scene base
                jump main

            "Build a filtration system.":
                scene filtration
                play sound "Yeah_Impact.mp3" volume 1.0

                "Me" "Yes! The filtration system is effective. The water is clean now."
                "Sylvie" "I'm glad we could fix this. I hope your future improves."
                "Me" "It has, for now. But challenges keep coming. Thank you for your help."

                "Two months later..."
                "Me" "Sylvie, it's me again. The situation is critical once more. I need your guidance."
                "Sylvie" "What should I do this time?"

                label main2:
                    "Me" "Sylvie, I’ve analyzed the situation further. Clean water isn’t enough—we need a sustainable system in place."
                    "Sylvie" "I see. So, we need to make decisions that will ensure the long-term availability of resources?"
                    "Me" "Exactly. Every choice you make now will have a significant impact on the future. Let’s discuss the options."

                    menu:

                        "Promote fair distribution through councils":
                            scene council
                            play sound "Yeah_Impact.mp3" volume 1.0
                            "Me" "Yes! By forming councils, we’ve created a fair system where water is distributed equally."
                            "Sylvie" "That’s great to hear! A cooperative approach seems to be working. What’s the next step?"
                            "Me" "We need to think beyond water now. Energy and sustainability will determine the future."

                            label main3:
                                "Me" "Sylvie, the council is working well, but there’s a new challenge. We need energy to power these systems sustainably."
                                "Sylvie" "That makes sense. What options do we have?"

                                menu:
                                    "Invest in renewable energy sources":
                                        scene renewable
                                        play sound "loseVoice.mp3" volume 1.0
                                        "Me" "Oh no! While renewable energy was a step forward, the infrastructure wasn’t inclusive. Wealth inequality grew, leading to unrest."
                                        "Sylvie" "I didn’t think about the socio-economic impacts. I’ll try something different."
                                        scene council
                                        jump main3

                                    "Tap into fossil fuels for immediate relief":
                                        scene fossil
                                        play sound "loseVoice.mp3" volume 1.0
                                        "Me" "Oh no! Fossil fuels provided temporary relief, but pollution has spiraled out of control, causing severe health problems."
                                        "Sylvie" "Short-term solutions never seem to work out. We need a better plan."
                                        scene council
                                        jump main3
                                    
                                    "Encourage decentralized energy solutions (local communities generate their own power)":
                                        scene decentralized
                                        play sound "Yeah_Impact.mp3" volume 1.0
                                        "Me" "This is perfect! Decentralized energy systems have empowered communities and made them self-reliant."
                                        "Sylvie" "That’s amazing! The people are now more independent, and the environment is recovering too."
                                        "Me" "Thanks to you, Sylvie, the future looks brighter than ever. Your decisions have saved countless lives."
                                        
                                        "2 years later..."
                                        play music "mysterious.mp3" volume 0.2
                                        scene final
                                        "Thank you for playing! Your choices have shaped a better future. The world is now sustainable and thriving."
                                        return

                        "Support expansion into new territories":
                            scene expansion
                            play sound "loseVoice.mp3" volume 1.0
                            "Me" "Oh no! Expanding into uncharted territories disrupted ecosystems and polluted water sources."
                            "Sylvie" "I didn’t realize the consequences would be so devastating. Let’s rethink this."
                            scene filtration
                            jump main2

                        "Rationing and austerity measures":
                            scene rationing
                            play sound "loseVoice.mp3" volume 1.0
                            "Me" "Oh no! Rationing created widespread dissatisfaction, and the lack of resources led to contamination."
                            "Sylvie" "This doesn’t seem to be the right solution. Let’s try something else."
                            scene filtration
                            jump main2

    return
