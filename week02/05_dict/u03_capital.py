
capital_country = {}

while True:
    
    capital_input = input("Give me a capital ('q' for quit) >> ").lower()
    
    if capital_input == "":
        print("No capital provided, try again!")
        continue 
    
    elif capital_input == "q":
        break
    
    elif capital_input in capital_country.keys():
        print("You have already provided that capital, try another one!")
        continue
    
    while True:
        country_input = input(f"Give me the country where '{capital_input.title()}' is the capital >> ").lower()
    
        if country_input == "":
            print("No country provided, try again!")
            continue 
        
        else:
            break
    
    capital_country[capital_input] = country_input
    
for capital, country in capital_country.items():
    
    print(f"You said that '{capital.title()}' is the capital of '{country.title()}'.")