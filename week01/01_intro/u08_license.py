have_licence = input("Har du tagit ditt körkort (y/n) >> ")

age = int(input("Hur gammal är du >> "))

if have_licence.casefold() == "y" and age < 18:
    print("Omöjligt!!! Man måste vara 18 år eller äldre för att ha körkort.")
    
elif have_licence.casefold() == "y":
    print("Grattis du för köra på vägarna.")
    
elif age >= 18:
    print("Du får lov att ta körkort.")

else:
    print("Du får lov att cykla.")