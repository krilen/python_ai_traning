number = int(input("Give me a number >> "))

number_fac = 1
number_str = str(number) +"! = "

for num in range(number, 0, -1):
    
    number_str += str(num) + " x "
    number_fac *= num
    
print(f"The faculty calculation for your number is '{number_str[:-3]} = {number_fac}'.")

