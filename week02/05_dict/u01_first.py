color_fruits = {}

color_fruits["red"] = "strawberry"
color_fruits["yellow"] = "apple"
color_fruits["green"] = "pear"


print(color_fruits)


color_input = input("Give me a color >> ")

print(f"The color '{color_input.upper()}' is assosiated with the fruit '{color_fruits.get(color_input.casefold(), "not known")}'.")