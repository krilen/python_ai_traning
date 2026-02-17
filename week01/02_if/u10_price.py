price = int(input("Give me a price >> "))

if price > 1000:
    price = price * 0.9
    
# With tax :)
tax = price * 0.25

print(f"The price is '{(price + tax):.2f}', including the tax of '{tax:.2f}'.")