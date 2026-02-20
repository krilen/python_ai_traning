import random

nums = [random.randint(1,100) for _ in range(10)]

#print(nums)

guess = int(input("Guess a number >> "))

if guess in nums:
    print("Ha lucky, you guessed right!")
    
else:
    print("Better luck next time.")