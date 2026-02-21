"""

Not done!!!

"""



dwellings = {}
dwelling = []
tenent = {"name": "", "age": 0, "occupation": "", "phone": ""}

limits = {"houses": [1,2,3,4,5,6], "stair": ["a", "b"], "appartment": [1,2,3,4,5,6,7,8,9,10]}






def list_tenents() {
    
    
    
}




def menu():
    
    while True:
        print()
        print("============== DD dwelling INC ==============")
        print()
        print("Main menu, make your selection")
        print(" - 'l' to list the apartments and the tenents in it")
        print()
        print(" - 'q' to quit the program")
        print()
        
        selection = input("Enter the selection >> ").casefold()
        
        match selection:
            case "q":
                break

            case _:
                print()
                print("No a valid selection, try again!")
    return

if __name__ == "__main__":
    
    menu()
    print()
    print("Thank you.")