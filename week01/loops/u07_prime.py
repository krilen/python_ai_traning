number = int(input("Give me a number >> "))

if number > 1:

    for x in range(2, number+1):
                
        for y in range(2, x+1):
            
            if x == y:
                print(f" * '{x} is a prime number'")
                
            elif x % y == 0:
                break
else:
    print("Can not work with a number that low!")