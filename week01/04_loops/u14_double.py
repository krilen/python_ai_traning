numbers = []

while True:
    user_input = input("Give me a number (negative included), 'q' for quit >> ")
    
    if user_input.casefold() == "q":
        break
    
    try:
        numbers.append(int(user_input))
        
    except ValueError:
        print("Not a number, try again!!")
        
unique_numbers = []

for number in numbers:
    
    if not number in unique_numbers:
        unique_numbers.append(number)
        
print("The numbers that we got: ", *numbers)
print("The unique numbers that was given: ", *unique_numbers)