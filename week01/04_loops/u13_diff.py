numbers = []

while True:
    user_input = input("Give me a number (negative included), 'q' for quit >> ")
    
    if user_input.casefold() == "q":
        break
    
    try:
        numbers.append(int(user_input))
        
    except ValueError:
        print("Not a number, try again!!")
        
        
numbers.sort()

print(f"The biggest number is: '{numbers[-1]}'.")
print(f"The smallest number is: '{numbers[0]}'.")
print(f"The difference between the numbers is: '{numbers[-1] - numbers[0]}'")