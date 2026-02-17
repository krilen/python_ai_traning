MY_NAME = "jack"
MY_AGE = 27
MY_HOBBY = "netflix"

name = input("Skriv in ditt namn >> ")
age = int(input("Skriv in din ålder >> "))
hobby = input("Skriv in din favorithobby >> ")

print()
print(f"Hejsan '{name.upper()}', mitt namn är '{MY_NAME.upper()}'.")

print(f"Du är '{age}' gammal, jag är '{MY_AGE}' och ", end="")

age_diff = age - MY_AGE

if age_diff < 0:
    print(f"jag är {age_diff * -1} år äldre.")

elif age_diff > 0:
    print(f"jag är {age_diff} år yngre.")
    
else:
    print("vi är lika gamla.")

if MY_HOBBY.casefold() == hobby.casefold():
    print(f"Vi har samma hobby, '{hobby}'.")
    
else:
    print(f"Jag gillar '{MY_HOBBY}' och du gillar '{hobby}'.")

print()
print(f"Trevligt att pratas vid '{name}', hoppas vi hörs snart igen!")