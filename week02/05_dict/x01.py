number1 = 1
number2 = [2]
number3 = {"n1": 3}


def change():
    
    print(number1, number2, number3)
    
    
    
    number1 = 11
    number2.append(22)
    number3["n2"] = 33


def main():
    
    print(number1)
    print(number2)
    print(number3)
    
    change()
    
    print(number1)
    print(number2)
    print(number3)

if __name__ == "__main__":
    
    main()