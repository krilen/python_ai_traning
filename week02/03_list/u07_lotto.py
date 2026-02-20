import random

lotto_numbers = random.sample(range(1, 36), 7)

guessed_numbers = []
correct_numbers = 0

while len(guessed_numbers) < 7:
    
    print(f"Number of tries left: {7-len(guessed_numbers)}")
    print(f"Number of correct numbers: {correct_numbers}")
    
    while True:
        
        try:
            guess = int(input("Guess a number between 1 and 35 to get the lotto >> "))
            
            if guess > 35 or guess < 1:
                print("A number between 1 and 35!")
                continue
            
        except ValueError:
            print("That is not a number, try again!")
            continue
        
        else:
            break
        
    print()
    
    if guess in guessed_numbers:

        print("You have already guessed that number")
        print()
        continue
    
    if guess in lotto_numbers:
        print("Correct, you are one number closer to be the winner")
        correct_numbers += 1
        
    else:
        print("Sorry that is not a correct number")
    
    guessed_numbers.append(guess)
    
    print()

match correct_numbers:
    
    case 7:
        print("You are this weeks winner with all correct numbers!")
        
    case 6:
        print("6 right is very good but you can do better.")
        
    case 5 | 4 | 3:
        print(f"{correct_numbers} right is good but you can do better.")
    
    case 2 | 1:
        print(f"{correct_numbers} right, atleast you got something right.")
        
    case _:
        print("No right, better luck next time.")