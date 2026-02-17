from math import pi

radius = float(input("Give me the radius of the circle >> "))

circumference = round(2 * pi * radius, 2)

if circumference > 50:
    print(f"That is a big circle, {circumference}.")
    
else:
    print(f"That is a small circle, {circumference}.")

