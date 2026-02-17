while True:
    
    try:
        year = int(input("Provide me with a year >> "))
        
    except:
        print("That was not a number, try again!")
        continue
    
    else:
        break
    
leap_year = " "

if year % 4:
    leap_year = " not "

print(f"The year, '{year}', is{leap_year}a leap year.")