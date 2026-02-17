number = int(input("Give me a number >> "))
number_is = "odd"

if not number % 2:
    number_is = "even"
    
print(f"The number '{number}' is {number_is}.")


if not number % 3 and not number % 5:
    
    x = number // (3*5)
    
    print(f"The number, '{number}', is also multiple of '3 * 5 * {x} = {number}'.")