products = {"apple": 1.99, "banana": 0.79, "milk": 2.49, "bread": 1.89,
            "eggs": 3.29, "cheese": 4.59, "chicken": 7.99, "beef": 9.49,
            "rice": 2.19, "pasta": 1.49, "tomato": 0.99, "potato": 0.69,
            "onion": 0.89, "carrot": 0.79, "yogurt": 1.19, "butter": 2.79,
            "coffee": 5.99, "tea": 3.49, "juice": 2.99, "cereal": 4.29}
cart = {"items": {}, "sum": 0}

def calc_total():
    
    sum = 0
    products_delete = []

    for product, data in cart["items"].items():
        
        if data["amount"] <= 0:
            products_delete.append(product)
        
        else:
            sum += data["total"]
            
    cart["sum"] = sum

    for product_delete in products_delete:
        del cart["items"][product_delete]

    cart["sum"] = sum

    return


def pay():
    if cart["items"]:
        print()
        print("You bought the following products")
        
        for cart_item, cart_data in cart["items"].items():
            print(f" - {cart_item.title()}: {cart_data['amount']} á {round(cart_data['price'], 2)} = {round(cart_data['total'], 2)}")
    
        print(f"For a total of {round(cart["sum"], 2)}.")


def add_product_cart(product, price, amount):
    cart_item = cart["items"].get(product, False)
    
    if cart_item:
        
        if amount == 0:
            amount = 0
            
        else:
            amount = cart_item["amount"] +amount
    
    cart["items"][product] = {"price": price, "amount": amount, "total": (price * amount)}
    
    return   



def show_products():
    print("PRODUCTS")
    
    for i, (product, price) in enumerate(products.items(), start=1):
        print(f" {i if i > 9 else "0" +str(i)}. - {product.title()}, {price}")
    
    return 


def show_cart():
    print("CART")
    
    if cart["items"]:
        for item, data in cart["items"].items():
            print(f" - {item.title()}: {data['amount']} á {data['price']} = {round(data['total'], 2)}")
        
        print(f" Total amount in the cart: {round(cart["sum"], 2)}")
        
    else:
        print(" - empty")

    return


def menu():
    while True:
        
        calc_total()
        
        print("============ REGISTER ============ ")
        print()
        show_products()
        print()
        show_cart()
        print()
        print("Press 'q' to quit and get the amount that are to be payed.")
        
        buy_input = input("Enter the ID of the item that you wish to buy >> ")
        
        if buy_input.casefold() == "q":
            break
        
        try:
            buy_input = int(buy_input)

            if buy_input <= 0 or buy_input > len(products):
                raise ValueError

        except ValueError:
            print("That is not a valid ID for a product, try again! ")
            print()
            continue
        
        # Convert product dict to a list 
        buy_item, buy_price = list(products.items())[buy_input -1]
        
        amount_input = input(f"Enter the number of '{buy_item.title()}' that you wish to buy >> ")
        
        if amount_input.casefold() == "q":
            amount_input = "0"

        try:
            amount_input = int(amount_input)
            
        except ValueError:
            print("That is not a valid number of products to buy, try again! ")
            print()
            continue
        
        add_product_cart(buy_item, buy_price, amount_input)

    return


if __name__ == "__main__":
    
    menu()
    pay()
    
    print()
    print("Thank you.")