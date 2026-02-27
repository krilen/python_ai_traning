

def collatz(number: int =1) -> int:
    
    if not isinstance(number, int):
        return 1
    
    count_steps = 0
    
    while True:
        count_steps += 1
        
        if number == 1:
            print("1", end=": ")
            break
            
        elif number % 2 == 0:
            print(number, end = " -> ")
            number //= 2
            
        
        else:
            print(number, end = " -> ")
            number *= 3
            number += 1
            
            
    return count_steps


print(f"{collatz()} steps")
print(f"{collatz(1)} steps")
print(f"{collatz(2)} steps")
print(f"{collatz(37)} steps")