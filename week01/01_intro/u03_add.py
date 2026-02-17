print("Låt mig addera två tal åt dig!")

num1 = input("Skriv in det första talet >> ")
num2 = input("Skriv in det andra talet >> ")

if num1.isdigit() and num2.isdigit():
    print(f"Summan blir '{num1} + {num2} = {int(num1) +int(num2)}'")

else:
    if not num1.isdigit() and not num2.isdigit():
        print("Av de angivna talen", end="")

    elif not num1.isdigit():
        print("Det första av de angivna talen", end="")
    
    elif not num2.isdigit():
        print("Det andra av de angivna talen", end="")
        
    print(" är inget heltal")
