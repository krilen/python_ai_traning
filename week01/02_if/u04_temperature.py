temperature = float(input("What is the temperature outside >> "))

match temperature:
    
    case x if x <= 0:
        print("It is cold outside.")
        
    case x if 0 < x <= 10:
        print("Cold but not freezing.")
        
    case x if 10 < x < 20:
        print("We will survive.")
        
    case _:
        print("It may be summer.")