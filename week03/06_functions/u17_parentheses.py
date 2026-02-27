
while True:
    try:
        string_input = list(input("Give me a string of/with parentheses >> "))

    except:
        print("That was not a valid string, try again!")
        continue
    
    else:
        break
    
parentheses_left = string_input.count("(")
parentheses_right = string_input.count(")")

if parentheses_left > parentheses_right:
    print("To many left parentheses!")
    
elif parentheses_left < parentheses_right:
    print("To many right parentheses!")
    
else:
    print("A balance of parentheses.")