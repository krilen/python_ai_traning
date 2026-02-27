accounts = {}

def account_create():
    while True:
        account_create_input = input(" Add a new account to be created, atleast 3 charaters ('e' to exit) >> ").casefold()

        if account_create_input == "e":
            break
        
        elif account_create_input == "":
            print(" An account can not be empty, try again!")
            continue
        
        elif len(account_create_input) < 3:
            print(" An account must have 3 charaters or more, try again!")
            continue
        
        if accounts.get(account_create_input, False):
            print(" An account already exists, try again!")
            continue
        
        accounts[account_create_input] = {"balance": 0, "transactions": []}
        break

    return


def account_list():
    print()
    
    if len(accounts) == 0:
        print(" No accounts exists!")
        return
    
    for account, data in accounts.items():
        
        print(f" * Account: '{account}', balance: {data['balance']}")
        
    return


def account_select():
    print()
    
    while True:
        
        account_input = input(" Please enter an account ('e' to exit) >> ").casefold()
        
        if account_input == "e":
            break
        
        account = accounts.get(account_input, None)
        
        if account:
            account_admin(account_input)
            break
        
        else:
            print(f" The account '{account_input}' does not exists, try again!")
            continue

    return


def account_admin(account):
    print()
    
    while True:
        
        menu_account(account)
        print()
        
        selection_input = input(" Please make a selection >> ")
        
        if selection_input == "e":
            break

        try: 
            selection = int(selection_input)
            
            if selection not in [1,2,3,4]:
                raise ValueError
        
        except ValueError:
            print(" Not a valid selection, try again!")
            continue
        
        match selection:
            case 1:
                while True:
                    money_add_input = input(" How much money should be added ('e' to exit) >> ")
                    
                    if money_add_input == "e":
                        print()
                        break
                    
                    try:
                        money_add = int(money_add_input)
                        
                        if money_add < 0:
                            raise ValueError
                        
                    except ValueError:
                        print(" Not a valid amount to be added, try again!")
                        continue
                    
                    else:
                        
                        accounts[account]["balance"] += money_add
                        accounts[account]["transactions"].append(money_add)
                        print()
                        break

            case 2:
                print()
                print(f" Current account balance: '{accounts[account]["balance"]}'.")
                
                if accounts[account]["balance"] <= 0:
                    print(" Not possible to withdraw any money!")
                    print()
                    continue
                
                while True:
                    money_withdraw_input = input(" How much money should be withdrawn ('e' to exit) >> ")
                    
                    if money_withdraw_input == "e":
                        print()
                        break
                    
                    try:
                        money_withdraw = int(money_withdraw_input)
                        
                        if money_withdraw < 0:
                            raise ValueError
                        
                    except ValueError:
                        print(" Not a valid amount to be withdrawn, try again!")
                        continue
                    
                    else:
                        
                        if money_withdraw <= 0:
                            print(" Not a valid amount to be withdrawn, try again!")
                            continue
                        
                        elif accounts[account]["balance"] - money_withdraw < 0:
                            print(f" Not enough money to withdraw '{money_withdraw}', try again!")
                            continue
                        
                        
                        accounts[account]["balance"] -= money_withdraw
                        accounts[account]["transactions"].append(money_withdraw * -1)
                        print()
                        break
            case 3:
                
                print()
                print(f" Current balance in the account: '{accounts[account]["balance"]}'.")
                print()
                
            case 4:
                
                print()
                
                if len(accounts[account]["transactions"]) == 0:
                    print(" No transactions for this account can be found.")
                    
                else:
                    print(" Transactions")
                    for i, transaction in enumerate(accounts[account]["transactions"], start=1):
                        print(f"  {i}. Transaction: '{transaction }'.")
                        
                    print(f" Current balance: '{accounts[account]["balance"]}'.")
                
                print()
                
            case _:
                continue

    return


def menu_main():
    print()
    print(" *** MAIN MENU ***")
    print("  1. Create account")
    print("  2. List accounts")
    print("  3. Administrate account")
    print()
    print("  'q' to quit")

    return


def menu_account(account):
    print(" *** ACCOUNT MENU ***")
    print(f" Account: {account}")
    print("  1. Add money")
    print("  2. Withdraw money")
    print("  3. Show account balance")
    print("  4. List transactions")
    print()
    print("  'e' to exit to main menu")
    
    return


def main():
    
    while True:
        
        menu_main()
        print()
        
        selection_input = input(" Please make a selection >> ")
        
        if selection_input.casefold() == "q":
            break
        
        try: 
            selection = int(selection_input)
            
            if selection not in [1,2,3]:
                raise ValueError
        
        except ValueError:
            print(" Not a valid selection, try again!")
        
        
        match selection:
            
            case 1:
                account_create()
                
            case 2:
                account_list()

            case 3:
                account_select()
            
            case _:
                continue
    pass



if __name__ == "__main__":
    
    main()
    print()
    print(" Thank You. Have a nice day.")
    print()








