

def check_prime(number: int) -> bool:
    
    if not isinstance(number, int) or number < 1:
        return False
    
    if number == 1:
        return True
    
    is_prime = True
    
    for i in range(2, number):
        
        if number % i == 0:
            is_prime = False
            break
        
        
    return is_prime


numbers = ["hello", 2, 7, 12, 19, 25, 31, 12.3, 44, 53, 68, None, 97]

for number in numbers:
    print(f"Is '{number}' a prime number? {check_prime(number)}")

