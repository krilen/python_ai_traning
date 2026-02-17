letter = input("Please give me a letter >> ")

VOWEL = "aeiou"
CONTANT = "bcdfghjklmnpqrstvwxyz"

if letter in VOWEL:
    print(f"The letter, '{letter}', is a vowel.")
    
if letter in CONTANT:
    print(f"The letter, '{letter}', is a constant.")