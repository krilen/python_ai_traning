start_value = int(input("Ange startvärdet >> "))
present_value = int(input("Ange nuvarande värde >> "))

round_value = int(input("Hur många nollor skall förändringen avrundas med >> "))

change = ((start_value -present_value)/start_value) *-100

print(f"Den procentuella förändringen är: '{round(change, round_value)}%'")