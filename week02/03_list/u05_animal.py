animals = ["dog", "cat", "cow", "horse", "sheep", "goat", "chicken", "pig", "duck", "rabbit", "deer", "lion", "tiger", "bear", "elephant", "monkey", "zebra", "giraffe", "wolf", "fox"]


user_animals = input("Could you give me three favorite animals, use a space to devide them >> ").split(" ")

common_animals = 0

for user_animal in user_animals:
    
    if user_animal.casefold() in animals:
        common_animals += 1

print(f"We have '{common_animals}' favorite animal{"s" if common_animals > 1 else ""} between each other.")
