from random import randint

numbers = [randint(1,101) for _ in range(10)]

while True:
    number_input = input("Give me a number between 1 and 100 >> ")

    try:
        number = int(number_input)
        
        if number > 100:
            raise ValueError
    
    except ValueError:
        print("Not a valid number, try again!")
        continue
    
    else:
        break

numbers.sort()

if number > numbers[-1]:
    print("No bigger number exists.")
    
else:

    for num in numbers:
        if num < number:
            continue
        
        break

    print(f"The bigger number than your input is: {num}.")


print(f"{number=}, {numbers=}")