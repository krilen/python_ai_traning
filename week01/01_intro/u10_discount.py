price = int(input("What is the price of the product >> "))
discount = int(input("What is the discount of the product in % >> "))

discount_value = price * (discount /100)

print(f"The price of the product was '{price}'.")
print(f"With a discount of '{discount}%' you pay '{price -discount_value:.2f}'.")
print(f"You save '{discount_value:.2f}'.")
