number = int(input("Give me a number >> "))

number_sum = 0
number_str = ""

while number > 0:
    
    number_str += str(number) + " + "
    number_sum += number
    
    number -= 1
    
print(f"The sum of all number from your number is '{number_str[:-3]} = {number_sum}'.")