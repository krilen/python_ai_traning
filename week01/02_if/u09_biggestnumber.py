num1 = float(input("Give me the first number >> "))
num2 = float(input("Give me the second number >> "))
num3 = float(input("Give me the third number >> "))

biggest_num = 0

if num1 >= num2 and num1 >= num3:
    print(f"The first number, '{num1}', is the biggest number")
    
elif num2 >= num1 and num2 >= num3:
    print(f"The second number, '{num2}', is the biggest number")
    
else:
    print(f"The third number, '{num3}', is the biggest number")