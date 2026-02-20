numbers = []

while True:
    user_input = input("Give me a number (negative included), 'q' for quit >> ")
    
    if user_input.casefold() == "q":
        break
    
    try:
        numbers.append(int(user_input))
        
    except ValueError:
        print("Not a number, try again!!")
        
swapped_numbers = []

for i in range(1, len(numbers), 2):
    swapped_numbers.append(numbers[i])
    swapped_numbers.append(numbers[i -1])

if len(numbers) % 2 == 1:
    swapped_numbers.append(numbers[-1])

print("The numbers that we got: ", *numbers)
print("The numbers after they have been swapped: ", *swapped_numbers)