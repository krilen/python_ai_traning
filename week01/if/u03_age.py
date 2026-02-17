age = int(input("How old are you >> "))

match age:
    
    case x if x < 13:
        print("You are a kid.")
        
    case x if 13 <= x < 20:
        print("You are a teenager.")
        
    case x if 20 <= x < 67:
        print("You are an adult.")
        
    case _:
        print("You are a senior citizen.")