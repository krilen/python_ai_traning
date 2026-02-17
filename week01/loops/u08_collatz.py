number = int(input("Give me a number >> "))

while number != 1:
    
    print(number, "-> ", end="")
    
    if number % 2 == 1:
        number *= 3
        number += 1
        
    else:
        number //= 2
        
print(number)