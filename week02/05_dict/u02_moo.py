animal_sounds = {"cat": "meow (but at 3am it's opera time)", "dog": "woof (professional doorbell impersonator)", "cow": "moo (grass-powered foghorn)", "duck": "quack (angry rubber chicken vibes)", "sheep": "baa (existential screaming softly)", "owl": "hoot (who? who? definitely not me)", "horse": "neigh (long face, loud opinions)", "pig": "oink (snack enthusiast noises)"}

animal_input = input("Provide me with an animal >> ").casefold()

_animal_sound = animal_sounds.get(animal_input .casefold(), None)

if _animal_sound:
    
    animal_sound = _animal_sound.split(" ")
    
    print(f"The animal '{animal_input.lower()}' make a sound like '{animal_sound[0]}'.")
    print(f"or you could say it sounds like '{" ".join(animal_sound[1:])[1:-1]}'.")
else:
    print(f"I do not know how the animal {animal_input.lower()} sounds like.")

