from math import sqrt

tal = input("Ange ett tal för att få reda på dess kvadrat >> ")

print(f"Kvadraten av '{tal}' är '{int(tal) **2}'")

sqroot = input("Vill du veta kvadratroten också (y/n) >> ")

if sqroot.casefold() == "y":
    print(f"Kvadratroten av '{tal}' är '{sqrt(int(tal)):.1f}'")