number = int(input("Give me a number >> "))

x = 0
y = 1
number_str = "0, 1, "

if number >= 3:
    
    for _ in range(3, number+1):
        
        number_next = x + y
        number_str += str(number_next) +", "
    
        x, y = y, number_next
        
    print(f"Fib scale to your number, '{number}' is '{number_str[:-2]}'.")
    
else:
    print("Can not work with a number that low!")